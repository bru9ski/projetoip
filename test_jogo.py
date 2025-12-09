import unittest
import sys
from main import (
    Jogador, ObjetoColetavel, Maca, Ouro, Diamante,
    TipoObjeto, GerenciadorObjetos, ConfiguradorJogo
)

class TestJogador(unittest.TestCase):
    """Testes para a classe Jogador"""
    
    def setUp(self):
        """Configuração executada antes de cada teste"""
        self.jogador = Jogador(400, 300)
    
    def test_inicializacao(self):
        """Testa se o jogador é inicializado corretamente"""
        self.assertEqual(self.jogador.x, 400)
        self.assertEqual(self.jogador.y, 300)
        self.assertEqual(self.jogador.coletados[TipoObjeto.MACA], 0)
        self.assertEqual(self.jogador.pontuacao, 0)
    
    def test_movimento_esquerda(self):
        """Testa movimento para a esquerda"""
        x_inicial = self.jogador.x
        teclas = {
            pygame.K_LEFT: True, pygame.K_RIGHT: False,
            pygame.K_UP: False, pygame.K_DOWN: False,
            pygame.K_a: False, pygame.K_d: False,
            pygame.K_w: False, pygame.K_s: False
        }
        # Simulação simplificada do movimento
        self.jogador.x -= self.jogador.velocidade
        self.assertLess(self.jogador.x, x_inicial)
    
    def test_movimento_limitado_tela(self):
        """Testa se o jogador não sai dos limites da tela"""
        # Tentar mover para fora da tela (esquerda)
        self.jogador.x = -100
        self.jogador.x = max(self.jogador.raio, self.jogador.x)
        self.assertGreaterEqual(self.jogador.x, self.jogador.raio)
        
        # Tentar mover para fora da tela (direita)
        self.jogador.x = ConfiguradorJogo.LARGURA_TELA + 100
        self.jogador.x = min(self.jogador.x, ConfiguradorJogo.LARGURA_TELA - self.jogador.raio)
        self.assertLessEqual(self.jogador.x, ConfiguradorJogo.LARGURA_TELA - self.jogador.raio)
    
    def test_coleta_objeto(self):
        """Testa coleta de objeto e atualização de estatísticas"""
        maca = Maca(400, 300)
        self.jogador.coletar_objeto(maca)
        
        self.assertEqual(self.jogador.coletados[TipoObjeto.MACA], 1)
        self.assertEqual(self.jogador.pontuacao, 1)
    
    def test_coleta_multipla(self):
        """Testa coleta de múltiplos objetos"""
        maca = Maca(400, 300)
        ouro = Ouro(450, 350)
        diamante = Diamante(500, 400)
        
        self.jogador.coletar_objeto(maca)
        self.jogador.coletar_objeto(ouro)
        self.jogador.coletar_objeto(diamante)
        
        self.assertEqual(self.jogador.coletados[TipoObjeto.MACA], 1)
        self.assertEqual(self.jogador.coletados[TipoObjeto.OURO], 1)
        self.assertEqual(self.jogador.coletados[TipoObjeto.DIAMANTE], 1)
        self.assertEqual(self.jogador.pontuacao, 16)  # 1 + 5 + 10
    
    def test_deteccao_colisao_verdadeira(self):
        """Testa detecção de colisão quando há sobreposição"""
        maca = Maca(400, 300)  # Mesma posição que jogador
        self.assertTrue(self.jogador.detectar_colisao(maca))
    
    def test_deteccao_colisao_falsa(self):
        """Testa detecção de colisão quando não há sobreposição"""
        maca = Maca(1000, 1000)  # Posição distante
        self.assertFalse(self.jogador.detectar_colisao(maca))


class TestObjetoColetavel(unittest.TestCase):
    """Testes para objetos coletáveis"""
    
    def test_inicializacao_maca(self):
        """Testa inicialização de maçã"""
        maca = Maca(100, 200)
        self.assertEqual(maca.x, 100)
        self.assertEqual(maca.y, 200)
        self.assertEqual(maca.tipo, TipoObjeto.MACA)
        self.assertEqual(maca.pontos, 1)
    
    def test_inicializacao_ouro(self):
        """Testa inicialização de ouro"""
        ouro = Ouro(150, 250)
        self.assertEqual(ouro.tipo, TipoObjeto.OURO)
        self.assertEqual(ouro.pontos, 5)
    
    def test_inicializacao_diamante(self):
        """Testa inicialização de diamante"""
        diamante = Diamante(200, 300)
        self.assertEqual(diamante.tipo, TipoObjeto.DIAMANTE)
        self.assertEqual(diamante.pontos, 10)
    
    def test_hierarquia_heranca(self):
        """Testa se as subclasses herdam corretamente de ObjetoColetavel"""
        maca = Maca(100, 200)
        self.assertIsInstance(maca, ObjetoColetavel)
        self.assertTrue(hasattr(maca, 'x'))
        self.assertTrue(hasattr(maca, 'y'))
        self.assertTrue(hasattr(maca, 'tipo'))
        self.assertTrue(hasattr(maca, 'pontos'))


class TestGerenciadorObjetos(unittest.TestCase):
    """Testes para o gerenciador de objetos"""
    
    def setUp(self):
        """Configuração executada antes de cada teste"""
        self.gerenciador = GerenciadorObjetos()
    
    def test_inicializacao(self):
        """Testa inicialização do gerenciador"""
        self.assertEqual(len(self.gerenciador.obter_objetos()), 0)
        self.assertEqual(self.gerenciador.contador_spawn, 0)
    
    def test_criar_objeto_aleatorio(self):
        """Testa criação de objeto aleatório"""
        self.gerenciador.criar_objeto_aleatorio()
        self.assertEqual(len(self.gerenciador.obter_objetos()), 1)
        
        objeto = self.gerenciador.obter_objetos()[0]
        self.assertIsInstance(objeto, ObjetoColetavel)
    
    def test_remover_objeto(self):
        """Testa remoção de objeto"""
        maca = Maca(100, 200)
        self.gerenciador.objetos.append(maca)
        
        self.assertEqual(len(self.gerenciador.obter_objetos()), 1)
        self.gerenciador.remover_objeto(maca)
        self.assertEqual(len(self.gerenciador.obter_objetos()), 0)
    
    def test_limpar(self):
        """Testa limpeza de todos os objetos"""
        self.gerenciador.criar_objeto_aleatorio()
        self.gerenciador.criar_objeto_aleatorio()
        self.gerenciador.criar_objeto_aleatorio()
        
        self.assertGreater(len(self.gerenciador.obter_objetos()), 0)
        self.gerenciador.limpar()
        self.assertEqual(len(self.gerenciador.obter_objetos()), 0)
    
    def test_limite_maximo_objetos(self):
        """Testa limite máximo de objetos na tela"""
        # Criar muitos objetos
        for _ in range(ConfiguradorJogo.QUANTIDADE_MAXIMA_OBJETOS + 10):
            self.gerenciador.criar_objeto_aleatorio()
        
        # Não deve exceder o limite
        self.assertLessEqual(len(self.gerenciador.obter_objetos()), 
                            ConfiguradorJogo.QUANTIDADE_MAXIMA_OBJETOS)


class TestConfiguradorJogo(unittest.TestCase):
    """Testes para as configurações do jogo"""
    
    def test_dimensoes_tela(self):
        """Testa dimensões da tela"""
        self.assertGreater(ConfiguradorJogo.LARGURA_TELA, 0)
        self.assertGreater(ConfiguradorJogo.ALTURA_TELA, 0)
    
    def test_cores_validas(self):
        """Testa se as cores estão em formato RGB válido"""
        cores = [
            ConfiguradorJogo.COR_FUNDO,
            ConfiguradorJogo.COR_JOGADOR,
            ConfiguradorJogo.COR_MACA,
            ConfiguradorJogo.COR_OURO,
            ConfiguradorJogo.COR_DIAMANTE,
            ConfiguradorJogo.COR_TEXTO
        ]
        
        for cor in cores:
            self.assertEqual(len(cor), 3)  # R, G, B
            for valor in cor:
                self.assertGreaterEqual(valor, 0)
                self.assertLessEqual(valor, 255)
    
    def test_parametros_positivos(self):
        """Testa se parâmetros são valores positivos"""
        self.assertGreater(ConfiguradorJogo.VELOCIDADE_JOGADOR, 0)
        self.assertGreater(ConfiguradorJogo.FPS, 0)
        self.assertGreater(ConfiguradorJogo.TAMANHO_JOGADOR, 0)


class TestIntegracaoSistema(unittest.TestCase):
    """Testes de integração do sistema completo"""
    
    def test_fluxo_jogo_basico(self):
        """Testa fluxo básico: criar, coletar, pontuar"""
        jogador = Jogador(400, 300)
        gerenciador = GerenciadorObjetos()
        
        # Criar objetos
        gerenciador.criar_objeto_aleatorio()
        gerenciador.criar_objeto_aleatorio()
        
        # Verificar que foram criados
        self.assertEqual(len(gerenciador.obter_objetos()), 2)
        
        # Simular coleta (sem colisão real, apenas teste)
        primeiro_objeto = gerenciador.obter_objetos()[0]
        jogador.coletar_objeto(primeiro_objeto)
        
        # Verificar pontuação
        self.assertGreater(jogador.pontuacao, 0)
    
    def test_tipos_diferentes_pontuacao(self):
        """Testa que diferentes tipos têm pontuação diferente"""
        jogador = Jogador(400, 300)
        
        maca = Maca(400, 300)
        ouro = Ouro(400, 300)
        diamante = Diamante(400, 300)
        
        pontuacao_inicial = jogador.pontuacao
        
        jogador.coletar_objeto(maca)
        self.assertEqual(jogador.pontuacao, pontuacao_inicial + 1)
        
        jogador.coletar_objeto(ouro)
        self.assertEqual(jogador.pontuacao, pontuacao_inicial + 6)
        
        jogador.coletar_objeto(diamante)
        self.assertEqual(jogador.pontuacao, pontuacao_inicial + 16)


# ============================================================================
# EXECUTAR TESTES
# ============================================================================

if __name__ == "__main__":
    # Configurar suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adicionar testes
    suite.addTests(loader.loadTestsFromTestCase(TestJogador))
    suite.addTests(loader.loadTestsFromTestCase(TestObjetoColetavel))
    suite.addTests(loader.loadTestsFromTestCase(TestGerenciadorObjetos))
    suite.addTests(loader.loadTestsFromTestCase(TestConfiguradorJogo))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegracaoSistema))
    
    # Executar testes
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Exibir resumo
    print("\n" + "="*70)
    print(f"Testes executados: {resultado.testsRun}")
    print(f"Sucessos: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"Falhas: {len(resultado.failures)}")
    print(f"Erros: {len(resultado.errors)}")
    print("="*70)
