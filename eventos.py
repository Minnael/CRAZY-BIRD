import pygame # 'pygame' contém as funcionalidades necessárias para criar um jogo.
from pygame.locals import * # importando todos elementos de pygame.locals para utilizar 'QUIT'.
from sys import exit # Mais uma possibilidade para haver um possível 'game over' no jogo.
import time

from passaro import Passaro # Importando classe 'Passaro'.
from ambiente import Fundo, Chao # Importando as classes 'Fundo' e 'Chao' (classes ambiente).
from pontuacao import Pontuacao
from config import Config

# 'pygame.sprite.Group' faz com que seja criado um grupo de sprites.
sprites_chao = pygame.sprite.Group() 
sprites_passaro = pygame.sprite.Group()
sprites_cano = pygame.sprite.Group()
sprite_fundo = pygame.sprite.Group()

fundo = Fundo() # Instância da classe 'Fundo'.
passaro = Passaro() # Instância da classe 'Passaro'.
chao = Chao() # Instância da classe 'Chao'.
pontuacao = Pontuacao() # Instância da classe 'Pontuacao'.
config = Config()

class Eventos():
    def __init__(self):
        self.colidiu = config.colidiu
        self.iniciar_jogo = config.iniciar_jogo

    #Função responsável por guardar o laço de eventos.
    def eventos(self):
        # Um evento é uma ação realizada pelo usuário enquanto joga.
        # O laço 'for' é um laço de 'eventos' que é responsável por ouvir cada ação.
        for evento in pygame.event.get(): 
            if evento.type == QUIT: # Caso esse entre nesse 'if' o jogo encerrará.
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and self.colidiu == False and self.iniciar_jogo == 1:
                    passaro.salto() # Chamando salto ao apertar a tecla 'SPACE'.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.iniciar_jogo = 1

    def iniciar_game(self):
        return self.iniciar_jogo

    #Função responsável por atualizar a tela conforme as seguintes condições (tela, cano_base e cano_ceu).
    def atualizar_tela(self, tela, cano_base, cano_ceu):
        som_colisao = pygame.mixer.Sound('audio/colisao.wav')
        som_game_over = pygame.mixer.Sound('audio/game_over.wav')

        sprite_fundo.add(fundo) # Adiciona a 'fundo' ao grupo 'sprite_fundo'.
        sprites_chao.add(chao) # Adiciona 'chao' ao grupo 'sprites_chao'.
        sprites_passaro.add(passaro) # Adiciona 'passaro' ao grupo 'sprites_passaro'.
        sprites_cano.add(cano_base) # Adiciona 'cano_base' ao grupo 'sprites_cano'.
        sprites_cano.add(cano_ceu) # Adiciona 'cano_ceu' ao grupo 'sprites_cano'.

        # '.draw(tela)' é responsável por fazer o desenho das sprites de um determinado grupo na tela.
        sprite_fundo.draw(tela)
        sprites_cano.draw(tela)
        sprites_passaro.draw(tela)
        sprites_chao.draw(tela)
        #print(len(sprites_cano))
        # Definindo colisões:
        colisao_passaro_cano = pygame.sprite.spritecollide(passaro, sprites_cano, False, pygame.sprite.collide_mask)
        colisao_passaro_chao = pygame.sprite.spritecollide(passaro, sprites_chao, False, pygame.sprite.collide_mask)

        recorde = pontuacao.return_record()
        pontos = pontuacao.return_pontuacao()

        if colisao_passaro_cano or colisao_passaro_chao and self.iniciar_jogo == 1:
            if self.colidiu == False:
                self.colidiu = True
                som_colisao.play()
                som_game_over.play()
                
        if self.colidiu == True:
            if colisao_passaro_chao:
                game_over = (pygame.image.load('imagens/game_over.png'))  # Carregando a imagem para o fundo.
                game_over = pygame.transform.scale(game_over, (192*1.5, 42*1.5))
                pontuacao_atual = pontuacao.exibir_mensagem_qualquer('SUA PONTUAÇÃO: ', 23)
                recorde_atual = pontuacao.exibir_mensagem_qualquer('MAIOR PONTUAÇÃO: ', 23)

                recorde = pontuacao.return_record()

                tela.blit(pontos, (270, 298))
                tela.blit(recorde, (300, 348))
                tela.blit(pontuacao_atual, (50, 300))
                tela.blit(recorde_atual, (50, 350))
                tela.blit(game_over, (60, 180))

            else:
                passaro.colisao()
        else:
            # '.update' é responsável por fazer a atualização das sprites, ou seja, a troca de sprites.
            
            for cano in sprites_cano.copy():
                if cano.rect.x <= -45:
                    sprites_cano.remove(cano)
            
            sprite_fundo.update()
            sprites_cano.update(tela)
            sprites_passaro.update()
            sprites_chao.update()
            
        pygame.display.flip() # Atualizará continuamente o display para mostrar as novas posições.