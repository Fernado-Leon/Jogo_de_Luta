from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg
import math




class tirinho:
    def __init__(self):
        self.cronometro=cronometro()
        self.velocidade_magia=5
        self.x=ConfigJogo.LARGURA_TELA//4
        self.y=ConfigJogo.ALTURA_TELA//2
        self.posicao_magia=(self.x, self.y)
        self.termina=0
        
        
      
        
    def dano(self, tela, jogador, inimigo):
           
          
            self.posicao_magia=(self.x, self.y)
            pg.draw.circle(
            surface=tela,
            color=(255, 10, 50),
            center=(self.posicao_magia),
            radius=10,
            width=0
            )
            if (((self.x-inimigo.posicao[0])**2)+((self.y-inimigo.posicao[1])**2))**0.5<=50:
                inimigo.vida-=jogador.dano_magico//40
            self.mover_magia(jogador)
           

    def mover_magia(self, jogador):
            if jogador.direcao==0:  
                if self.x<ConfigJogo.LARGURA_TELA:
                    self.x=self.x+self.velocidade_magia
                    self.posicao_magia=(self.x, self.y)
            if jogador.direcao==1:  
                if self.x<ConfigJogo.LARGURA_TELA:
                    self.x=self.x-self.velocidade_magia
                    self.posicao_magia=(self.x, self.y)
    def resetar_posicao(self, jogador):
        self.termina=0
        self.x=jogador.posicao[0]+ConfigJogo.meiotamanho_per
        self.y=jogador.posicao[1]+ConfigJogo.meiotamanho_per
        self.posicao_magia=(self.x, self.y)
    def tempo(self):
        if self.cronometro.tempo_passado()>4:
            self.termina=1
            self.cronometro.reset()
              

        
           
           

        
           
           