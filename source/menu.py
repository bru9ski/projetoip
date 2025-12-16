import pygame
import random
from source.config import *

class Estrela(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.tamanho = random.randint(1, 3)
        self.brilho = random.randint(100, 255)
        self.image = pygame.Surface((self.tamanho, self.tamanho))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_brilho = random.choice([-2, -1, 1, 2])

    def update(self):
        self.brilho += self.velocidade_brilho
        if self.brilho <= 100 or self.brilho >= 255:
            self.velocidade_brilho *= -1

        #brilho
        self.image.fill((self.brilho, self.brilho, self.brilho))

class MenuInicial:
    
    def __init__(self):
        self.font_titulo = pygame.font.Font(None, 80)
        self.font_instrucoes = pygame.font.Font(None, 40)
        self.font_pequeno = pygame.font.Font(None, 24)

        #gerar estrelas
        self.estrelas = pygame.sprite.Group()
        for _ in range(100):
            x = random.randint(0, LARGURA_TELA)
            y = random.randint(0, ALTURA_TELA)
            estrela = Estrela(x, y)
            self.estrelas.add(estrela)

        self.animacao_texto = 0
        self.show_press_start = True

    def desenhar(self, tela):
        #fundo 
        tela.fill(PRETO)
        
        self.estrelas.update()
        self.estrelas.draw(tela)

        # Título
        titulo = self.font_titulo.render("SpaCINvadors", True, CYAN)
        rect_titulo = titulo.get_rect(center=(LARGURA_TELA // 2, 100))
        tela.blit(titulo, rect_titulo)

        self.animacao_texto += 1
        if self.animacao_texto % 60 < 30:
            texto_start = self.font_instrucoes.render("Press START", True, AMARELO)
            rect_start = texto_start.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
            tela.blit(texto_start, rect_start)

        instrucoes = [
            "Sobreviva o máximo de tempo possível!",
            "← → para mover | ESPAÇO para atirar",
            "CAFÉ = Escudo + Tiros rápidos",
            "WI-FI = +1 Vida | RELÓGIO = +10s",
            "",
            "Pressione SPACE para começar"
        ]

        y = ALTURA_TELA // 2 + 100
        for instrucao in instrucoes:
            if instrucao:
                texto = self.font_pequeno.render(instrucao, True, BRANCO)
                rect = texto.get_rect(center=(LARGURA_TELA // 2, y))
                tela.blit(texto, rect)
            y += 35

        pygame.display.flip()

    def esperando_inicio(self):
        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True

            self.desenhar(screen)
            clock.tick(60)

        return False
