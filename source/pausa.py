import pygame
from source.config import *

class MenuPausa:
    def __init__(self):
        self.font_titulo = pygame.font.Font(None, 80)
        self.font_instrucoes = pygame.font.Font(None, 40)
        self.font_pequeno = pygame.font.Font(None, 24)
        self.animacao = 0

    def executar(self, canvas, funcao_renderizacao):
        pausado = True
        clock = pygame.time.Clock()

        # Cria um overlay escuro sobre o jogo atual
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(150)
        overlay.fill(PRETO)
        
        # Salva o estado atual do jogo 
        fundo_congelado = canvas.copy()

        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "sair"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return "continuar"
                    if event.key == pygame.K_ESCAPE:
                        return "sair"
                    # Permite alternar tela cheia também no pause
                    if event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_ALT):
                         pygame.display.toggle_fullscreen()

            canvas.blit(fundo_congelado, (0, 0))
            canvas.blit(overlay, (0, 0))

            titulo = self.font_titulo.render("PAUSA", True, AMARELO)
            canvas.blit(titulo, titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 50)))

            self.animacao += 1
            if self.animacao % 60 < 30:
                txt = self.font_instrucoes.render("P para Continuar", True, CYAN)
                canvas.blit(txt, txt.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 20)))

            txt_sair = self.font_pequeno.render("ESC para Sair do Jogo", True, BRANCO)

            canvas.blit(txt_sair, txt_sair.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 80)))

            funcao_renderizacao()
            clock.tick(60)