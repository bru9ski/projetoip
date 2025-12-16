import pygame 
import random 

class Inimigo(pygame.sprite.Sprite): 

    def __init__(self, x, y, velocidade_x=2, velocidade_y=0, dano=10):
         super().__init__() #criar superficie
         self.image = pygame.Surface((40, 40)) 
         self.image.fill((255, 0, 0)) 
         self.rect = self.image.get_rect() 
         self.rect.x = x 
         self.rect.y = y #atributo de movimento 
         self.velocidade_x = velocidade_x 
         self.velocidade_y = velocidade_y #atributo de dano 
         self.dano = dano 
    
    def atualizar(self, largura_tela, altura_tela): 
        self.rect.x += self.velocidade_x 
        self.rect.y += self.velocidade_y #wraparound
        if self.rect.x > largura_tela: 
            self.rect.x = -40 
        elif self.rect.x < -40: 
            self.rect.x = largura_tela #manter na tela verticalmente 
        if self.rect.y > altura_tela: 
            self.rect.y = 0 
        elif self.rect.y < 0: self.rect.y = altura_tela 
    
    def desenhar(self, tela): 
        tela.blit(self.image, self.rect) 

    def colidiu(self, player):
        return self.rect.colliderect(player.rect) 
    
    def remover(self): 
        self.kill()
