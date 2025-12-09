# 📐 GUIA DE ARQUITETURA - Projeto de Coleta

## Visão Geral da Arquitetura

O projeto segue um modelo de **arquitetura em camadas**, onde cada componente tem uma responsabilidade bem definida:

```
┌──────────────────────────────────────────────┐
│         CAMADA DE APRESENTAÇÃO               │
│  (Renderização, Interface, Eventos)          │
└──────────────────────────────────────────────┘
              ↓           ↓           ↓
┌──────────────┬──────────────┬──────────────┐
│   Jogo       │  Renderiz.   │  Eventos     │
│   (Loop)     │  (Draw)      │  (Input)     │
└──────────────┴──────────────┴──────────────┘
              ↓           ↓           ↓
┌──────────────────────────────────────────────┐
│         CAMADA DE LÓGICA DE NEGÓCIO         │
│  (Colisões, Coleta, Pontuação)              │
└──────────────────────────────────────────────┘
              ↓           ↓           ↓
┌──────────────┬──────────────┬──────────────┐
│   Jogador    │   Objetos    │  Gerenciador │
│              │              │              │
└──────────────┴──────────────┴──────────────┘
              ↓           ↓           ↓
┌──────────────────────────────────────────────┐
│         CAMADA DE DADOS / CONFIG             │
│  (Constantes, Enums, Estruturas)            │
└──────────────────────────────────────────────┘
```

---

## Padrões de Projeto Utilizados

### 1. **Padrão Singleton (Implícito)**
**Classe:** `ConfiguradorJogo`
```python
class ConfiguradorJogo:
    # Todas as variáveis são estáticas (de classe)
    LARGURA_TELA = 800
    ALTURA_TELA = 600
    # ...
```
**Benefício:** Centraliza todas as constantes em um único lugar, facilitando manutenção.

### 2. **Padrão Factory (Implícito)**
**Método:** `GerenciadorObjetos.criar_objeto_aleatorio()`
```python
def criar_objeto_aleatorio(self):
    """Cria um dos 3 tipos de forma aleatória"""
    tipo_aleatorio = random.choice([Maca, Ouro, Diamante])
    novo_objeto = tipo_aleatorio(x, y)
```
**Benefício:** Abstrai a criação de diferentes tipos de objetos.

### 3. **Padrão Template Method (Herança)**
**Classes:** `ObjetoColetavel` (base), `Maca`, `Ouro`, `Diamante` (subclasses)
```python
class ObjetoColetavel:
    def __init__(self, x, y, tipo, raio, cor, pontos):
        self.x = x
        # ... inicialização comum

class Maca(ObjetoColetavel):
    def __init__(self, x, y):
        super().__init__(x, y, TipoObjeto.MACA, 12, (255, 0, 0), 1)
        # especialização específica
```
**Benefício:** Reutiliza código comum enquanto permite especialização.

### 4. **Padrão Observer (Implícito)**
**Conceito:** O `Jogo` observa eventos do Pygame e reage
```python
def processar_eventos(self):
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            # Reage ao evento
```
**Benefício:** Desacoplamento entre entrada e lógica.

---

## Fluxo de Execução

### Sequência Principal

```
1. __main__
   └── Jogo()  # Instancia o jogo
       └── __init__()
           ├── pygame.init()
           ├── criar janela
           └── inicializar_novo_jogo()

2. jogo.executar()  # Loop principal
   ├── while rodando:
   │   ├── processar_eventos()
   │   │   ├── ler entrada do teclado
   │   │   └── atualizar estado (menu/pausa/jogo)
   │   │
   │   ├── atualizar_logica()
   │   │   ├── jogador.processar_entrada()
   │   │   ├── gerenciador_objetos.atualizar()
   │   │   ├── detectar colisões
   │   │   └── verificar game over
   │   │
   │   ├── renderizar()
   │   │   ├── limpar tela
   │   │   ├── desenhar objetos
   │   │   ├── desenhar jogador
   │   │   └── atualizar display
   │   │
   │   └── relogio.tick(60)  # 60 FPS
   │
   └── pygame.quit()
```

### Fluxo de Colisão

```
jogador.position = (400, 300)
objetos = [objeto1, objeto2, objeto3, ...]

Para cada objeto:
  ├── calcular distância euclidiana
  ├── if distância < (raio_jogador + raio_objeto):
  │   ├── jogador.coletar_objeto(objeto)
  │   │   ├── atualizar contadores[tipo]
  │   │   └── adicionar pontos
  │   └── gerenciador.remover_objeto(objeto)
  └── continuar próximo objeto
```

### Fluxo de Spawn

```
contador_spawn += 1

if contador_spawn >= INTERVALO_SPAWN:
  if len(objetos) < QUANTIDADE_MAXIMA:
    ├── x_aleatorio = random(30, LARGURA - 30)
    ├── y_aleatorio = random(30, ALTURA - 30)
    ├── tipo_aleatorio = random([Maca, Ouro, Diamante])
    ├── novo_objeto = tipo_aleatorio(x, y)
    ├── objetos.append(novo_objeto)
    └── contador_spawn = 0
```

---

## Responsabilidades das Classes

### `ConfiguradorJogo`
```
├── Dimensões
│   ├── LARGURA_TELA
│   └── ALTURA_TELA
├── Cores (RGB)
│   ├── COR_FUNDO
│   ├── COR_JOGADOR
│   └── COR_[TIPO]
├── Tamanhos
│   ├── TAMANHO_JOGADOR
│   └── TAMANHO_[TIPO]
└── Parâmetros
    ├── VELOCIDADE_JOGADOR
    └── FPS
```
**Princípio:** Single Responsibility - centraliza configuração

---

### `Jogador`
```
├── Estado
│   ├── x, y (posição)
│   ├── velocidade
│   └── raio
├── Dados
│   ├── coletados (dict tipo → quantidade)
│   └── pontuacao
└── Comportamento
    ├── processar_entrada()
    ├── detectar_colisao()
    ├── coletar_objeto()
    └── desenhar()
```
**Princípio:** Encapsulamento - dados + operações relacionadas

---

### `ObjetoColetavel` (Base)
```
├── Estado
│   ├── x, y (posição)
│   ├── tipo
│   ├── raio
│   ├── cor
│   └── pontos
└── Comportamento
    ├── desenhar()
    └── obter_info()
```
**Princípio:** Herança - template para subclasses

---

### `Maca`, `Ouro`, `Diamante` (Subclasses)
```
Herdam de ObjetoColetavel:
├── __init__() com valores específicos
│   ├── raio (12, 15, 18)
│   ├── cor específica
│   └── pontos (1, 5, 10)
```
**Princípio:** Herança + Polimorfismo

---

### `GerenciadorObjetos`
```
├── Estado
│   ├── objetos[] (lista)
│   └── contador_spawn
└── Comportamento
    ├── atualizar()          # Spawn automático
    ├── criar_objeto_aleatorio()
    ├── remover_objeto()
    ├── obter_objetos()
    ├── desenhar()
    └── limpar()
```
**Princípio:** Separação de conceitos - gerencia ciclo de vida dos objetos

---

### `Jogo` (Orquestrador)
```
├── Componentes
│   ├── jogador (Jogador)
│   ├── gerenciador_objetos (GerenciadorObjetos)
│   └── tela (pygame)
├── Estado
│   └── estado ("menu", "jogando", "pausado", "gameover")
└── Comportamento
    ├── processar_eventos()
    ├── atualizar_logica()
    ├── renderizar()
    └── executar()
```
**Princípio:** Composição - coordena outros objetos

---

## Padrão MVC (Model-View-Controller)

Embora não seja um MVC puro, o projeto segue princípios similares:

| Componente | Padrão | Classes |
|-----------|--------|---------|
| **Model** | Dados + Lógica | `Jogador`, `ObjetoColetavel`, `GerenciadorObjetos` |
| **View** | Renderização | Métodos `desenhar()`, `renderizar*()` |
| **Controller** | Entrada + Orquestração | `Jogo.processar_eventos()`, `Jogo.executar()` |

---

## Comunicação Entre Classes

### Fluxo de Dados

```
┌─────────────────────────────────────────────┐
│         ENTRADA: pygame.event               │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Jogo.processar_eventos()                   │
│  - Lê eventos                               │
│  - Atualiza estado                          │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Jogo.atualizar_logica()                    │
│  - Chama Jogador.processar_entrada()        │
│  - Chama GerenciadorObjetos.atualizar()     │
│  - Detecta colisões Jogador ↔ Objetos      │
│  - Chama Jogador.coletar_objeto()           │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Jogo.renderizar()                          │
│  - Limpa tela                               │
│  - Chama Jogador.desenhar()                 │
│  - Chama GerenciadorObjetos.desenhar()      │
│  - Atualiza display (pygame)                │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│         SAÍDA: tela renderizada             │
└─────────────────────────────────────────────┘
```

### Dependências Entre Classes

```
Jogo
├── usa → Jogador
│   └── usa → TipoObjeto (enum)
├── usa → GerenciadorObjetos
│   └── usa → Maca, Ouro, Diamante
│       └── herdam de ObjetoColetavel
│           └── usa → TipoObjeto (enum)
├── usa → ConfiguradorJogo
│   └── estático
└── usa → pygame (biblioteca externa)
```

**Observação:** Acoplamento mínimo, alta coesão.

---

## Pontos de Extensão (Novas Features)

### 1. Adicionar Novo Tipo de Objeto

```python
# 1. Criar nova classe
class Cristal(ObjetoColetavel):
    def __init__(self, x, y):
        super().__init__(x, y, TipoObjeto.CRISTAL, 16, (200, 100, 255), 7)

# 2. Adicionar enum
class TipoObjeto(Enum):
    MACA = 1
    OURO = 2
    DIAMANTE = 3
    CRISTAL = 4  # NOVO

# 3. Atualizar factory
def criar_objeto_aleatorio(self):
    tipo_aleatorio = random.choice([Maca, Ouro, Diamante, Cristal])  # NOVO

# 4. Inicializar contador no Jogador
self.coletados = {
    TipoObjeto.MACA: 0,
    TipoObjeto.OURO: 0,
    TipoObjeto.DIAMANTE: 0,
    TipoObjeto.CRISTAL: 0  # NOVO
}
```

### 2. Adicionar Power-up

```python
class PowerUp(ObjetoColetavel):
    """Tipo especial de objeto com efeito"""
    
    def __init__(self, x, y):
        super().__init__(x, y, TipoObjeto.POWERUP, 10, (255, 255, 0), 0)
    
    def aplicar_efeito(self, jogador):
        """Duplica pontos do próximo objeto por 5 segundos"""
        jogador.multiplicador_pontos = 2
        jogador.tempo_powerup = 300  # 5 segundos a 60 FPS
```

### 3. Adicionar Obstáculo

```python
class Obstaculo(ObjetoColetavel):
    """Objeto que reduz pontuação"""
    
    def __init__(self, x, y):
        super().__init__(x, y, TipoObjeto.OBSTACULO, 15, (100, 100, 100), -5)

# Em Jogo.atualizar_logica():
if jogador.detectar_colisao(obstaculo):
    jogador.pontuacao += obstaculo.pontos  # Subtrai pontos
```

### 4. Adicionar Sistema de Níveis

```python
class Fase:
    def __init__(self, numero, tempo_limite, quantidade_objetivo):
        self.numero = numero
        self.tempo_limite = tempo_limite
        self.quantidade_objetivo = quantidade_objetivo

# Em Jogo:
self.fase_atual = 1
self.tempo_decorrido = 0

def proximo_nivel():
    self.fase_atual += 1
    self.tempo_decorrido = 0
```

---

## Boas Práticas Implementadas

| Prática | Aplicação |
|---------|-----------|
| **DRY** (Don't Repeat Yourself) | Herança reduz duplicação de código |
| **SOLID** | Responsabilidade única por classe |
| **Encapsulamento** | Dados protegidos dentro de classes |
| **Type Hints** | Documentação e validação de tipos |
| **Docstrings** | Documentação em formato Python |
| **Nomes Descritivos** | Classes, métodos e variáveis claras |
| **Separação de Conceitos** | Config, Model, View separados |

---

## Problemas Comuns e Soluções

### Problema 1: Muitos Objetos na Tela
**Sintoma:** Jogo fica lento
**Solução:** Reduzir `QUANTIDADE_MAXIMA_OBJETOS` ou aumentar `INTERVALO_SPAWN`

### Problema 2: Colisões Imprecisas
**Sintoma:** Objeto não coleta mesmo próximo
**Solução:** Verificar valores de `raio` das classes

### Problema 3: Código Duplicado Entre Tipos
**Sintoma:** `Maca`, `Ouro`, `Diamante` muito similares
**Solução:** Usar configuração em dicionário
```python
TIPOS_OBJETO = {
    TipoObjeto.MACA: {'raio': 12, 'cor': (255, 0, 0), 'pontos': 1},
    TipoObjeto.OURO: {'raio': 15, 'cor': (255, 215, 0), 'pontos': 5},
    ...
}
```

---

## Métricas de Qualidade

| Métrica | Alvo | Status |
|---------|------|--------|
| **Coesão** | Alta | ✓ Cada classe tem um propósito claro |
| **Acoplamento** | Baixo | ✓ Poucas dependências entre classes |
| **Complexidade Ciclomática** | Baixa | ✓ Métodos simples e diretos |
| **Cobertura de Testes** | > 80% | ✓ Testes para funcionalidades principais |
| **Documentação** | Completa | ✓ Docstrings e comments |

---

## Conclusão

A arquitetura segue princípios sólidos de OOP, permitindo:

✅ **Extensibilidade:** Fácil adicionar novos tipos de objetos
✅ **Manutenibilidade:** Código organizado e documentado
✅ **Testabilidade:** Componentes isolados e testáveis
✅ **Reusabilidade:** Herança reduz duplicação

Perfeito como base educacional para aprender OOP em Python!

