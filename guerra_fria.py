import pygame as pg
from CONFIG_JOGO import ConfigJogo
from Cena_inicial import Cenainicial
from Cena_historia import Historia
from Cena_Selecao1 import *
from Cena_Selecao2 import *
from Cena_principal import *


class guerrafria:
    def __init__(self):
        pg.init()

      

    def rodar(self):
        ConfigJogo.Tela=1
        while True:
            if ConfigJogo.Tela==1:
                ConfigJogo.LARGURA_TELA=600
                ConfigJogo.ALTURA_TELA=400
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
            ))
                cena = Cenainicial(self.tela)        
                cena.rodar()
            if ConfigJogo.Tela==2:
                cena=Historia(self.tela)
                cena.rodar()
            if ConfigJogo.Tela==3:
                cena=CenaSelecao1(self.tela)
                cena.rodar()
                indice_1=cena.escolha()
            if ConfigJogo.Tela==4:
                cena=CenaSelecao2(self.tela)
                cena.rodar()
                indice_2=cena.escolha()
            if ConfigJogo.Tela==5:
               
                ConfigJogo.LARGURA_TELA=1200
                ConfigJogo.ALTURA_TELA=900
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
            ))
                
              
                
                cena=CenaPrincipal(self.tela, indice_1, indice_2)
                cena.rodar()
            
            
            

       