import pygame # 'pygame' contém as funcionalidades necessárias para criar um jogo.
from config import Config

config = Config()

# Ao colocar 'pygame.sprite.Sprite' a classe 'Fundo' 
# passa a herdar os atributos e os metódos da classe 'Sprite'.
class Fundo(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Inicializando a classe 'Sprite'.
        self.fundo = (pygame.image.load('imagens/fundo_dia.png'))  # Carregando a imagem para o fundo.

        self.image = self.fundo # Definiando imagem do fundo.

        self.rect = self.image.get_rect()  # Definindo retangulo da imagem.
        self.rect.topleft = 0, 0 # Posicionando o retangulo da imagem.
    
    def update(self): # O metódo 'update' é um metódo herdado da classe 'Sprite'.
        self.image = self.fundo # Desenhando o fundo corretamente.

# Ao colocar 'pygame.sprite.Sprite' a classe 'Chao' 
# passa a herdar os atributos e os metódos da classe 'Sprite'.
class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Inicializando a classe 'Sprite'.
        self.chao = (pygame.image.load('imagens/chao.png')) # Carregando a imagem para o chao.

        self.image = self.chao # Definiando imagem do chao.
 
        self.rect = self.image.get_rect() # Definindo retangulo da imagem.
        self.rect.topleft = 0, 576 # Posicionando o retangulo da imagem.

        self.velocidade = 0 # Definindo velocidade do chao.

    def update(self): # O metódo 'update' é um metódo herdado da classe 'Sprite'.
        # Artifícios utilizados para fazer o movimento do chao:
        self.velocidade -= config.velocidade_chao
        self.rect.topleft = self.velocidade, 576

        if self.velocidade <= -483:
            self.velocidade = 0
        self.image = self.chao
