import pygame # 'pygame' contém as funcionalidades necessárias para criar um jogo.
import random # 'random' é a biblioteca responsável por escolher 'tipos de canos aleatórios'.
import time
from pontuacao import Pontuacao
from config import Config

config = Config()
pontuacao = Pontuacao()

# Ao colocar 'pygame.sprite.Sprite' a classe 'Cano' 
# passa a herdar os atributos e os metódos da classe 'Sprite'.
class Cano(pygame.sprite.Sprite):
    def __init__(self, rotacao, ajuste): 
        # rotacao é responsável por definir o tipo de cano (base ou céu).
        # ajuste é responsável por receber um valor no eixo Y para definir a posição de um determinado cano. 
        self.rotacao = rotacao
        self.ajuste = ajuste 

        pygame.sprite.Sprite.__init__(self) # Inicializando a classe 'Sprite'.
        self.cano = (pygame.image.load('imagens/cano_verde.png')) # Carregando a imagem para do cano.

        self.image = self.cano # Definiando imagem do cano.
        self.image = pygame.transform.rotate(self.image, self.rotacao) # Fazendo a rotação necessária.

        self.rect = self.image.get_rect() # Definindo retangulo da imagem.

        self.mask = pygame.mask.from_surface(self.image) # Criando uma máscara para fazer a colisão.

        if self.rotacao == 0: # Se o cano tiver rotação 0 ele receberá um ajuste no 'top.left'.
            self.rect.topleft = (1000, self.ajuste)
        else:                 #Se o cano tiver rotação 180 ele receberá um ajuste no 'bottom.left'.
            self.rect.bottomleft = (1000, self.ajuste)

        self.velocidade = 0 # Definindo a velocidade em que os canos vão passar na tela.

    def update(self, tela): # O metódo 'update' é um metódo herdado da classe 'Sprite'.
        self.velocidade -= config.velocidade_canos

        pontos = pontuacao.return_pontuacao()

        if self.rotacao == 0: # Se o cano tiver rotação 0 ele receberá um ajuste no 'top.left'.
            self.rect.topleft = 700 + self.velocidade, self.ajuste
                
        else: # Se o cano tiver rotação 180 ele receberá um ajuste no 'bottom.left'.
            self.rect.bottomleft = 700 + self.velocidade, self.ajuste
            if 79 <= 700 + self.velocidade <= 81:
                som_ponto = pygame.mixer.Sound('audio/pontos.wav')
                som_ponto.play()
                pontuacao.somar_pontos()
        
        tela.blit(pontos, (200, 130))
        self.image = self.cano # Desenhando cano corretamente.
        self.image = pygame.transform.rotate(self.image, self.rotacao) # Atualizando ajuste na rotação.

# Classe responsável pela aleatoriedade do par de canos.
class Ajuste():
	def __init__(self):
        # Lista de possibilidades de pares de cano:
	    self.possibilidades = [[260, 130], [310, 180], [360, 230], [410, 280], [450, 320]]
	    self.possibilidade = random.randint(0, 4) # Define o componente da lista aleatoriamente.
    
	def altura(self): # Reponsável por fazer o 'return' da possibilidade selecionada.
	    return self.possibilidades[self.possibilidade]