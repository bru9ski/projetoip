import pygame
import random
from source.config import *

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        try:
            # carrega as imagens
            img = pygame.image.load(get_imagem(f"{self.tipo}.png")).convert_alpha()
            self.image = pygame.transform.scale(img, (35, 35))
        except Exception as e:
            print(f"ERRO ASSET COLETAVEL {self.tipo}: {e}")
            self.image = pygame.Surface((30, 30))
            if self.tipo == 'cafe': self.image.fill(AMARELO)
            elif self.tipo == 'relogio': self.image.fill(BRANCO)
            elif self.tipo == 'wifi': self.image.fill(VERDE)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, LARGURA_TELA - 35)
        self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = random.randrange(2, 5)

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