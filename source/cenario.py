import pygame
from PIL import Image, ImageSequence
from source.config import LARGURA_TELA, ALTURA_TELA, get_imagem

class Cenario:
    def __init__(self):
        self.frames = []
        self.frame_atual = 0
        self.ultimo_update = 0
        
        PULAR_QUADROS = 2 
        
        self.delay_animacao = 100 
        
        try:
            caminho_arquivo = get_imagem("cenario.gif")
            pil_imagem = Image.open(caminho_arquivo)
            
            for i, frame in enumerate(ImageSequence.Iterator(pil_imagem)):
                
                if i % PULAR_QUADROS != 0:
                    continue

                frame = frame.convert("RGBA")
                
                frame = frame.resize((LARGURA_TELA, ALTURA_TELA), Image.Resampling.NEAREST)
                
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()
                
                imagem_pygame = pygame.image.fromstring(data, size, mode)
                self.frames.append(imagem_pygame)
                
        except Exception as e:
            print(f"ERRO AO CARREGAR GIF: {e}")
            fallback = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
            fallback.fill((0, 0, 0))
            self.frames.append(fallback)

    def update(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_update > self.delay_animacao:
            self.ultimo_update = agora
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)

    def draw(self, superficie):
        if self.frames:
            superficie.blit(self.frames[self.frame_atual], (0, 0))