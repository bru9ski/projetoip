import pygame
import random
from source.config import *

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, LARGURA_TELA - 30)
        self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = random.randrange(2, 5)
        
        if self.tipo == 'cafe':
            self.image.fill(AMARELO)  
        elif self.tipo == 'relogio':
            self.image.fill(BRANCO)  
        elif self.tipo == 'wifi':
            self.image.fill(VERDE) 

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.top > ALTURA_TELA:
            self.kill()

def gerar_coletavel():
    chance = random.random()
    if chance < 0.01:
        tipos = ['cafe', 'relogio', 'wifi']
        pesos = [10, 45, 45] 
        tipo = random.choices(tipos, weights=pesos, k=1)[0]
        return Coletavel(tipo)
    return None