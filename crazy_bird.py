import pygame # 'pygame' contém as funcionalidades necessárias para criar um jogo.
from eventos import Eventos # 'eventos' contém as funções 'eventos' e 'atualizar_tela'.
from canos import Cano, Ajuste # 'canos' possui as classses Cano e Ajuste.
from config import Config
from pontuacao import Pontuacao

def iniciar(): # Função que inicia o jogo 
    pygame.init() # Inicializa as funcionalidades que o pygame precisa para funcionar.

    eventos = Eventos()
    pontuacao = Pontuacao()
    config = Config()

    pygame.display.set_caption('CRAZY BIRD') # Denomina o nome da janela do jogo.
    tela = pygame.display.set_mode((config.largura_tela, config.altura_tela)) # Ajuste de resolução por meio de uma tupla clássica.

    distancia_entre_canos = 0 # Distância entre os canos.
    relogio = pygame.time.Clock() # Criando relógio para variar a 'taxa de frames'.

    jogo_iniciado = 0
    
    while True: # Inicia o laço principal do jogo.
        relogio.tick(60) # Definindo 'taxa de frames' do jogo.

        if jogo_iniciado == 0:
            fundo = (pygame.image.load('imagens/fundo_dia.png'))  # Carregando a imagem para o fundo.
            chao = (pygame.image.load('imagens/chao.png'))
            menu = (pygame.image.load('imagens/menu.png'))
            menu = pygame.transform.scale(menu, (184*1.2, 267*1.2))
            
            tela.blit(fundo, (0,0))
            tela.blit(chao, (0, 576))
            tela.blit(menu, (90, 120))

            pygame.display.flip()
            eventos.eventos()
            jogo_iniciado = eventos.iniciar_game()
        
        elif jogo_iniciado == 1:
            if distancia_entre_canos == 0:
                ajuste = Ajuste() # Instância da classe 'Ajuste'.
                cano_base = Cano(0,  ajuste.altura()[0]) # 'ajuste.altura[0]' define uma altura aleatória.
                cano_ceu = Cano(180, ajuste.altura()[1]) # 'ajuste.altura[1]' define uma altura aleatória.
                distancia_entre_canos = config.distancia_entre_canos # Padronizando a distância entre os canos em 125.

            distancia_entre_canos -= 1 # Fazendo a diminuição da distância entre os canos até chegar em 0.

            eventos.eventos() # Chama o laço de eventos, para que os eventos sejam ouvidos o tempo todo.
            jogo_iniciado = eventos.iniciar_game()
            eventos.atualizar_tela(tela, cano_base, cano_ceu) # Faz as atualizações necessárias de posição.

        else:
            iniciar()

iniciar() # Inicializa completamente o jogo.