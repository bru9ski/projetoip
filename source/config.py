import pygame
import random
import os

# dimensões da tela 
LARGURA_TELA = 600
ALTURA_TELA = 800
TITULO_JOGO = "SpaCINvadors"
FPS = 60
PASTA_SOURCE = os.path.dirname(os.path.abspath(__file__))
PASTA_PROJETO = os.path.dirname(PASTA_SOURCE)
PASTA_IMG = os.path.join(PASTA_PROJETO, "assets", "img")

def get_imagem(nome_arquivo):
    return os.path.join(PASTA_IMG, nome_arquivo)

# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CYAN = (0, 255, 255)
MARROM = (139, 69, 19)
ROXO = (128, 0, 128) 

# configurações do jogo
TEMPO_INICIAL = 60
VIDAS_INICIAIS = 3
VELOCIDADE_TIRO = 10
COOLDOWN_TIRO_PADRAO = 400 

pygame.init()