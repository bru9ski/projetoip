import pygame
from source.config import *

class HUD:
    def __init__(self):
        self.fonte = pygame.font.SysFont("Arial", 24)

    def desenhar(self, tela, tempo_restante, vidas, cafes):
        cor_tempo = VERMELHO if tempo_restante < 10 else BRANCO
        texto_tempo = self.fonte.render(f"Tempo: {tempo_restante}s", True, cor_tempo)
        
        texto_vidas = self.fonte.render(f"Wi-Fi: {vidas}", True, VERDE)
        
        if cafes >= 3:
            texto_cafe = self.fonte.render(f"Cafés: MAX (ESCUDO)", True, CYAN)
        else:
            texto_cafe = self.fonte.render(f"Cafés: {cafes}/3", True, AMARELO)

        tela.blit(texto_tempo, (10, 10))
        tela.blit(texto_vidas, (10, 40))
        tela.blit(texto_cafe, (10, 70))