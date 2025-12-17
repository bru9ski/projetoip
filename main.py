import pygame
import sys
from source.config import *
from source.inimigos import Inimigo
from source.jogador import Jogador
from source.coletaveis import gerar_coletavel
from source.cenario import Cenario
from source.hud import HUD
from source.menu import MenuInicial
from source.pausa import MenuPausa

class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption(TITULO_JOGO)
        self.clock = pygame.time.Clock()
        self.cenario = Cenario()
        self.hud = HUD()
        self.menu_pausa = MenuPausa()
        
        self.rodando = True
        self.pausado = False
        self.game_over = False
        self.tempo_restante = TEMPO_INICIAL
        self.evento_segundo = pygame.USEREVENT + 1
        pygame.time.set_timer(self.evento_segundo, 1000)
        self.inicializar_sprites()

    def inicializar_sprites(self):
        self.jogador = Jogador()
        self.sprites_todos = pygame.sprite.Group()
        self.sprites_todos.add(self.jogador)
        self.inimigos = pygame.sprite.Group()
        self.coletaveis = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()

        for i in range(5):
            inimigo = Inimigo(i * 150 + 20, 50)
            self.inimigos.add(inimigo)
            self.sprites_todos.add(inimigo)

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

            #pausa
            if not self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.pausado = not self.pausado

            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.rodando = False

            if not self.game_over and not self.pausado:
                if event.type == self.evento_segundo:
                    self.tempo_restante -= 1
                    if self.tempo_restante <= 0:
                        self.game_over = True

                #autofogo
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_SPACE]:
                    tiro = self.jogador.atirar()
                    if tiro:
                        self.tiros.add(tiro)
                        self.sprites_todos.add(tiro)

    def atualizar(self):
        if self.game_over or self.pausado:
            return
        
        self.cenario.update()
        self.sprites_todos.update()

        novo_item = gerar_coletavel()
        if novo_item:
            self.coletaveis.add(novo_item)
            self.sprites_todos.add(novo_item)

        #logica dificuldade
        if self.jogador.cafe >= 3:
            limite_inimigos = 8
            vel_min = 6
            vel_max = 9
        else:
            #normal
            limite_inimigos = 5
            vel_min = 3
            vel_max = 6

        #respawn
        if len(self.inimigos) < limite_inimigos:
            import random
            novo_inimigo = Inimigo(
                random.randint(0, LARGURA_TELA-40),
                -40,
                v_min=vel_min,
                v_max=vel_max
            )
            self.inimigos.add(novo_inimigo)
            self.sprites_todos.add(novo_inimigo)

        #colisões
        pygame.sprite.groupcollide(self.inimigos, self.tiros, True, True)

        hits_coletavel = pygame.sprite.spritecollide(self.jogador, self.coletaveis, True)
        for item in hits_coletavel:
            if item.tipo == 'cafe':
                self.jogador.powerup_cafe()
            elif item.tipo == 'relogio':
                self.tempo_restante += 10
            elif item.tipo == 'wifi':
                self.jogador.powerup_wifi()

        hits_dano = pygame.sprite.spritecollide(self.jogador, self.inimigos, True)
        if hits_dano:
            morreu = self.jogador.receber_dano()
            if morreu:
                self.game_over = True

    def desenhar(self):
        self.cenario.draw(self.tela)
        self.sprites_todos.draw(self.tela)

        if self.game_over:
            self.hud.desenhar_game_over(self.tela)
        else:
            self.hud.desenhar(self.tela, self.tempo_restante, self.jogador.vidas, self.jogador.cafe)
            
            #pausa
            if self.pausado:
                font_pausa = pygame.font.Font(None, 40)
                texto_pausa = font_pausa.render("[PAUSADO - P para continuar]", True, AMARELO)
                rect_pausa = texto_pausa.get_rect(center=(LARGURA_TELA // 2, 30))
                self.tela.blit(texto_pausa, rect_pausa)

        pygame.display.flip()

    def executar(self):
        #menu inicial
        menu = MenuInicial()
        
        if not menu.esperando_inicio():
            pygame.quit()
            sys.exit()

        while self.rodando:
            self.processar_eventos()
            
            if self.pausado:
                resultado = self.menu_pausa.aguardar_resumo(self.tela)
                if resultado == "sair":
                    self.rodando = False
                elif resultado == "continuar":
                    self.pausado = False
            
            self.atualizar()
            self.desenhar()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()