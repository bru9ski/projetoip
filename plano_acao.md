# 📋 PLANO DE AÇÃO - Projeto de Introdução à Programação

**Disciplina:** Introdução à Programação  
**Tema:** Sistema Interativo 2D de Coleta de Objetos  
**Data de Entrega:** Conforme cronograma da disciplina

---

## 🎯 Objetivo Geral

Desenvolver um sistema interativo em ambiente 2D usando Python e Orientação a Objetos, onde o usuário controla um objeto para coletar outros objetos dispostos na tela, mantendo registro de coletas por tipo.

---

## 📊 Fase 1: Planejamento & Setup (Semana 1)

### 1.1 Organização da Equipe
- [ ] Definir membros do grupo (5-6 pessoas)
- [ ] Atribuir papéis: Líder, Desenvolvedor(a) Frontend, Backend, Testes, Documentação
- [ ] Criar canal de comunicação (WhatsApp/Discord)
- [ ] Criar workspace no Notion para gerenciamento de conhecimento
- [ ] Configurar repositório GitHub com GitFlow
- [ ] Criar projeto no GitHub Projects com colunas: Backlog → Sprint → ToDo → Doing → Done

### 1.2 Pesquisa Técnica
- [ ] Avaliar bibliotecas: **Pygame** (recomendado), Arcade, Pyglet
- [ ] Pesquisar estrutura de projetos Python profissionais
- [ ] Estudar OOP (Classes, Herança, Polimorfismo, Encapsulamento)
- [ ] Criar documento com decisões arquiteturais
- [ ] Documenta justificativa da biblioteca escolhida

### 1.3 Requisitos & Escopo
- [ ] Definir tema/história do jogo (ex: Jardineiro coletando frutas, Astronauta coletando minerais)
- [ ] Listar 3 tipos de objetos coletáveis diferentes
- [ ] Descrever requisitos mínimos confirmados
- [ ] Planejar features extras (fases, power-ups, inimigos, etc.)
- [ ] Esboçar wireframes/mockups do interface

**Entrega da Fase 1:**
- Preenchimento da planilha "Equipes" com informações do grupo
- Documento de arquitetura inicial
- Repositório GitHub criado e compartilhado

---

## 🏗️ Fase 2: Implementação Base (Semanas 2-4)

### 2.1 Estrutura OOP - Núcleo do Sistema
- [ ] Criar classe `Jogador` (posição, movimento, velocidade, coleta)
- [ ] Criar classe base `ObjetoColetavel` (posição, tipo, aparência)
- [ ] Criar 3 subclasses distintas de `ObjetoColetavel`:
  - Tipo A (ex: Maçã - comum, 1 ponto)
  - Tipo B (ex: Ouro - raro, 5 pontos)
  - Tipo C (ex: Diamante - muito raro, 10 pontos)
- [ ] Criar classe `Jogo` (controla fluxo, lógica, estado)
- [ ] Criar classe `Renderizador` ou integrar Pygame (desenha sprites/objetos)
- [ ] Criar classe `Colisao` (detecta e processa colisões)

### 2.2 Mecânicas Principais
- [ ] Sistema de entrada (setas ou WASD para movimento)
- [ ] Física básica (movimento suave, limites de tela)
- [ ] Detecção de colisão entre jogador e objetos
- [ ] Sistema de contagem por tipo (dicionário ou variáveis)
- [ ] HUD mostrando quantidade coletada de cada tipo
- [ ] Spawn aleatório de objetos na tela
- [ ] Loop principal do jogo (atualizar, desenhar, detectar eventos)

### 2.3 Testes Unitários & Debug
- [ ] Testar colisões em diferentes posições
- [ ] Verificar movimento do jogador
- [ ] Validar contagem de objetos
- [ ] Documentar bugs encontrados em Issues do GitHub
- [ ] Criar testes automáticos (unittest)

**Checkpoint 1 (Final da Semana 2):**
- Atualizar planilha "Checkpoints" com progresso
- Demonstrar requisitos mínimos funcionando
- Resolver dificuldades encontradas

**Checkpoint 2 (Final da Semana 4):**
- Todas as mecânicas base implementadas
- Sistema de OOP completo e funcional
- Código documentado e testado

---

## ✨ Fase 3: Polimento & Features Extras (Semanas 5-6)

### 3.1 Melhorias de UX/Interface
- [ ] Menu inicial (botão "Jogar", "Instruções", "Sair")
- [ ] Tela de game over com placar final
- [ ] Pausa do jogo (tecla ESC)
- [ ] Interface visual clara (fontes, cores, disposição)
- [ ] Instruções na tela ou em tela de ajuda
- [ ] Feedback visual (animações de coleta, feedback de pontos)

### 3.2 Melhorias Visuais & Áudio
- [ ] Sprites ou desenhos geométricos melhorados
- [ ] Cores distintas para cada tipo de objeto
- [ ] Fundo com tema visual consistente
- [ ] Som de coleta (opcional mas recomendado)
- [ ] Som de background (opcional)

### 3.3 Features Adicionais (Não-Obrigatórias - se tempo permitir)
- [ ] Sistema de dificuldade progressiva (mais objetos a cada nível)
- [ ] Fases/Níveis (ex: 3 níveis com objetivos diferentes)
- [ ] Inimigos/Obstáculos que reduzem pontuação
- [ ] Power-ups especiais (dobro de pontos, escudo, etc.)
- [ ] Placar de high-score (salvar em arquivo)
- [ ] Efeitos visuais adicionais (partículas, animações)

**Checkpoint 3 (Final da Semana 6):**
- Apresentação funcional completa
- Todas as features planejadas implementadas
- Código refatorado e otimizado

---

## 📚 Fase 4: Documentação & Relatório (Semana 6-7)

### 4.1 Captura de Evidências
- [ ] Capturar 5-7 screenshots do jogo em funcionamento
- [ ] Registrar diferentes estados (menu, gameplay, game over)
- [ ] Criar GIF ou vídeo curto do gameplay (opcional)

### 4.2 Desenvolvimento do Relatório
Deve conter obrigatoriamente:

1. **Capa e Informações Básicas**
   - [ ] Título do projeto
   - [ ] Nomes e matrículas dos membros
   - [ ] Data de entrega
   - [ ] Instituição e disciplina

2. **Descrição e Contexto**
   - [ ] Breve descrição do projeto
   - [ ] Objetivos alcançados

3. **Arquitetura do Projeto**
   - [ ] Diagrama de classes UML ou texto descritivo
   - [ ] Explicação de como o código está organizado
   - [ ] Descrição de cada classe principal
   - [ ] Fluxo de execução (como o programa funciona)

4. **Tecnologias Utilizadas**
   - [ ] Biblioteca Pygame (ou outra): versão, funcionalidades usadas
   - [ ] Python: versão
   - [ ] Outras bibliotecas (random, math, etc.)
   - [ ] **Justificativa de cada escolha técnica**

5. **Divisão de Trabalho**
   - [ ] Tabela ou lista indicando quem foi responsável por:
     - Arquitetura/Design
     - Classe Jogador
     - Classes de Objetos
     - Sistema de Colisão
     - Interface/Menu
     - Testes
     - Documentação

6. **Conceitos de OOP Utilizados**
   - [ ] Classes e Objetos (exemplos)
   - [ ] Herança (qual classe herda de qual?)
   - [ ] Polimorfismo (se usado)
   - [ ] Encapsulamento (atributos privados/públicos)
   - [ ] Composição (se usado)
   - [ ] **Indicar em qual parte do código cada conceito foi aplicado**

7. **Galeria de Screenshots**
   - [ ] Menu inicial
   - [ ] Gameplay principal
   - [ ] Interface com placar
   - [ ] Tela de game over
   - [ ] Features extras (se houver)

8. **Desafios, Erros e Lições Aprendidas**
   - [ ] **Qual foi o maior erro cometido durante o projeto?**
     - Como vocês lidaram com ele?
   - [ ] **Qual foi o maior desafio enfrentado?**
     - Como vocês lidaram com ele?
   - [ ] **Quais as lições aprendidas durante o projeto?**
   - [ ] O que faria diferente em um próximo projeto?
   - [ ] Dicas para futuras equipes

9. **Conclusão**
   - [ ] Resumo dos resultados
   - [ ] Satisfação com o projeto
   - [ ] Próximos passos ou melhorias futuras

10. **Apêndices (Opcional)**
    - [ ] Instruções detalhadas de instalação
    - [ ] Guia do usuário
    - [ ] Código-fonte relevante (trechos importantes)

---

## 🎬 Fase 5: Apresentação (Última Semana)

### 5.1 Desenvolvimento dos Slides
- [ ] Utilizar template fornecido (Google Slides ou equivalente)
- [ ] Manter consistência visual (cores, fontes, espaçamento)
- [ ] Seguir estrutura do relatório de forma sucinta

**Estrutura sugerida dos slides:**
1. Slide 1: Capa (Título, nomes, data)
2. Slide 2: Introdução (O que é o projeto?)
3. Slide 3: Objetivos (O que foi alcançado?)
4. Slide 4-5: Arquitetura (Diagrama de classes, estrutura)
5. Slide 6: Tecnologias (Bibliotecas e justificativas)
6. Slide 7: Demo ao Vivo (Executar o jogo)
7. Slide 8-9: Desafios e Lições (Pontos principais)
8. Slide 10: Conclusão (Resultados finais)
9. Slide 11: Perguntas?

### 5.2 Preparação da Demonstração
- [ ] Testar execução do jogo completamente
- [ ] Preparar dados/assets para demo (screenshots, vídeo backup)
- [ ] Ensaiar a apresentação em grupo (mínimo 3x)
- [ ] Distribuir partes: quem fala de quê
- [ ] Cronometrar: máximo 8 minutos
- [ ] Preparar resposta para possíveis perguntas

### 5.3 Checklist Antes da Apresentação
- [ ] Todos os membros do grupo sabem o que vai ser apresentado
- [ ] Código está funcional e foi testado
- [ ] Slides estão prontos e compartilhados
- [ ] Áudio/vídeo (se necessário) testado
- [ ] Plano B: vídeo da execução em caso de problema

---

## 📦 Fase 6: Entrega Final

### 6.1 Preparação do Repositório
- [ ] Código-fonte completo e organizado em pastas:
  ```
  projeto_nome/
  ├── src/
  │   ├── main.py
  │   ├── jogador.py
  │   ├── objeto_coletavel.py
  │   ├── jogo.py
  │   └── utils.py
  ├── assets/
  │   ├── sprites/
  │   ├── sounds/
  │   └── images/
  ├── tests/
  │   └── test_*.py
  ├── README.md
  ├── requirements.txt
  └── .gitignore
  ```
- [ ] **README.md com:**
  - Descrição do projeto
  - Instruções de instalação (pip install -r requirements.txt)
  - Como executar (python src/main.py)
  - Controles do jogo
  - Capturas de tela
  - Informações dos autores
- [ ] Arquivo `requirements.txt` com dependências
- [ ] `.gitignore` configurado
- [ ] Histórico de commits limpo e descritivo

### 6.2 Documentação Final
- [ ] Relatório em PDF ou README.md completo
- [ ] Todas as seções do relatório preenchidas
- [ ] Screenshots inclusos
- [ ] Formatação profissional

### 6.3 Slides da Apresentação
- [ ] Compartilhados em Google Drive ou equivalente
- [ ] Acesso para leitura para os professores
- [ ] Versão de backup em PDF

### 6.4 Preenchimento da Planilha de Entrega
- [ ] **Link do repositório** (GitHub ou Google Drive)
- [ ] **Link do relatório** (PDF ou README.md)
- [ ] **Link dos slides** (Google Slides ou equivalente)
- [ ] **Data de entrega:** Verificar cronograma
- [ ] ⚠️ **ATENÇÃO:** Após deadline, edição desabilitada!

---

## 🎓 Critérios de Avaliação

O projeto será avaliado em:

1. **Processo de Desenvolvimento (25%)**
   - Checkpoints preenchidos na planilha
   - Evolução visível do projeto
   - Participação ativa de todos os membros
   - Uso adequado de versionamento (Git)

2. **Funcionamento & Qualidade do Software (35%)**
   - Requisitos mínimos implementados ✓
   - Código bem estruturado (OOP)
   - Sem bugs críticos
   - Testes implementados
   - Tratamento de erros

3. **Qualidade do Relatório (20%)**
   - Completo e bem organizado
   - Arquitetura clara
   - Justificativas técnicas
   - Divisão de trabalho documentada
   - Conceitos de OOP identificados

4. **Qualidade da Apresentação (20%)**
   - Clareza e objetividade
   - Tempo adequado (≤ 8 minutos)
   - Demonstração ao vivo funcionando
   - Participação de todos os membros
   - Respostas às perguntas

---

## ⚠️ Dicas Importantes

### Comece pelos Requisitos Mínimos ✓
- Implementar 100% dos requisitos antes de adicionar features extras
- Com mínimo garantido, AÍ SIM adicione features legais
- Qualidade > Quantidade

### Gerenciamento do Projeto
- **Comunicação:** Use Discord/WhatsApp para dúvidas rápidas
- **Documentação:** Notion com: decisões, problemas, soluções
- **Tarefas:** GitHub Projects com sprint semanal
- **Código:** GitHub com branch por feature, pull requests obrigatórios

### Boas Práticas de Desenvolvimento
```python
# ✓ BOM: Código organizado em classes
class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

# ✗ RUIM: Tudo em uma função gigante
def jogar():
    x, y = 400, 300
    # 500 linhas de código...
```

### Divisão Eficiente do Trabalho
- Não deixe para última hora
- Trabalhe em paralelo em diferentes módulos
- Use branches do Git para evitar conflitos
- Faça merge regularmente
- Teste sempre antes de fazer merge

---

## 📅 Cronograma Sugerido

| Semana | Fase | Deadline |
|--------|------|----------|
| 1 | Planejamento & Setup | Preench planilha "Equipes" |
| 2 | Implementação Base (Parte 1) | **Checkpoint 1** |
| 3 | Implementação Base (Parte 2) | - |
| 4 | Implementação Base (Parte 3) | **Checkpoint 2** |
| 5 | Polimento & Features Extras | **Checkpoint 3** |
| 6 | Documentação & Relatório | Relatório pronto |
| 7 | Apresentação | **ENTREGA FINAL** |

---

## 📞 Recursos e Referências

### Documentação Oficial
- **Pygame:** https://www.pygame.org/docs/
- **Python OOP:** https://docs.python.org/3/tutorial/classes.html
- **Git:** https://git-scm.com/doc

### Ferramentas Recomendadas
- **IDE:** VS Code, PyCharm, Thonny
- **Versionamento:** GitHub, GitLab
- **Gerenciamento:** Notion, Trello
- **Comunicação:** Discord, Slack

### Exemplos de Projetos Anteriores
- Verifique a galeria disponibilizada pela disciplina
- Analise estrutura e qualidade dos projetos

---

**Boa sorte! 🎮🚀**

Lembre-se: Comunicação, organização e qualidade fazem a diferença!
