import pygame
import random
from source.config import *

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        try:
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

def gerar_coletavel(jogador, coletaveis_ativos, tempo_restante):
    if len(coletaveis_ativos) >= 3:
        return None

    tipos_na_tela = [item.tipo for item in coletaveis_ativos]

    if random.random() < 0.02: 
        tipos = ['cafe', 'relogio', 'wifi']
        pesos = [20, 40, 40] 

        # lógica do cafézinho
        if jogador.cafe == 1:
            pesos = [60, 20, 20] 
        elif jogador.cafe == 2:
            pesos = [10, 45, 45] 
        elif jogador.cafe >= 3:
            pesos = [0, 50, 50]

        # lógica do wifi 
        if jogador.vidas >= 3:
            pesos[2] = 0   
        elif jogador.vidas == 1:
            pesos[2] = 80 

        # lógica do relogio
        if tempo_restante > 50:
            pesos[1] = 5   
        elif tempo_restante < 15:
            pesos[1] = 80  

        # filtro para repetições
        if 'cafe' in tipos_na_tela: pesos[0] = 0
        if 'relogio' in tipos_na_tela: pesos[1] = 0
        if 'wifi' in tipos_na_tela: pesos[2] = 0

        if sum(pesos) == 0:
            return None

        tipo = random.choices(tipos, weights=pesos, k=1)[0]
        return Coletavel(tipo)
    
    return None