🎮 SpaCINvadors
===================

Disciplina: Introdução à Porgramação


👨‍💻 Divisão de Trabalho do Grupo
--------------------------------
| Integrante | Responsabilidade | Principais Tarefas |
| :--- | :--- | :--- |
| **Bruno Silva** | Gerência e Estrutura | Organização do projeto, estrutura de pastas e main.py. |
| **Layse Gomes** | Jogador | Classe Jogador, movimentação, tiros e power-ups. |
| **João Pedro Pessoa** | Inimigos | Classe Inimigo, velocidade e balanceamento. |
| **Antonio Moura** | Itens Coletáveis | Lógica de spawn (Café, Relógio, Wi-Fi) e efeitos. |
| **Ianne** | Interface e HUD | HUD, vidas, tempo e organização visual. |
| **Kraus Jatobá** | Áudio e Menus | Menus, efeitos sonoros e trilha sonora. |

📖 Descrição Geral do Projeto
----------------------------
Este projeto consiste no desenvolvimento de um jogo 2D utilizando a biblioteca Pygame.
O jogador controla um personagem que deve sobreviver o maior tempo possível, enfrentando
inimigos, coletando itens e gerenciando recursos como vidas, tempo e café (power-ups).

O jogo possui menu inicial, menu de pausa, tela de game over, sistema de tempo,
efeitos sonoros, música dinâmica e dificuldade progressiva.


🏗️ Arquitetura do Projeto
-------------------------
O projeto foi desenvolvido de forma modular, separando as responsabilidades em
diferentes arquivos dentro da pasta source/, facilitando a organização e manutenção
do código.

Descrição geral da estrutura:

main.py inicia o jogo e chama o núcleo do sistema.
core concentra regras gerais, estados e configurações.
entities contém todos os objetos que interagem no jogo.
ui gerencia interface gráfica e menus.
world controla o ambiente e geração de entidades.
audio organiza músicas e efeitos sonoros.
assets armazena todos os recursos visuais e sonoros.

A classe Jogo, localizada no arquivo main.py, é responsável por inicializar o sistema,
controlar o loop principal, gerenciar os estados do jogo e integrar todos os módulos.


🖼️ Galeria do Projeto
--------------------
![Menu](./assets/menuInicial.png)
![Gameplay](./assets/telaGameOver.png)
![Itens](./assets/telaGameplay.png)


🛠️ Ferramentas e Tecnologias
-----------------------------
- Python 3 – Linguagem principal do projeto
- Pygame – Desenvolvimento do jogo 2D
- VS Code – Editor de código
- Git/GitHub – Versionamento e colaboração
- Trello - Dinâmica de trabalho em equipe


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



