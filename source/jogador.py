import pygame
from source.config import *

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidade_extra=None):
        super().__init__()
        self.image = pygame.Surface((6, 20)) 
        self.image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        
        if velocidade_extra:
            self.velocidade = velocidade_extra
        else:
            self.velocidade = VELOCIDADE_TIRO

    def update(self):
        self.rect.y -= self.velocidade
        if self.rect.bottom < 0:
            self.kill()

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # carregamento de imagens
        try:
            img_nave = pygame.image.load(get_imagem("nave.png")).convert_alpha()
            img_escudo = pygame.image.load(get_imagem("navescudo.png")).convert_alpha()
            
            self.sprite_normal = pygame.transform.scale(img_nave, (60, 50))
            self.sprite_escudo = pygame.transform.scale(img_escudo, (60, 50))
        except Exception as e:
            print(f"ERRO ASSETS JOGADOR: {e}")
            # Fallback visual
            self.sprite_normal = pygame.Surface((60, 50))
            self.sprite_normal.fill(ROXO)
            self.sprite_escudo = pygame.Surface((60, 50))
            self.sprite_escudo.fill(CYAN)

        self.image = self.sprite_normal
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA_TELA // 2
        self.rect.bottom = ALTURA_TELA - 20
        
        self.velocidade = 7 
        self.vidas = VIDAS_INICIAIS
        
        self.cafe = 0
        self.max_cafe = 3
        
        self.cooldown_tiro = COOLDOWN_TIRO_PADRAO
        self.ultimo_tiro = pygame.time.get_ticks()
        self.grupo_tiros = pygame.sprite.Group()

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade
            
        if self.rect.right > LARGURA_TELA:
            self.rect.right = LARGURA_TELA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA
            
        if self.cafe >= self.max_cafe:
            self.image = self.sprite_escudo
        else:
            self.image = self.sprite_normal

    def atirar(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_tiro > self.cooldown_tiro:
            self.ultimo_tiro = agora
            
            if self.cafe >= self.max_cafe:
                velocidade_atual = VELOCIDADE_TIRO * 3 
            else:
                velocidade_atual = VELOCIDADE_TIRO
                
            novo_tiro = Tiro(self.rect.centerx, self.rect.top, velocidade_atual)
            self.grupo_tiros.add(novo_tiro)
            return novo_tiro
        return None

    def powerup_cafe(self):
        self.cooldown_tiro = max(100, self.cooldown_tiro - 100)
        if self.cafe < self.max_cafe:
            self.cafe += 1

    def powerup_wifi(self):
        if self.vidas < 3:
            self.vidas += 1

    def receber_dano(self):
        if self.cafe >= self.max_cafe:
            self.cafe = 2
        else:
            self.vidas -= 1
            if self.cafe > 0:
                self.cafe -= 1
        return self.vidas <= 0