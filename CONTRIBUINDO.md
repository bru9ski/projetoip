# 🤝 GUIA DE CONTRIBUIÇÃO

Este guia descreve como contribuir para o desenvolvimento do **Projeto de Coleta** e como o trabalho será dividido entre os membros da equipe.

---

## 📋 Divisão de Trabalho Sugerida

### Para Equipes de 5-6 Pessoas

| Função | Responsável | Tarefas |
|--------|-------------|---------|
| **👨‍💼 Líder de Projeto** | 1 pessoa | - Coordenação geral<br>- Planejamento de sprints<br>- Resolução de conflitos<br>- Atualizações na planilha |
| **🎮 Desenvolvedor(a) Frontend** | 1-2 pessoas | - Renderização gráfica<br>- Menu e interface<br>- HUD e elementos visuais<br>- Efeitos visuais |
| **⚙️ Desenvolvedor(a) Backend** | 1-2 pessoas | - Lógica do jogo<br>- Sistema de colisões<br>- Gerenciamento de objetos<br>- Pontuação |
| **🧪 Responsável de Testes** | 1 pessoa | - Testes unitários<br>- Testes de integração<br>- Relatório de bugs<br>- Validação de features |
| **📚 Responsável de Documentação** | 1 pessoa | - README.md<br>- Relatório final<br>- Slides de apresentação<br>- Comentários no código |

---

## 🔄 Workflow de Desenvolvimento

### Usando Git (Recomendado)

#### 1. Setup Inicial
```bash
# Clonar repositório
git clone [url-do-repositorio]
cd projeto_coleta

# Configurar identidade
git config user.name "Seu Nome"
git config user.email "seu.email@ufpe.br"

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Fluxo de Features (GitFlow Simplificado)

```bash
# 1. Atualizar código principal
git checkout main
git pull origin main

# 2. Criar branch para sua feature
git checkout -b feature/nome-descritivo
# Exemplos:
# - feature/adicionar-inimigos
# - feature/sistema-pontuacao
# - feature/menu-pausar

# 3. Fazer suas mudanças
# ... edite os arquivos ...

# 4. Adicionar e commitar
git add .
git commit -m "Descrição clara da mudança"

# 5. Push para repositório
git push origin feature/nome-descritivo

# 6. Criar Pull Request (no GitHub)
# - Descrever mudanças
# - Solicitar review
# - Aguardar aprovação

# 7. Merge após aprovação
# ... GitHub merge automático ...
```

### Sem Git (Google Drive)

```
projeto_coleta/
├── docs/
│   └── Documentacao_Compartilhada.docx
├── codigo/
│   ├── main_v1_João.py
│   ├── main_v2_Maria.py
│   └── main_final_Merged.py
├── testes/
│   └── test_resultados.md
└── Changelog.md
```

**⚠️ Cuidado:** Sem Git, risco de conflitos. Use nomes descritivos!

---

## 📝 Padrões de Código

### Convenção de Nomenclatura

```python
# ✅ BOM
class Jogador:
    def processar_entrada(self):
        pass

def calcular_distancia(x1, y1, x2, y2):
    pass

# ❌ RUIM
class jogador:
    def processarEntrada(self):
        pass

def calcdist(a, b, c, d):
    pass
```

### Docstrings Obrigatórias

```python
# ✅ BOM
class Jogador:
    """Representa o jogador controlável no jogo."""
    
    def __init__(self, x: float, y: float):
        """
        Inicializa o jogador em uma posição.
        
        Args:
            x: Posição X inicial
            y: Posição Y inicial
        """
        self.x = x
        self.y = y
    
    def mover(self, dx: float, dy: float):
        """
        Move o jogador.
        
        Args:
            dx: Deslocamento em X
            dy: Deslocamento em Y
        """
        self.x += dx
        self.y += dy

# ❌ RUIM
class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
```

### Type Hints

```python
# ✅ OBRIGATÓRIO
from typing import List, Dict, Tuple

def criar_objeto(x: float, y: float) -> ObjetoColetavel:
    """Cria um objeto coletável."""
    pass

def contar_objetos() -> Dict[str, int]:
    """Retorna contagem por tipo."""
    return {'maca': 5, 'ouro': 2}

# ❌ SEM TYPE HINTS
def criar_objeto(x, y):
    pass
```

### Comprimento de Linhas

```python
# ✅ BOM - máximo 100 caracteres
configuracao = {
    'largura': 800,
    'altura': 600,
    'cor_fundo': (30, 30, 30)
}

# ❌ RUIM - linha muito longa
configuracao = {'largura': 800, 'altura': 600, 'cor_fundo': (30, 30, 30), 'cor_texto': (255, 255, 255), 'velocidade_padrao': 5}
```

---

## 🐛 Processo de Bug Reporting

### Template de Bug

```markdown
**Descrição do Bug**
Descreva o problema encontrado de forma clara.

**Passos para Reproduzir**
1. Abrir o jogo
2. Coletar um objeto
3. [Ação adicional]

**Resultado Esperado**
Descreva o que deveria acontecer.

**Resultado Obtido**
Descreva o que realmente aconteceu.

**Ambiente**
- Versão Python: 3.8
- Sistema Operacional: Windows 10
- Versão do Pygame: 2.1.0

**Evidências**
- Screenshot da tela
- Mensagem de erro (se houver)
```

### Exemplo Real

```markdown
**Descrição do Bug**
Objetos desaparecem quando o jogador está no canto da tela.

**Passos para Reproduzir**
1. Ir para canto superior esquerdo
2. Coletar vários objetos
3. Objetos deixam de aparecer

**Resultado Esperado**
Objetos continuam aparecendo normalmente.

**Resultado Obtido**
Nenhum objeto novo aparece após coletar no canto.

**Causa Provável**
Spawn aleatório pode estar fora dos limites da tela.

**Solução Proposta**
Limitar posição do spawn dentro dos limites.
```

---

## 📊 Processo de Code Review

### Checklist de Review

- [ ] Código segue convenções de nomenclatura
- [ ] Docstrings presentes em classes e métodos
- [ ] Type hints utilizados
- [ ] Sem hardcoding (usar ConfiguradorJogo)
- [ ] Não duplica código existente
- [ ] Sem prints de debug deixados
- [ ] Testes escritos se aplicável
- [ ] Não quebra funcionalidades existentes
- [ ] Documentação atualizada

### Exemplo de Review

```python
# ❌ Antes (sem documentação)
class NovaClasse:
    def novo_metodo(self, x):
        return x * 2

# ✅ Depois (com documentação)
class NovaClasse:
    """Classe que implementa cálculos especiais."""
    
    def novo_metodo(self, x: int) -> int:
        """
        Duplica um valor.
        
        Args:
            x: Valor a duplicar
            
        Returns:
            Valor duplicado
        """
        return x * 2
```

---

## 🚀 Adicionando Novas Features

### Exemplo: Adicionar Power-up

#### Passo 1: Criar a Classe
```python
class PowerUp(ObjetoColetavel):
    """Power-up que duplica pontos."""
    
    def __init__(self, x: float, y: float):
        super().__init__(x, y, TipoObjeto.POWERUP, 10, (255, 255, 0), 0)
    
    def aplicar_efeito(self, jogador: Jogador):
        """Ativa efeito do power-up."""
        jogador.multiplicador_pontos = 2
```

#### Passo 2: Adicionar ao Gerenciador
```python
def criar_objeto_aleatorio(self):
    """Cria objeto aleatório."""
    tipos = [Maca, Ouro, Diamante, PowerUp]  # NOVO
    tipo_aleatorio = random.choice(tipos)
    novo_objeto = tipo_aleatorio(x, y)
    self.objetos.append(novo_objeto)
```

#### Passo 3: Aplicar no Jogo
```python
def atualizar_logica(self):
    # ... código anterior ...
    
    for objeto in objetos_para_remover:
        # NOVO
        if isinstance(objeto, PowerUp):
            objeto.aplicar_efeito(self.jogador)
        
        self.gerenciador_objetos.remover_objeto(objeto)
```

#### Passo 4: Testar
```python
def test_powerup():
    jogador = Jogador(400, 300)
    powerup = PowerUp(400, 300)
    
    assert jogador.multiplicador_pontos == 1
    powerup.aplicar_efeito(jogador)
    assert jogador.multiplicador_pontos == 2
```

#### Passo 5: Documentar
```markdown
## Power-up

Adiciona multiplicador 2x à pontuação dos próximos 5 objetos.

**Implementado por:** Maria  
**Data:** 2025-12-10  
**Commit:** abc123def456
```

---

## 📅 Sprints Sugeridas

### Sprint 1 (Semana 1-2): Setup e Estrutura
- [ ] Configurar repositório
- [ ] Criar estrutura base de classes
- [ ] Implementar Jogador com movimento
- [ ] Testes básicos

**Equipe:** Toda  
**Entrega:** Código rodando com Jogador controlável

---

### Sprint 2 (Semana 2-3): Objetos e Colisões
- [ ] Criar classes de objetos (Maca, Ouro, Diamante)
- [ ] Sistema de detecção de colisão
- [ ] Gerenciador de objetos
- [ ] HUD básico

**Equipe:** Backend + Frontend  
**Entrega:** Coleta de objetos funcionando

---

### Sprint 3 (Semana 4): Interface
- [ ] Menu inicial
- [ ] Tela de game over
- [ ] Pausa
- [ ] Sistema de estados

**Equipe:** Frontend  
**Entrega:** Interface completa

---

### Sprint 4 (Semana 5-6): Testes e Documentação
- [ ] Testes unitários completos
- [ ] README e documentação técnica
- [ ] Slides de apresentação
- [ ] Relatório final

**Equipe:** Testes + Documentação  
**Entrega:** Tudo pronto para apresentação

---

## 🎯 Checklist de Entrega

Antes de submeter, verificar:

- [ ] Código executa sem erros
- [ ] Todos os 3 tipos de objetos funcionam
- [ ] Pontuação atualiza corretamente
- [ ] HUD mostra dados atualizados
- [ ] Menu funciona
- [ ] Game over dispara corretamente
- [ ] Testes passam (>80% cobertura)
- [ ] README.md completo
- [ ] Código documentado
- [ ] Sem arquivos desnecessários (.pyc, __pycache__)

---

## 💬 Comunicação

### Canal de Comunicação
- **Diário:** Discord/WhatsApp para dúvidas rápidas
- **Semanal:** Reunião de sincronização (Slack/Zoom)
- **Decisões:** Documentar em Notion

### Reunião Semanal (Suggested)
```
Segundo-feira às 19:00
Duração: 30 minutos

Ordem:
1. Andamento da semana (5 min)
2. Problemas e bloqueadores (10 min)
3. Próximos passos (10 min)
4. Dúvidas técnicas (5 min)
```

---

## 📚 Recursos Úteis

### Documentação
- [Pygame Docs](https://www.pygame.org/docs/)
- [Python OOP](https://docs.python.org/3/tutorial/classes.html)
- [Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)

### Ferramentas
- **IDE:** VS Code, PyCharm Community
- **Git:** GitHub, GitLab
- **Comunicação:** Discord, Slack
- **Documentação:** Notion, Google Docs

---

## 🏆 Boas Práticas

### ✅ DOs
- ✅ Fazer commits frequentes com mensagens claras
- ✅ Revisar código antes de fazer merge
- ✅ Documentar decisões técnicas
- ✅ Testar novo código
- ✅ Comunicar dúvidas no time
- ✅ Ajudar colegas quando possível

### ❌ DON'Ts
- ❌ Fazer commits com código não testado
- ❌ Forçar push sem revisão
- ❌ Esquecer docstrings e comentários
- ❌ Deixar print() de debug no código
- ❌ Criar código não documentado
- ❌ Modificar código de outros sem autorização

---

## ❓ FAQ

**P: Como resolver conflitos de merge?**
R: Usar ferramentas visuais (VS Code) ou mesclar manualmente com cuidado.

**P: Posso trabalhar sem Git?**
R: Sim, use Google Drive com versionamento explícito (v1, v2, etc).

**P: Quanto tempo leva cada feature?**
R: Classe simples: 1-2 horas | Feature complexa: 4-8 horas

**P: Como testo meu código?**
R: Execute `python test_jogo.py` para rodar os testes unitários.

**P: Quem aprova o código?**
R: O Líder do projeto ou Responsável de Testes.

---

## 📞 Suporte

**Dúvida sobre funcionalidade?**
→ Abra uma Issue no GitHub ou mensagem no Discord

**Bug encontrado?**
→ Use o template de Bug Report e atribua a alguém

**Problema com Git?**
→ Consulte o Líder do projeto

---

**Obrigado por contribuir! 🎉**

---

*Última atualização: Dezembro 2025*  
*Versão: 1.0*
