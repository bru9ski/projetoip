import pygame
import random
from source.config import *

class Estrela(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.tamanho = random.randint(1, 3)
        self.brilho = random.randint(50, 255)
        self.image = pygame.Surface((self.tamanho, self.tamanho))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_brilho = random.choice([-2, -1, 1, 2])

    def update(self):
        self.brilho += self.velocidade_brilho
        if self.brilho <= 50 or self.brilho >= 300:
            self.velocidade_brilho *= -1
        
        c = max(0, min(255, self.brilho))
        self.image.fill((c, c, c))

class MenuBase:
    def __init__(self, imagem_fundo):
        self.font_titulo = pygame.font.Font(None, 80)
        self.font_instrucoes = pygame.font.Font(None, 40)
        self.font_pequeno = pygame.font.Font(None, 24)

        try:
            img = pygame.image.load(get_imagem(imagem_fundo)).convert()
            img.set_alpha(200) 
            self.fundo = pygame.transform.scale(img, (LARGURA_TELA, ALTURA_TELA))
        except:
            self.fundo = None

        # estrelas
        self.estrelas = pygame.sprite.Group()
        for _ in range(100):
            x = random.randint(0, LARGURA_TELA)
            y = random.randint(0, ALTURA_TELA)
            self.estrelas.add(Estrela(x, y))
            
        self.animacao_texto = 0

    def desenhar_base(self, canvas):
        if self.fundo:
            canvas.fill(PRETO) 
            canvas.blit(self.fundo, (0, 0))
        else:
            canvas.fill(PRETO)
        
        self.estrelas.update()
        self.estrelas.draw(canvas)

class MenuInicial(MenuBase):
    def __init__(self):
        super().__init__("menu.jpg")

    def executar(self, canvas, funcao_renderizacao):
        esperando = True
        clock = pygame.time.Clock()

        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "sair"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "jogar"
                    if event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_ALT):
                         pygame.display.toggle_fullscreen()

            self.desenhar_base(canvas)

            # título
            titulo = self.font_titulo.render("SpaCINvadors", True, CYAN)
            canvas.blit(titulo, titulo.get_rect(center=(LARGURA_TELA // 2, 170)))

            # Pisca Texto
            self.animacao_texto += 1
            if self.animacao_texto % 60 < 30:
                texto_start = self.font_instrucoes.render("PRESS SPACE", True, AMARELO)
                canvas.blit(texto_start, texto_start.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 100)))

            # Instruções
            instrucoes = [
                "Sobreviva o máximo de tempo possível!",
                "SETAS: Mover | ESPAÇO: Atirar",
                "CAFÉ: Escudo + Tiro Rápido",
                "WI-FI: Vida | RELÓGIO: Tempo",
                "",
                "ALT + ENTER: Tela Cheia"
            ]
            y = ALTURA_TELA // 2 + 20
            for linha in instrucoes:
                txt = self.font_pequeno.render(linha, True, BRANCO)
                canvas.blit(txt, txt.get_rect(center=(LARGURA_TELA // 2, y)))
                y += 30
            funcao_renderizacao()
            clock.tick(60)

class MenuGameOver(MenuBase):
    def __init__(self):
        super().__init__("gameover.jpg") 

    def executar(self, canvas, funcao_renderizacao):
        esperando = True
        clock = pygame.time.Clock()

        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "sair"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "reiniciar"
                    if event.key == pygame.K_ESCAPE:
                        return "sair"
                    if event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_ALT):
                         pygame.display.toggle_fullscreen()

            self.desenhar_base(canvas)

            # Texto GAME OVER
            lbl_go = self.font_titulo.render("GAME OVER", True, VERMELHO)
            canvas.blit(lbl_go, lbl_go.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 50)))

            self.animacao_texto += 1
            if self.animacao_texto % 60 < 30:
                lbl_restart = self.font_instrucoes.render("ESPAÇO para Reiniciar", True, BRANCO)
                canvas.blit(lbl_restart, lbl_restart.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 50)))
            
            lbl_sair = self.font_pequeno.render("ESC para Sair", True, BRANCO)
            canvas.blit(lbl_sair, lbl_sair.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 100)))

            funcao_renderizacao()
            clock.tick(60)