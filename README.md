# 🎮 Jogo de Coleta - Sistema 2D em Python

## Descrição

Sistema interativo em ambiente 2D desenvolvido com **Python e Pygame**, onde o jogador controla um objeto para coletar outros objetos dispostos na tela. O projeto implementa conceitos de **Orientação a Objetos** com classes, herança, polimorfismo e encapsulamento.

**Requisitos Implementados:**
- ✅ Sistema interativo 2D controlável
- ✅ 3 tipos distintos de objetos coletáveis (Maçã, Ouro, Diamante)
- ✅ Registro de quantidade coletada por tipo
- ✅ Arquitetura baseada em Orientação a Objetos
- ✅ Exibição de informações ao usuário (HUD)

---

## Tecnologias Utilizadas

### Bibliotecas Principais

| Biblioteca | Versão | Justificativa |
|-----------|--------|---------------|
| **Pygame** | >= 2.1.0 | Biblioteca recomendada para jogos 2D em Python. Fornece renderização gráfica, detecção de eventos, gerenciamento de frames e facilidades para sprites. |
| **Python** | >= 3.8 | Linguagem do projeto com suporte a OOP, type hints e recursos modernos. |

### Módulos Python Utilizados

- **`pygame`** - Renderização gráfica e loop do jogo
- **`sys`** - Saída do programa
- **`random`** - Geração aleatória de posições e tipos de objetos
- **`enum`** - Enumeração de tipos de objetos
- **`typing`** - Type hints para melhor documentação do código

---

## Arquitetura do Projeto

```
.
├── main.py                  # Arquivo principal com toda a lógica
├── requirements.txt         # Dependências do projeto
├── README.md               # Este arquivo
└── assets/                 # (Opcional) Sprites e recursos
```

### Estrutura de Classes

```
┌─────────────────────────────────────────┐
│           APLICAÇÃO PRINCIPAL           │
├─────────────────────────────────────────┤
│                  Jogo                   │
│  - executar()                           │
│  - processar_eventos()                  │
│  - atualizar_logica()                   │
│  - renderizar()                         │
├─────────────────────────────────────────┤
│    ↑ Componentes Principais ↑           │
├─────────────────────────────────────────┤
│ Jogador │ GerenciadorObjetos │ Config  │
├─────────────────────────────────────────┤
│   ↑ Hierarquia de Objetos Coletáveis ↑  │
├─────────────────────────────────────────┤
│      ObjetoColetavel (classe base)      │
│           ↑         ↑         ↑         │
│         Maçã      Ouro    Diamante      │
└─────────────────────────────────────────┘
```

### Descrição das Classes

#### `ConfiguradorJogo`
Classe com todas as constantes do jogo (dimensões, cores, velocidades).
- **Padrão:** Singleton com atributos de classe
- **Uso:** Centraliza configurações para fácil manutenção

#### `Jogador`
Representa o jogador controlável no jogo.
- **Responsabilidades:**
  - Armazenar posição (x, y) e velocidade
  - Processar entrada do teclado
  - Detectar colisões com objetos
  - Manter estatísticas de coleta
- **Métodos principais:**
  - `processar_entrada()` - Atualiza posição baseado em teclas pressionadas
  - `detectar_colisao()` - Verifica colisão com objeto
  - `coletar_objeto()` - Registra coleta e atualiza pontuação

#### `ObjetoColetavel` (Classe Base)
Classe abstrata que define a interface para objetos coletáveis.
- **Responsabilidades:**
  - Armazenar posição, tipo, aparência e valor
  - Fornecer método de desenho
- **Conceito:** **Herança** - base para Maçã, Ouro e Diamante
- **Padrão:** Template base para subclasses

#### `Maca`, `Ouro`, `Diamante` (Subclasses)
Especializações de `ObjetoColetavel`.
- **Conceito:** **Herança e Polimorfismo**
- Cada subclasse define valores específicos (cor, tamanho, pontos)
- Herdadas de `ObjetoColetavel` reutilizam método `desenhar()`

#### `GerenciadorObjetos`
Responsável pelo ciclo de vida dos objetos coletáveis.
- **Responsabilidades:**
  - Criar objetos aleatoriamente
  - Manter lista de objetos na tela
  - Remover objetos coletados
  - Limitar número máximo de objetos
- **Métodos principais:**
  - `atualizar()` - Spawn automático de novos objetos
  - `criar_objeto_aleatorio()` - Instancia um dos 3 tipos aleatoriamente
  - `desenhar()` - Renderiza todos os objetos

#### `Jogo`
Classe principal que orquestra todo o sistema.
- **Responsabilidades:**
  - Inicializar Pygame
  - Loop principal do jogo
  - Processar eventos (teclado, quit)
  - Atualizar lógica (colisões, spawn)
  - Renderizar estado atual
  - Gerenciar transições de estado
- **Estados:** `menu` → `jogando` → `pausado` → `gameover`
- **Métodos principais:**
  - `executar()` - Loop principal
  - `processar_eventos()` - Trata entrada do usuário
  - `atualizar_logica()` - Atualiza posições e colisões
  - `renderizar()` - Desenha na tela

---

## Conceitos de OOP Utilizados

| Conceito | Localização | Descrição |
|----------|-------------|-----------|
| **Classes** | Todas as classes | Estruturas que encapsulam dados e comportamentos |
| **Herança** | `Maca`, `Ouro`, `Diamante` estendem `ObjetoColetavel` | Reutilização de código e especialização |
| **Polimorfismo** | `desenhar()` chamado em `ObjetoColetavel` e subclasses | Mesmo método com comportamento específico |
| **Encapsulamento** | Atributos privados (`self.x`, `self.y`) | Dados protegidos dentro de classes |
| **Composição** | `Jogo` contém `Jogador` e `GerenciadorObjetos` | Objetos compostos por outros objetos |
| **Type Hints** | `typing.List`, `typing.Tuple` | Documentação e validação de tipos |
| **Enum** | `TipoObjeto` | Enumeração segura de tipos |

---

## Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe o projeto:**
```bash
cd projeto_jogo_coleta
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

---

## 🎮 Controles do Jogo

| Ação | Tecla |
|------|-------|
| Mover Esquerda | Seta ← ou **A** |
| Mover Direita | Seta → ou **D** |
| Mover Cima | Seta ↑ ou **W** |
| Mover Baixo | Seta ↓ ou **S** |
| Pausar/Despausar | **ESC** |
| Começar/Reiniciar | **ESPAÇO** |
| Sair | **X** ou fechar janela |

---

## Mecânicas do Jogo

### Objetivo
Coletar o máximo de objetos possível para ganhar pontos.

### Objetos Coletáveis

| Objeto | Cor | Tamanho | Pontos | Frequência |
|--------|-----|--------|--------|-----------|
| **Maçã** 🍎 | Vermelho | 12px | 1 | Comum |
| **Ouro** 💰 | Dourado | 15px | 5 | Raro |
| **Diamante** 💎 | Ciano | 18px | 10 | Muito Raro |

### Estados do Jogo

1. **Menu**
   - Exibe instruções
   - Mostra legenda de objetos
   - Pressione ESPAÇO para começar

2. **Jogando**
   - Controle o círculo verde com setas/WASD
   - Colida com objetos para coletá-los
   - HUD mostra quantidade coletada de cada tipo
   - ESC para pausar

3. **Pausado**
   - Jogo congelado
   - ESC para continuar

4. **Game Over**
   - Acionado ao atingir 50 objetos coletados
   - Mostra estatísticas finais
   - ESPAÇO para jogar novamente

---

## Progressão e Dificuldade

- Máximo de 20 objetos na tela simultaneamente
- Novos objetos aparecem a cada 30 frames (~2 segundos em 60 FPS)
- Fim do jogo: atingir 50 objetos coletados
- Sem aumento de dificuldade (versão base)

---

## Testes

### Teste Manual de Funcionalidades

- [ ] Menu exibe corretamente
- [ ] Movimento do jogador funciona em 4 direções
- [ ] Objetos aparecem aleatoriamente
- [ ] Colisões são detectadas
- [ ] Pontuação atualiza corretamente
- [ ] HUD mostra dados atualizados
- [ ] Pausa/unpause funcionam
- [ ] Game over dispara ao atingir 50 objetos
- [ ] Reiniciar limpa dados anteriores

### Como Executar Testes

```bash
# (Testes automáticos podem ser adicionados)
python -m unittest tests/
```

---

## Features Futuras / Extensões

### Melhorias Propostas
- [ ] Sistema de fases com dificuldade progressiva
- [ ] Inimigos que reduzem pontuação
- [ ] Power-ups (2x pontos, escudo, etc.)
- [ ] Placar de high-score (persistência em arquivo)
- [ ] Sprites customizados e animações
- [ ] Sistema de som (coleta, background)
- [ ] Modo multiplayer local
- [ ] Efeitos visuais (partículas)
- [ ] Menu de pausar com opções
- [ ] Diferentes mapas/ambientes

### Implementação Sugerida
```python
# Exemplo: adicionar power-ups
class PowerUp(ObjetoColetavel):
    def __init__(self, x, y, tipo):
        super().__init__(x, y, TipoObjeto.POWERUP, ...)
    
    def aplicar_efeito(self, jogador):
        """Aplica efeito especial ao jogador"""
        pass
```

---

## Estrutura de Código

### Organização e Estilo

- **PEP 8 Compliance:** Código segue padrões Python
- **Documentação:** Docstrings em todas as classes e métodos
- **Type Hints:** Anotações de tipo para maior clareza
- **Comentários:** Explicações de seções importantes
- **Separação de Conceitos:** Cada classe tem responsabilidade única

### Exemplo de Boa Prática
```python
class Jogador:
    """Classe que representa o jogador no jogo."""
    
    def __init__(self, x: float, y: float):
        """Inicializa o jogador em uma posição."""
        self.x = x
        self.y = y
        self.velocidade = ConfiguradorJogo.VELOCIDADE_JOGADOR
    
    def processar_entrada(self, teclas):
        """Processa entrada do teclado e atualiza posição."""
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
```

---

## Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'pygame'"
**Solução:** Instale pygame com `pip install pygame`

### Problema: Jogo muito lento
**Solução:** Verifique se há muitos objetos na tela. Reduza `QUANTIDADE_MAXIMA_OBJETOS` em `ConfiguradorJogo`.

### Problema: Colisões não funcionam
**Solução:** A detecção de colisão usa distância euclidiana. Verifique valores de `raio` dos objetos.

### Problema: Janela não abre ou congela
**Solução:** Pressione ESC ou feche a janela. Certifique-se de que Pygame foi instalado corretamente.

---

## Equipe

| Nome | Função | Responsabilidades |
|------|--------|-------------------|
| [Nome do Aluno 1] | Líder + Backend | Arquitetura, classes principais |
| [Nome do Aluno 2] | Frontend | Renderização, HUD, menu |
| [Nome do Aluno 3] | Lógica de Jogo | Colisões, spawn, estados |
| [Nome do Aluno 4] | Testes | Testes unitários, debug |
| [Nome do Aluno 5] | Documentação | Relatório, README, slides |

---

## Referências

- [Documentação Pygame](https://www.pygame.org/docs/)
- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Type Hints in Python](https://www.python.org/dev/peps/pep-0484/)

---

## Licença

Projeto educacional para disciplina de Introdução à Programação do CIN-UFPE

---

## Checklist de Entrega

- [x] Código-fonte funcional
- [x] README.md com instruções
- [x] Arquivo requirements.txt
- [x] Documentação de classes
- [x] 3 tipos de objetos coletáveis
- [x] Sistema de pontuação
- [x] HUD com estatísticas
- [x] Menu e game over
- [x] Controles funcionais
- [x] Código bem estruturado (OOP)

---

**Desenvolvido com ❤️ para a disciplina de Introdução à Programação**

**Data de Entrega:** [Conforme cronograma]  
**Última Atualização:** Dezembro 2025

