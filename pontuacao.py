import pygame
from config import Config
from recorde import Record

config = Config()
record = Record()

class Pontuacao():
    def __init__(self):
        self.pontos = config.pontos
        self.pontuacao_maxima = record.record_atual
        
    def exibir_pontuacao(self):
        fonte = pygame.font.SysFont('arial', 35, True, False)
        msg = f'{self.pontos}'
        texto_formatado = fonte.render(msg, True, (255, 255, 255))
        return texto_formatado
    
    def somar_pontos(self):
        self.pontos += 1
        if self.pontos > self.pontuacao_maxima:
            self.pontuacao_maxima = self.pontos
            record.muda_recorde_atual(self.pontos)

    def return_pontuacao(self):
        self.fonte = pygame.font.SysFont('arial', 25, True, False)
        pontos_str = f'{self.pontos}'

        self.pontos_image = self.fonte.render(pontos_str, True, (255, 255, 255))
        return self.pontos_image
    
    def return_record(self):
        self.fonte = pygame.font.SysFont('arial', 25, True, False)
        pontuacao_maxima_str = f'{self.pontuacao_maxima}'

        self.pontuacao_maxima_image = self.fonte.render(pontuacao_maxima_str, True, (255, 255, 255))
        return self.pontuacao_maxima_image
    
    def exibir_mensagem_qualquer(self, mensagem, tamanho):
        fonte = pygame.font.SysFont('arial', tamanho, True, False)
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        return texto_formatado
