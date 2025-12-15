import pygame
import sys
import random
from enum import Enum
from typing import List, Tuple

# ============================================================================
# CONFIGURAÇÕES E CONSTANTES
# ============================================================================

class TipoObjeto(Enum):
    """Enum para os tipos de objetos coletáveis"""
    MACA = 1
    OURO = 2
    DIAMANTE = 3

class ConfiguradorJogo:
    """Classe com todas as configurações do jogo"""
    # Dimensões da tela
    LARGURA_TELA = 800
    ALTURA_TELA = 600
    
    # Cores (RGB)
    COR_FUNDO = (30, 30, 30)
    COR_JOGADOR = (0, 255, 0)
    COR_MACA = (255, 0, 0)
    COR_OURO = (255, 215, 0)
    COR_DIAMANTE = (0, 255, 255)
    COR_TEXTO = (255, 255, 255)
    
    # Jogador
    TAMANHO_JOGADOR = 20
    VELOCIDADE_JOGADOR = 5
    
    # Objetos coletáveis
    TAMANHO_MACA = 12
    TAMANHO_OURO = 15
    TAMANHO_DIAMANTE = 18
    
    # Spawn de objetos
    INTERVALO_SPAWN = 30  # frames
    QUANTIDADE_MAXIMA_OBJETOS = 20
    
    # FPS
    FPS = 60

# ============================================================================
# CLASSES PRINCIPAIS (OOP)
# ============================================================================

class Jogador:
    """
    Classe que representa o jogador no jogo.
    
    Responsabilidades:
    - Armazenar posição e velocidade
    - Processar movimento
    - Detectar colisões com objetos
    - Manter estatísticas de coleta
    """
    
    def __init__(self, x: float, y: float):
        """
        Inicializa o jogador.
        
        Args:
            x: Posição X inicial
            y: Posição Y inicial
        """
        self.x = x
        self.y = y
        self.raio = ConfiguradorJogo.TAMANHO_JOGADOR
        self.velocidade = ConfiguradorJogo.VELOCIDADE_JOGADOR
        
        # Estatísticas de coleta
        self.coletados = {
            TipoObjeto.MACA: 0,
            TipoObjeto.OURO: 0,
            TipoObjeto.DIAMANTE: 0
        }
        
        # Pontuação
        self.pontuacao = 0
    
    def processar_entrada(self, teclas):
        """
        Processa a entrada do teclado e atualiza posição.
        
        Args:
            teclas: Dicionário de teclas pressionadas do pygame
        """
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.velocidade
        
        # Limitar dentro da tela
        self.x = max(self.raio, min(self.x, ConfiguradorJogo.LARGURA_TELA - self.raio))
        self.y = max(self.raio, min(self.y, ConfiguradorJogo.ALTURA_TELA - self.raio))
    
    def detectar_colisao(self, objeto: 'ObjetoColetavel') -> bool:
        """
        Detecta colisão entre o jogador e um objeto coletável.
        
        Args:
            objeto: Objeto a verificar colisão
            
        Returns:
            True se houve colisão, False caso contrário
        """
        distancia = ((self.x - objeto.x)**2 + (self.y - objeto.y)**2)**0.5
        return distancia < (self.raio + objeto.raio)
    
    def coletar_objeto(self, objeto: 'ObjetoColetavel'):
        """
        Coleta um objeto e atualiza estatísticas.
        
        Args:
            objeto: Objeto a ser coletado
        """
        self.coletados[objeto.tipo] += 1
        self.pontuacao += objeto.pontos
    
    def desenhar(self, tela):
        """Desenha o jogador na tela"""
        pygame.draw.circle(tela, ConfiguradorJogo.COR_JOGADOR, 
                         (int(self.x), int(self.y)), self.raio)
    
    def obter_estatisticas(self) -> dict:
        """Retorna as estatísticas do jogador"""
        return {
            'coletados': self.coletados.copy(),
            'pontuacao': self.pontuacao
        }

# testando testando

class ObjetoColetavel:
    """
    Classe base para objetos coletáveis.
    
    Usa Herança - esta é a classe pai que será estendida
    por tipos específicos de objetos.
    """
    
    def __init__(self, x: float, y: float, tipo: TipoObjeto, 
                 raio: int, cor: Tuple[int, int, int], pontos: int):
        """
        Inicializa um objeto coletável.
        
        Args:
            x: Posição X
            y: Posição Y
            tipo: Tipo do objeto (enum TipoObjeto)
            raio: Raio do objeto
            cor: Cor RGB do objeto
            pontos: Pontos ao coletar
        """
        self.x = x
        self.y = y
        self.tipo = tipo
        self.raio = raio
        self.cor = cor
        self.pontos = pontos
    
    def desenhar(self, tela):
        """Desenha o objeto na tela"""
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)
    
    def obter_info(self) -> str:
        """Retorna informações do objeto"""
        return f"{self.tipo.name}: {self.pontos} pts"

# ============================================================================

class Maca(ObjetoColetavel):
    """
    Subclasse de ObjetoColetavel representando uma maçã.
    Exemplo de Herança - estende ObjetoColetavel com valores específicos.
    """
    
    def __init__(self, x: float, y: float):
        """Inicializa uma maçã com valores pré-definidos"""
        super().__init__(
            x=x,
            y=y,
            tipo=TipoObjeto.MACA,
            raio=ConfiguradorJogo.TAMANHO_MACA,
            cor=ConfiguradorJogo.COR_MACA,
            pontos=1
        )

# ============================================================================

class Ouro(ObjetoColetavel):
    """
    Subclasse de ObjetoColetavel representando ouro.
    Exemplo de Herança - estende ObjetoColetavel com valores específicos.
    """
    
    def __init__(self, x: float, y: float):
        """Inicializa ouro com valores pré-definidos"""
        super().__init__(
            x=x,
            y=y,
            tipo=TipoObjeto.OURO,
            raio=ConfiguradorJogo.TAMANHO_OURO,
            cor=ConfiguradorJogo.COR_OURO,
            pontos=5
        )

# ============================================================================

class Diamante(ObjetoColetavel):
    """
    Subclasse de ObjetoColetavel representando diamante.
    Exemplo de Herança - estende ObjetoColetavel com valores específicos.
    """
    
    def __init__(self, x: float, y: float):
        """Inicializa diamante com valores pré-definidos"""
        super().__init__(
            x=x,
            y=y,
            tipo=TipoObjeto.DIAMANTE,
            raio=ConfiguradorJogo.TAMANHO_DIAMANTE,
            cor=ConfiguradorJogo.COR_DIAMANTE,
            pontos=10
        )

# ============================================================================

class GerenciadorObjetos:
    """
    Classe responsável por gerenciar objetos coletáveis.
    
    Responsabilidades:
    - Criar novos objetos aleatoriamente
    - Manter lista de objetos na tela
    - Remover objetos coletados
    """
    
    def __init__(self):
        """Inicializa o gerenciador"""
        self.objetos: List[ObjetoColetavel] = []
        self.contador_spawn = 0
    
    def atualizar(self):
        """Atualiza o gerenciador (spawn de novos objetos)"""
        self.contador_spawn += 1
        
        # Spawn de novo objeto a cada INTERVALO_SPAWN frames
        if (self.contador_spawn >= ConfiguradorJogo.INTERVALO_SPAWN and 
            len(self.objetos) < ConfiguradorJogo.QUANTIDADE_MAXIMA_OBJETOS):
            
            self.criar_objeto_aleatorio()
            self.contador_spawn = 0
    
    def criar_objeto_aleatorio(self):
        """Cria um objeto aleatório em posição aleatória"""
        x = random.randint(30, ConfiguradorJogo.LARGURA_TELA - 30)
        y = random.randint(30, ConfiguradorJogo.ALTURA_TELA - 30)
        
        tipo_aleatorio = random.choice([Maca, Ouro, Diamante])
        novo_objeto = tipo_aleatorio(x, y)
        self.objetos.append(novo_objeto)
    
    def remover_objeto(self, objeto: ObjetoColetavel):
        """Remove um objeto da lista"""
        if objeto in self.objetos:
            self.objetos.remove(objeto)
    
    def obter_objetos(self) -> List[ObjetoColetavel]:
        """Retorna lista de objetos"""
        return self.objetos
    
    def desenhar(self, tela):
        """Desenha todos os objetos"""
        for objeto in self.objetos:
            objeto.desenhar(tela)
    
    def limpar(self):
        """Limpa todos os objetos"""
        self.objetos.clear()
        self.contador_spawn = 0

# ============================================================================

class Jogo:
    """
    Classe principal que controla o fluxo e lógica do jogo.
    
    Responsabilidades:
    - Inicializar pygame
    - Loop principal do jogo
    - Processar eventos
    - Atualizar estado
    - Renderizar elementos
    - Gerenciar transições de estado
    """
    
    def __init__(self):
        """Inicializa o jogo"""
        pygame.init()
        
        self.tela = pygame.display.set_mode(
            (ConfiguradorJogo.LARGURA_TELA, ConfiguradorJogo.ALTURA_TELA)
        )
        pygame.display.set_caption("Jogo de Coleta - OOP em Python")
        
        self.relogio = pygame.time.Clock()
        self.fonte_grande = pygame.font.Font(None, 48)
        self.fonte_media = pygame.font.Font(None, 32)
        self.fonte_pequena = pygame.font.Font(None, 24)
        
        # Estados do jogo
        self.estado = "menu"  # menu, jogando, pausado, gameover
        
        # Inicializar componentes
        self.jogador = None
        self.gerenciador_objetos = None
        self.inicializar_novo_jogo()
    
    def inicializar_novo_jogo(self):
        """Reinicializa o jogo para um novo começo"""
        self.jogador = Jogador(
            ConfiguradorJogo.LARGURA_TELA // 2,
            ConfiguradorJogo.ALTURA_TELA // 2
        )
        self.gerenciador_objetos = GerenciadorObjetos()
        self.estado = "jogando"
    
    def processar_eventos(self):
        """Processa eventos do pygame"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if self.estado == "jogando":
                        self.estado = "pausado"
                    elif self.estado == "pausado":
                        self.estado = "jogando"
                
                if evento.key == pygame.K_SPACE:
                    if self.estado == "menu" or self.estado == "gameover":
                        self.inicializar_novo_jogo()
        
        return True
    
    def atualizar_logica(self):
        """Atualiza a lógica do jogo"""
        if self.estado != "jogando":
            return
        
        # Processar entrada do jogador
        teclas = pygame.key.get_pressed()
        self.jogador.processar_entrada(teclas)
        
        # Atualizar gerenciador de objetos
        self.gerenciador_objetos.atualizar()
        
        # Detectar colisões
        objetos_para_remover = []
        for objeto in self.gerenciador_objetos.obter_objetos():
            if self.jogador.detectar_colisao(objeto):
                self.jogador.coletar_objeto(objeto)
                objetos_para_remover.append(objeto)
        
        # Remover objetos coletados
        for objeto in objetos_para_remover:
            self.gerenciador_objetos.remover_objeto(objeto)
        
        # Verificar condição de game over (exemplo: 50 objetos coletados)
        total_coletados = sum(self.jogador.coletados.values())
        if total_coletados >= 50:
            self.estado = "gameover"
    
    def renderizar_menu(self):
        """Renderiza tela do menu"""
        self.tela.fill(ConfiguradorJogo.COR_FUNDO)
        
        # Título
        titulo = self.fonte_grande.render("JOGO DE COLETA", True, ConfiguradorJogo.COR_TEXTO)
        rect_titulo = titulo.get_rect(
            center=(ConfiguradorJogo.LARGURA_TELA // 2, 100)
        )
        self.tela.blit(titulo, rect_titulo)
        
        # Instruções
        instrucoes = [
            "Colete os objetos e ganhe pontos!",
            "Setas ou WASD para mover",
            "ESC para pausar",
            "Pressione ESPAÇO para começar"
        ]
        
        y_pos = 200
        for instrucao in instrucoes:
            texto = self.fonte_pequena.render(instrucao, True, ConfiguradorJogo.COR_TEXTO)
            rect_texto = texto.get_rect(
                center=(ConfiguradorJogo.LARGURA_TELA // 2, y_pos)
            )
            self.tela.blit(texto, rect_texto)
            y_pos += 50
        
        # Legenda de objetos
        y_pos += 30
        self.fonte_pequena.render("Objetos:", True, ConfiguradorJogo.COR_TEXTO)
        
        objetos_info = [
            ("Maçã (1 pt)", ConfiguradorJogo.COR_MACA),
            ("Ouro (5 pts)", ConfiguradorJogo.COR_OURO),
            ("Diamante (10 pts)", ConfiguradorJogo.COR_DIAMANTE)
        ]
        
        for info, cor in objetos_info:
            texto = self.fonte_pequena.render(info, True, cor)
            rect_texto = texto.get_rect(
                center=(ConfiguradorJogo.LARGURA_TELA // 2, y_pos)
            )
            self.tela.blit(texto, rect_texto)
            y_pos += 40
    
    def renderizar_jogo(self):
        """Renderiza o jogo em execução"""
        self.tela.fill(ConfiguradorJogo.COR_FUNDO)
        
        # Desenhar jogador
        self.jogador.desenhar(self.tela)
        
        # Desenhar objetos
        self.gerenciador_objetos.desenhar(self.tela)
        
        # Desenhar HUD (cabeça-cima)
        self.renderizar_hud()
    
    def renderizar_hud(self):
        """Renderiza a interface de usuário (HUD)"""
        y_offset = 10
        x_offset = 10
        
        # Título
        titulo = self.fonte_media.render("Pontuação", True, ConfiguradorJogo.COR_TEXTO)
        self.tela.blit(titulo, (x_offset, y_offset))
        y_offset += 40
        
        # Estatísticas
        stats = self.jogador.obter_estatisticas()
        
        for tipo_obj, quantidade in stats['coletados'].items():
            cor = self.obter_cor_tipo(tipo_obj)
            texto = self.fonte_pequena.render(
                f"{tipo_obj.name}: {quantidade}",
                True,
                cor
            )
            self.tela.blit(texto, (x_offset, y_offset))
            y_offset += 30
        
        # Pontuação total
        y_offset += 10
        pontuacao_texto = self.fonte_media.render(
            f"Total: {stats['pontuacao']} pts",
            True,
            ConfiguradorJogo.COR_TEXTO
        )
        self.tela.blit(pontuacao_texto, (x_offset, y_offset))
    
    def renderizar_pausa(self):
        """Renderiza overlay de pausa"""
        # Semi-transparente
        overlay = pygame.Surface(
            (ConfiguradorJogo.LARGURA_TELA, ConfiguradorJogo.ALTURA_TELA)
        )
        overlay.set_alpha(100)
        overlay.fill((0, 0, 0))
        self.tela.blit(overlay, (0, 0))
        
        # Texto de pausa
        texto_pausa = self.fonte_grande.render(
            "PAUSADO",
            True,
            ConfiguradorJogo.COR_TEXTO
        )
        rect_pausa = texto_pausa.get_rect(
            center=(ConfiguradorJogo.LARGURA_TELA // 2, 
                   ConfiguradorJogo.ALTURA_TELA // 2)
        )
        self.tela.blit(texto_pausa, rect_pausa)
        
        # Instrução
        instrucao = self.fonte_pequena.render(
            "Pressione ESC para continuar",
            True,
            ConfiguradorJogo.COR_TEXTO
        )
        rect_instrucao = instrucao.get_rect(
            center=(ConfiguradorJogo.LARGURA_TELA // 2, 
                   ConfiguradorJogo.ALTURA_TELA // 2 + 80)
        )
        self.tela.blit(instrucao, rect_instrucao)
    
    def renderizar_gameover(self):
        """Renderiza tela de game over"""
        self.tela.fill(ConfiguradorJogo.COR_FUNDO)
        
        # Título
        titulo = self.fonte_grande.render("FIM DE JOGO!", True, (255, 0, 0))
        rect_titulo = titulo.get_rect(
            center=(ConfiguradorJogo.LARGURA_TELA // 2, 100)
        )
        self.tela.blit(titulo, rect_titulo)
        
        # Estatísticas finais
        stats = self.jogador.obter_estatisticas()
        y_pos = 200
        
        titulo_stats = self.fonte_media.render("Estatísticas Finais:", True, ConfiguradorJogo.COR_TEXTO)
        self.tela.blit(titulo_stats, (ConfiguradorJogo.LARGURA_TELA // 2 - 150, y_pos))
        y_pos += 50
        
        for tipo_obj, quantidade in stats['coletados'].items():
            cor = self.obter_cor_tipo(tipo_obj)
            texto = self.fonte_pequena.render(
                f"{tipo_obj.name}: {quantidade}",
                True,
                cor
            )
            self.tela.blit(texto, (ConfiguradorJogo.LARGURA_TELA // 2 - 100, y_pos))
            y_pos += 40
        
        # Pontuação final
        y_pos += 20
        pontuacao_final = self.fonte_media.render(
            f"Pontuação Total: {stats['pontuacao']} pts",
            True,
            (255, 255, 0)
        )
        self.tela.blit(pontuacao_final, (ConfiguradorJogo.LARGURA_TELA // 2 - 200, y_pos))
        
        # Instrução para reiniciar
        y_pos += 80
        instrucao = self.fonte_pequena.render(
            "Pressione ESPAÇO para jogar novamente",
            True,
            ConfiguradorJogo.COR_TEXTO
        )
        rect_instrucao = instrucao.get_rect(
            center=(ConfiguradorJogo.LARGURA_TELA // 2, y_pos)
        )
        self.tela.blit(instrucao, rect_instrucao)
    
    def obter_cor_tipo(self, tipo: TipoObjeto) -> Tuple[int, int, int]:
        """Retorna a cor correspondente ao tipo de objeto"""
        cores = {
            TipoObjeto.MACA: ConfiguradorJogo.COR_MACA,
            TipoObjeto.OURO: ConfiguradorJogo.COR_OURO,
            TipoObjeto.DIAMANTE: ConfiguradorJogo.COR_DIAMANTE
        }
        return cores.get(tipo, ConfiguradorJogo.COR_TEXTO)
    
    def renderizar(self):
        """Renderiza a tela de acordo com o estado"""
        if self.estado == "menu":
            self.renderizar_menu()
        elif self.estado == "jogando":
            self.renderizar_jogo()
        elif self.estado == "pausado":
            self.renderizar_jogo()
            self.renderizar_pausa()
        elif self.estado == "gameover":
            self.renderizar_gameover()
        
        pygame.display.flip()
    
    def executar(self):
        """Loop principal do jogo"""
        rodando = True
        
        while rodando:
            rodando = self.processar_eventos()
            self.atualizar_logica()
            self.renderizar()
            self.relogio.tick(ConfiguradorJogo.FPS)
        
        pygame.quit()
        sys.exit()

# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Ponto de entrada principal do programa.
    Cria e executa o jogo.
    
    Exemplo de OOP: instanciação de um objeto Jogo e chamada de seu método.
    """
    jogo = Jogo()
    jogo.executar()
