import pygame
import random
from source.config import *

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, v_min=3, v_max=6):
        super().__init__()
        try:
            img = pygame.image.load(get_imagem("inimigo.png")).convert_alpha()
            self.image = pygame.transform.scale(img, (50, 50))
        except Exception as e:
            print(f"ERRO ASSET INIMIGO: {e}")
            self.image = pygame.Surface((40, 40))
            self.image.fill(VERMELHO)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.velocidade_y = random.randint(v_min, v_max)

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
        
        if self.rect.right > LARGURA_TELA or self.rect.left < 0:
            self.velocidade_x *= -1
            
        if self.rect.top > ALTURA_TELA:
            self.kill()