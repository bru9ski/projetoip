import pygame
from .config import LARGURA_TELA, ALTURA_TELA

class Cenario:
    def __init__(self):
        self.image = pygame.image.load("cenarioespaco.png").convert()
        
        self.image = pygame.transform.scale(self.image, (LARGURA_TELA, ALTURA_TELA))
        
        self.height = self.image.get_height()
        self.scroll = 0
        self.velocidade = 5

    def update(self):
        self.scroll += self.velocidade

    def draw(self, superficie):
        rel_y = self.scroll % self.height
        
        superficie.blit(self.image, (0, rel_y))
        superficie.blit(self.image, (0, rel_y - self.height))