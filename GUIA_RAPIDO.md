# 🚀 GUIA RÁPIDO DE INÍCIO

## ⚡ Setup em 3 Passos

### Passo 1: Instalar Python e pip
```bash
# Verifique se tem Python 3.8+
python --version

# pip já vem com Python
pip --version
```

### Passo 2: Clonar/Baixar o Projeto
```bash
# Se usando Git:
git clone [url-do-repositorio]
cd jogo_coleta

# Se baixar como ZIP, descompacte e entre no diretório
```

### Passo 3: Instalar e Executar
```bash
# Ativar ambiente virtual (opcional mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar o jogo!
python main.py
```

---

## 🎮 Controles Rápidos

```
Movimento:     Setas ou WASD
Pausar:        ESC
Começar/Novo:  ESPAÇO
Sair:          Fechar janela ou ALT+F4
```

---

## 📁 Estrutura de Arquivos

```
projeto/
├── main.py              ← EXECUTAR ESTE ARQUIVO
├── requirements.txt     ← Dependências (pygame)
├── README.md            ← Documentação completa
├── ARQUITETURA.md       ← Design técnico
├── CONTRIBUINDO.md      ← Como contribuir
├── test_jogo.py         ← Testes unitários
└── assets/              ← (Opcional) Imagens e sons
```

---

## ✅ Checklist Rápido

- [ ] Python 3.8+ instalado
- [ ] `pip install pygame` ou `pip install -r requirements.txt`
- [ ] Executar `python main.py`
- [ ] Jogo abre com tela inicial
- [ ] Presionar ESPAÇO para jogar
- [ ] Mover com setas e coletar objetos
- [ ] ESC para pausar

---

## 🎮 Mecânicas do Jogo (Resumo)

| Aspecto | Detalhe |
|--------|---------|
| **Objetivo** | Coletar 50 objetos para vencer |
| **Controle** | Círculo verde que você move |
| **Objetos** | 3 tipos: Maçã (1pt), Ouro (5pts), Diamante (10pts) |
| **Colisão** | Automática ao tocar o objeto |
| **Tela** | 800x600 pixels |
| **FPS** | 60 frames por segundo |

---

## 🐛 Problemas Comuns

| Problema | Solução |
|----------|---------|
| "ModuleNotFoundError: pygame" | Execute: `pip install pygame` |
| Jogo muito lento | Reduza `QUANTIDADE_MAXIMA_OBJETOS` em `main.py` |
| Colisões não funcionam | Verifique se há objetos na tela (espere 2 segundos) |
| Janela não abre | Tente novamente, pode ser primeira inicialização |

---

## 📚 Arquivos de Documentação

### Para Estudar OOP
→ Leia **ARQUITETURA.md** e veja exemplos em `main.py`

### Para Implementar Novas Features
→ Leia **CONTRIBUINDO.md** e **ARQUITETURA.md**

### Para Entender Tudo
→ Comece com **README.md** depois **ARQUITETURA.md**

---

## 🎓 Conceitos de OOP no Projeto

```python
# 1. CLASSES
class Jogador:           # Encapsula dados e comportamento
    def __init__(self):
        self.x = 0       # Atributo (dados)
    def mover(self):     # Método (comportamento)
        pass

# 2. HERANÇA
class Maca(ObjetoColetavel):  # Maca herda de ObjetoColetavel
    def __init__(self, x, y):
        super().__init__(...)  # Chama construtor da classe pai

# 3. POLIMORFISMO
jogador.desenhar()       # Jogador tem seu desenhar()
objeto.desenhar()        # ObjetoColetavel tem seu desenhar()
# Mesmo nome, comportamento diferente!

# 4. ENCAPSULAMENTO
self.x = 400             # Dado privado da classe
self.obter_posicao()     # Método para acessar

# 5. COMPOSIÇÃO
class Jogo:
    self.jogador = Jogador()      # Jogo CONTÉM um Jogador
    self.objetos = GerenciadorObjetos()  # Jogo CONTÉM um Gerenciador
```

---

## 🔧 Personalizações Fáceis

### Mudar Cores
```python
# Em ConfiguradorJogo:
COR_JOGADOR = (0, 255, 0)  # RGB verde
COR_MACA = (255, 0, 0)      # RGB vermelho
COR_OURO = (255, 215, 0)    # RGB dourado
```

### Mudar Velocidade
```python
# Em ConfiguradorJogo:
VELOCIDADE_JOGADOR = 5  # Aumentar para 10 fica mais rápido
```

### Mudar Tamanho da Tela
```python
# Em ConfiguradorJogo:
LARGURA_TELA = 1024   # De 800 para 1024
ALTURA_TELA = 768     # De 600 para 768
```

### Mudar Objetivo (Quantidade de Objetos)
```python
# Em Jogo.atualizar_logica():
if total_coletados >= 100:  # De 50 para 100
    self.estado = "gameover"
```

---

## 📊 Estatísticas do Código

| Métrica | Valor |
|---------|-------|
| Linhas de Código | ~800 |
| Classes | 8 (2 base + 3 subclasses + 3 principais) |
| Métodos | ~30 |
| Documentação | 100% |
| Tipo Hints | Sim |

---

## 🎯 Próximos Passos

### Nível 1: Entender
1. Ler `README.md`
2. Executar `main.py`
3. Jogar e entender mecânicas

### Nível 2: Estudar Código
1. Ler `ARQUITETURA.md`
2. Analisar cada classe em `main.py`
3. Entender herança em `Maca`, `Ouro`, `Diamante`

### Nível 3: Modificar
1. Mudar cores em `ConfiguradorJogo`
2. Adicionar novo tipo de objeto (copiar `Maca`)
3. Mudar velocidade ou tamanho

### Nível 4: Expandir
1. Ler `CONTRIBUINDO.md`
2. Adicionar power-ups ou inimigos
3. Implementar sistema de níveis

---

## 💡 Dicas de Desenvolvimento

### 1. Use Breakpoints
```python
# Adicione em qualquer lugar para pausar execução
import pdb; pdb.set_trace()
```

### 2. Print para Debug
```python
print(f"Posição do jogador: ({self.jogador.x}, {self.jogador.y})")
print(f"Objetos na tela: {len(self.gerenciador_objetos.obter_objetos())}")
```

### 3. Teste a Colisão Manualmente
```python
# Mude a posição de um objeto para a posição do jogador
objeto = Maca(400, 300)  # Mesmo que jogador
resultado = jogador.detectar_colisao(objeto)
print(resultado)  # Deve ser True
```

### 4. Versionamento com Git
```bash
git add .
git commit -m "Adicionar novo tipo de objeto"
git push origin main
```

---

## 🚀 Deployment (Compartilhar)

### Opção 1: GitHub
```bash
git init
git add .
git commit -m "Projeto inicial"
git remote add origin [seu-repo-url]
git push -u origin main
```

### Opção 2: Google Drive
1. Compacte a pasta: `projeto_coleta.zip`
2. Envie para Google Drive
3. Compartilhe o link

### Opção 3: Executável (Windows)
```bash
pip install pyinstaller
pyinstaller --onefile main.py
# Arquivo .exe criado em `dist/`
```

---

## 📞 Suporte

### Dúvidas sobre Pygame
→ https://www.pygame.org/docs/

### Dúvidas sobre Python OOP
→ https://docs.python.org/3/tutorial/classes.html

### Dúvidas sobre o Projeto
→ Verifique `ARQUITETURA.md` e comente no código

---

## ✨ Features Implementadas

✅ Menu inicial
✅ 3 tipos de objetos coletáveis
✅ Sistema de pontuação
✅ HUD (interface na tela)
✅ Pausa
✅ Game Over
✅ Colisões precisas
✅ Spawn aleatório
✅ Limite de FPS
✅ Documentação completa

---

## 🎉 Você está Pronto!

Agora é só **executar `python main.py`** e começar a jogar!

Para dúvidas técnicas, consulte os arquivos de documentação. 

**Divirta-se! 🎮🚀**

---

**Última atualização:** Dezembro 2025  
**Versão:** 1.0  
**Status:** Pronto para Produção ✅
