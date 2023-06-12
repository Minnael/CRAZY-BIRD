import pygame # 'pygame' contém as funcionalidades necessárias para criar um jogo.
from config import Config

config = Config()

# Ao colocar 'pygame.sprite.Sprite' a classe 'Passaro' 
# passa a herdar os atributos e os metódos da classe 'Sprite'.
class Passaro(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Inicializando a classe 'Sprite'.
        self.passaro = [] #Lista de sprites do passáro.
        self.passaro.append(pygame.image.load('imagens/bird1.png')) #0
        self.passaro.append(pygame.image.load('imagens/bird2.png')) #1
        self.passaro.append(pygame.image.load('imagens/bird3.png')) #2
        
        self.sprite_atual = 0 #Controlador da sprite atual do passaro.

        self.image = self.passaro[self.sprite_atual] # Definiando imagem da sprite atual.
        self.image = pygame.transform.scale(self.image, (34*1.3, 24*1.3)) # Ajuste na escala do passáro.
        self.image = pygame.transform.rotate(self.image, 0)

        self.altura = config.altura_inicial_passaro # Variável altura para o passáro.
        self.rect = self.image.get_rect() # Definindo retangulo da imagem.

        self.mask = pygame.mask.from_surface(self.image) # Criando uma máscara para fazer a colisão.
    
    def update(self): # O metódo 'update' é um metódo herdado da classe 'Sprite'.
        self.altura += 3.5
        self.sprite_atual = self.sprite_atual + 0.40 # Responsável pela velocidade do 'bater de asas'.

        if self.sprite_atual >= len(self.passaro): # Limitando 'self.sprite_atual' para reiniciar animação. 
            self.sprite_atual = 0

        self.rect.topleft = 80, (0 + self.altura) #Fazer com que o passáro caia por natureza.

        self.image = self.passaro[int(self.sprite_atual)] # Responsável pela troca de sprites.
        self.image = pygame.transform.scale(self.image, (34*1.3, 24*1.3)) # Ajuste na escala do passáro.
    
    def salto(self): # Metódo responsável por fazer o passáro subir.
        for i in range(12):
            self.altura -= 5
        som_voo = pygame.mixer.Sound('audio/voo.wav')
        som_voo.play()
    
    def voltar(self):
        self.altura -= 150

    def colisao(self):
        self.altura += 15
        self.rect.topleft = 80, self.altura #Fazer com que o passáro caia por natureza.

        self.image = self.passaro[int(self.sprite_atual)] # Responsável pela troca de sprites.
        self.image = pygame.transform.scale(self.image, (34*10, 24*10)) # Ajuste na escala do passáro.