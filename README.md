🎮 Jogo 2D em Pygame
===================

Nome do jogo: (coloque aqui)
Disciplina: (coloque aqui)


👥 Membros da Equipe
-------------------
- Nome 1 – Estrutura geral do jogo e menus
- Nome 2 – Jogador, tiros e power-ups
- Nome 3 – Inimigos e colisões
- Nome 4 – HUD, sons e música dinâmica


📖 Descrição Geral do Projeto
----------------------------
Este projeto consiste no desenvolvimento de um jogo 2D utilizando a biblioteca Pygame.
O jogador controla um personagem que deve sobreviver o maior tempo possível, enfrentando
inimigos, coletando itens e gerenciando recursos como vidas, tempo e power-ups.

O jogo possui menu inicial, menu de pausa, tela de game over, sistema de tempo,
efeitos sonoros, música dinâmica e dificuldade progressiva.


🏗️ Arquitetura do Projeto
-------------------------
O projeto foi desenvolvido de forma modular, separando as responsabilidades em
diferentes arquivos dentro da pasta source/, facilitando a organização e manutenção
do código.

Estrutura do projeto:

source/
- config.py        → Constantes globais (cores, FPS, resolução)
- jogador.py       → Classe Jogador (movimento, tiros, vidas e power-ups)
- inimigos.py      → Classe Inimigo (movimentação e comportamento)
- coletaveis.py    → Geração e lógica dos itens coletáveis
- cenario.py       → Atualização e desenho do cenário
- hud.py           → Interface gráfica (vidas, tempo, café)
- menu.py          → Menu inicial e menu de game over
- pausa.py         → Menu de pausa
- main.py          → Loop principal e controle do jogo

A classe Jogo, localizada no arquivo main.py, é responsável por inicializar o sistema,
controlar o loop principal, gerenciar os estados do jogo e integrar todos os módulos.


🖼️ Galeria do Projeto
--------------------
Adicionar capturas de tela do jogo em funcionamento, como:
- Menu inicial
- Tela de gameplay
- Tela de game over


🛠️ Ferramentas e Tecnologias
-----------------------------
- Python 3 – Linguagem principal do projeto
- Pygame – Desenvolvimento do jogo 2D
- VS Code – Editor de código
- Git/GitHub – Versionamento e colaboração


👨‍💻 Divisão de Trabalho do Grupo
--------------------------------
- Integrante 1: Loop principal, controle de estados e menus
- Integrante 2: Jogador, tiros e sistema de power-ups
- Integrante 3: Inimigos, colisões e balanceamento
- Integrante 4: HUD, efeitos sonoros e música dinâmica


📚 Conceitos da Disciplina Utilizados
------------------------------------
- Programação Orientada a Objetos (uso de classes)
- Máquina de estados (menu, jogo, pausa e game over)
- Eventos e laço de repetição
- Modularização do código
- Tratamento de exceções (try/except)


⚠️ Desafios, Erros e Lições Aprendidas
-------------------------------------

Maior erro cometido durante o projeto:
Tentativa de implementar muitas funcionalidades ao mesmo tempo, dificultando a
identificação de erros.

Como lidamos com isso:
O código foi refatorado e passou a ser testado de forma incremental, módulo por módulo.

Maior desafio enfrentado durante o projeto:
Integrar corretamente jogador, inimigos, coletáveis, HUD e sistema de música.

Como lidamos com isso:
Centralizando o controle na classe principal do jogo.

Lições aprendidas:
- Importância do planejamento antes da implementação
- Benefícios da modularização
- Necessidade de testes constantes
- Uso do Git para trabalho em equipe


▶️ Como Executar o Projeto
-------------------------
1. Instalar o Python 3
2. Instalar o Pygame com o comando:
   pip install pygame
3. Executar o jogo com o comando:
   python main.py



