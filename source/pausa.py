import pygame
from source.config import LARGURA_TELA, ALTURA_TELA, PRETO, BRANCO, CYAN, AMARELO

class MenuPausa:

    def __init__(self):
        self.font_titulo = pygame.font.Font(None, 80)
        self.font_instrucoes = pygame.font.Font(None, 40)
        self.font_pequeno = pygame.font.Font(None, 24)
        self.animacao_texto = 0

    def desenhar(self, tela):

        #overlayescuro
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(180)
        overlay.fill(PRETO)
        tela.blit(overlay, (0, 0))

        #pausa
        titulo = self.font_titulo.render("PAUSA", True, AMARELO)
        rect_titulo = titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 100))
        tela.blit(titulo, rect_titulo)

        #piscar
        self.animacao_texto += 1
        if self.animacao_texto % 60 < 30:
            texto_resumir = self.font_instrucoes.render("P para resumir", True, CYAN)
            rect_resumir = texto_resumir.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
            tela.blit(texto_resumir, rect_resumir)

        #opções
        opcoes = [
            "ESC para sair do jogo"
        ]

        y = ALTURA_TELA // 2 + 80
        for opcao in opcoes:
            texto = self.font_pequeno.render(opcao, True, BRANCO)
            rect = texto.get_rect(center=(LARGURA_TELA // 2, y))
            tela.blit(texto, rect)
            y += 40

        pygame.display.flip()

    def aguardar_resumo(self, tela):
        pausado = True
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "sair"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return "continuar"
                    if event.key == pygame.K_ESCAPE:
                        return "sair"

            self.desenhar(tela)
