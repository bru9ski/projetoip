import os
import pygame 

# dimensões de tela
LARGURA_TELA = 600
ALTURA_TELA = 800
TITULO_JOGO = "SpaCINvadors"
FPS = 60

# configuração para caminhos
PASTA_SOURCE = os.path.dirname(os.path.abspath(__file__))
PASTA_PROJETO = os.path.dirname(PASTA_SOURCE)
PASTA_IMG = os.path.join(PASTA_PROJETO, "assets", "img")
PASTA_SND = os.path.join(PASTA_PROJETO, "assets", "sound") 

# sistema para pegar imagem
def get_imagem(nome_arquivo):
    return os.path.join(PASTA_IMG, nome_arquivo)

# sistema para pegar audio
def get_som(nome_arquivo):
    return os.path.join(PASTA_SND, nome_arquivo)

# sistema de cache
IMAGENS_CACHE = {}

def carregar_imagem_otimizada(nome_arquivo, tamanho=None):
    chave_cache = (nome_arquivo, tamanho)

    if chave_cache not in IMAGENS_CACHE:
        try:
            caminho = get_imagem(nome_arquivo)
            img = pygame.image.load(caminho).convert_alpha()
            if tamanho:
                img = pygame.transform.scale(img, tamanho)
            IMAGENS_CACHE[chave_cache] = img
        except Exception as e:
            print(f"Erro ao carregar {nome_arquivo}: {e}")
            return None
        
    return IMAGENS_CACHE[chave_cache]

# cores e configurações 
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CYAN = (0, 255, 255)
MARROM = (139, 69, 19)
ROXO = (128, 0, 128) 
TEMPO_INICIAL = 60
VIDAS_INICIAIS = 3
VELOCIDADE_TIRO = 10
COOLDOWN_TIRO_PADRAO = 400