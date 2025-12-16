import pygame
from source.config import *

class HUD:
    def __init__(self):
        self.fonte = pygame.font.SysFont("Arial", 24)
        self.fonte_gameover = pygame.font.SysFont("Arial", 64, bold=True)

    def desenhar(self, tela, tempo_restante, vidas, cafes):
        # tempo
        cor_tempo = VERMELHO if tempo_restante < 10 else BRANCO
        texto_tempo = self.fonte.render(f"Tempo: {tempo_restante}s", True, cor_tempo)
        
        # vida
        texto_vidas = self.fonte.render(f"Wi-Fi: {vidas}", True, VERDE)
        
        # café 
        if cafes >= 3:
            texto_cafe = self.fonte.render(f"Cafés: MAX (ESCUDO)", True, CYAN)
        else:
            texto_cafe = self.fonte.render(f"Cafés: {cafes}/3", True, AMARELO)

        tela.blit(texto_tempo, (10, 10))
        tela.blit(texto_vidas, (10, 40))
        tela.blit(texto_cafe, (10, 70)) 

    def desenhar_game_over(self, tela):
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(150)
        overlay.fill(PRETO)
        tela.blit(overlay, (0,0))

        texto_fim = self.fonte_gameover.render("GAME OVER", True, VERMELHO)
        rect_fim = texto_fim.get_rect(center=(LARGURA_TELA//2, ALTURA_TELA//2))
        
        texto_instrucao = self.fonte.render("Pressione ESC para sair", True, BRANCO)
        rect_instrucao = texto_instrucao.get_rect(center=(LARGURA_TELA//2, ALTURA_TELA//2 + 60))

        tela.blit(texto_fim, rect_fim)
        tela.blit(texto_instrucao, rect_instrucao)