import pygame
import sys
from source.config import *
from source.inimigos import Inimigo
from source.jogador import Jogador
from source.coletaveis import gerar_coletavel
from source.cenario import Cenario
from source.hud import HUD
from source.menu import MenuInicial, MenuGameOver
from source.pausa import MenuPausa

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        try:
            self.sfx_pega_escudo = pygame.mixer.Sound(get_som("pegaescudo.wav"))
            self.sfx_pega_escudo.set_volume(0.8)
            # duração do som
            self.duracao_sfx_escudo = self.sfx_pega_escudo.get_length() * 1000
        except Exception as e:
            print(f"Erro ao carregar SFX pegaescudo: {e}")
            self.sfx_pega_escudo = None
            self.duracao_sfx_escudo = 0

        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.RESIZABLE)
        pygame.display.set_caption(TITULO_JOGO)
        
        self.canvas = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        self.clock = pygame.time.Clock()
        
        self.cenario = Cenario() 
        self.hud = HUD()
        self.menu_pausa = MenuPausa()
        self.menu_gameover = MenuGameOver()
        
        self.rodando = True
        
        # estados de música
        self.estado_musical = "NORMAL" 
        self.tempo_inicio_transicao = 0
        
        self.reiniciar_jogo(tocar_musica=False)

    def reiniciar_jogo(self, tocar_musica=True):
        self.game_over = False
        self.pausado = False
        self.tempo_restante = TEMPO_INICIAL
        self.evento_segundo = pygame.USEREVENT + 1
        pygame.time.set_timer(self.evento_segundo, 1000)
        
        self.jogador = Jogador()
        self.sprites_todos = pygame.sprite.Group()
        self.sprites_todos.add(self.jogador)
        self.inimigos = pygame.sprite.Group()
        self.coletaveis = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()
        
        self.estado_musical = "NORMAL"
        
        for i in range(5):
            self.criar_inimigo()

        if tocar_musica:
            self.tocar_musica_principal()

    def tocar_musica_principal(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(get_som("rolajogo.wav"))
            pygame.mixer.music.set_volume(0.4) 
            pygame.mixer.music.play(-1, fade_ms=3000) 
            self.estado_musical = "NORMAL"
        except Exception as e:
            print(f"Erro ao tocar rolajogo: {e}")

    def criar_inimigo(self):
        import random
        inimigo = Inimigo(random.randint(20, LARGURA_TELA - 60), random.randint(-100, -40))
        self.inimigos.add(inimigo)
        self.sprites_todos.add(inimigo)

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_ALT):
                    if self.tela.get_flags() & pygame.FULLSCREEN:
                        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.RESIZABLE)
                    else:
                        self.tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                    acao = self.menu_pausa.executar(self.canvas, self.renderizar_tela_final)
                    pygame.mixer.music.unpause()
                    if acao == "sair":
                        self.rodando = False

            if event.type == self.evento_segundo:
                self.tempo_restante -= 1
                if self.tempo_restante <= 0:
                    self.game_over = True

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                tiro_ou_lista = self.jogador.atirar()
                if tiro_ou_lista:
                    if isinstance(tiro_ou_lista, list):
                        for t in tiro_ou_lista:
                            self.tiros.add(t)
                            self.sprites_todos.add(t)
                    else:
                        self.tiros.add(tiro_ou_lista)
                        self.sprites_todos.add(tiro_ou_lista)

    def gerenciar_musica_dinamica(self):
        agora = pygame.time.get_ticks()

        # inicio da transição do escudo
        if self.jogador.cafe >= 3 and self.estado_musical == "NORMAL":
            pygame.mixer.music.stop()
            
            if self.sfx_pega_escudo:
                self.sfx_pega_escudo.play()
            
            self.estado_musical = "TRANSICAO"
            self.tempo_inicio_transicao = agora

        elif self.estado_musical == "TRANSICAO":
            # espera o som acabar
            tempo_espera_exato = self.duracao_sfx_escudo - 42 
            
            if agora - self.tempo_inicio_transicao > tempo_espera_exato:
                try:
                    pygame.mixer.music.load(get_som("musicaescudo.wav"))
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    self.estado_musical = "ESCUDO"
                except:
                    self.estado_musical = "ESCUDO"

        # para voltar ao normal
        elif self.jogador.cafe < 3 and (self.estado_musical == "ESCUDO" or self.estado_musical == "TRANSICAO"):
            self.tocar_musica_principal()

    def atualizar(self):
        self.cenario.update()
        self.sprites_todos.update()
        self.gerenciar_musica_dinamica()

        novo_item = gerar_coletavel(self.jogador, self.coletaveis, self.tempo_restante)
        if novo_item:
            self.coletaveis.add(novo_item)
            self.sprites_todos.add(novo_item)

        if self.jogador.cafe >= 3:
            limite = 8; v_min = 6; v_max = 9
        else:
            limite = 5; v_min = 3; v_max = 6

        if len(self.inimigos) < limite:
            import random
            novo_inimigo = Inimigo(random.randint(0, LARGURA_TELA-40), -40, v_min, v_max)
            self.inimigos.add(novo_inimigo)
            self.sprites_todos.add(novo_inimigo)

        pygame.sprite.groupcollide(self.inimigos, self.tiros, True, True)

        hits_coletavel = pygame.sprite.spritecollide(self.jogador, self.coletaveis, True)
        for item in hits_coletavel:
            if item.tipo == 'cafe': self.jogador.powerup_cafe()
            elif item.tipo == 'relogio': self.tempo_restante += 10
            elif item.tipo == 'wifi': self.jogador.powerup_wifi()

        inimigos_colidindo = pygame.sprite.spritecollide(self.jogador, self.inimigos, True)
        if inimigos_colidindo:
            morreu = self.jogador.receber_dano()
            if morreu:
                pygame.mixer.music.stop()
                self.game_over = True

    def renderizar_tela_final(self):
        largura_janela, altura_janela = self.tela.get_size()
        escala = min(largura_janela / LARGURA_TELA, altura_janela / ALTURA_TELA)
        nova_largura = int(LARGURA_TELA * escala)
        nova_altura = int(ALTURA_TELA * escala)
        x_offset = (largura_janela - nova_largura) // 2
        y_offset = (altura_janela - nova_altura) // 2
        img_escalada = pygame.transform.scale(self.canvas, (nova_largura, nova_altura))
        self.tela.fill(PRETO)
        self.tela.blit(img_escalada, (x_offset, y_offset))
        pygame.display.flip()

    def desenhar_jogo(self):
        self.cenario.draw(self.canvas) 
        self.sprites_todos.draw(self.canvas)
        self.hud.desenhar(self.canvas, self.tempo_restante, self.jogador.vidas, self.jogador.cafe)
        self.renderizar_tela_final()

    def executar(self):
        menu = MenuInicial()
        acao = menu.executar(self.canvas, self.renderizar_tela_final)
        
        if acao == "sair":
            pygame.quit()
            sys.exit()

        if acao == "jogar":
            self.reiniciar_jogo(tocar_musica=True) 

        while self.rodando:
            if self.game_over:
                acao_go = self.menu_gameover.executar(self.canvas, self.renderizar_tela_final)
                if acao_go == "reiniciar":
                    self.reiniciar_jogo(tocar_musica=True)
                else:
                    self.rodando = False
            else:
                self.processar_eventos()
                self.atualizar()
                self.desenhar_jogo()
                self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()