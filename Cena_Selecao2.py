import pygame as pg
from constantes import Constantes
from lista_personagens import lista_2
import sys



class CenaSelecao2:
    def __init__(self, tela):
        self.tela = tela       
        self.fim= False
        self.indice=0
        self.lista=lista_2
        self.px=0
        self.py=0
        self.py_rect=(0.458 * Constantes.ALTURA_TELA // 2) 
        


        # cria os textos que serao mostrados na tela
        font_titulo = pg.font.SysFont(None, Constantes.FONTE_SUBTITULO)
        font_subtitulo = pg.font.SysFont(None, Constantes.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'JOGADOR 2', True, Constantes.COR_TITULO)
        self.selecao1 = font_subtitulo.render(
            self.lista[0].nome, True, Constantes.COR_TITULO)
        self.selecao2 = font_subtitulo.render(
            self.lista[1].nome, True, Constantes.COR_TITULO)
        self.selecao3 = font_subtitulo.render(
           self.lista[2].nome, True, Constantes.COR_TITULO)
        self.selecao4 = font_subtitulo.render(
            self.lista[3].nome, True, Constantes.COR_TITULO)


    def rodar(self):
        while not self.fim:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
         for event in pg.event.get():
            
            if (event.type == pg.QUIT):
                sys.exit(0)
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                    (pg.key.get_pressed()[pg.K_ESCAPE]):
                self.fim = True
                Constantes.Tela=1

       
            if pg.key.get_pressed()[pg.K_SPACE]:
                self.fim = True
                Constantes.Tela=5
            if   (event.type == pg.KEYDOWN and event.key == pg.K_i) and self.indice>0:
                self.py_rect=self.py_rect-0.25* Constantes.ALTURA_TELA // 2
                self.indice-=1
             
            if   (event.type == pg.KEYDOWN and event.key == pg.K_k) and self.indice<=2:
                self.py_rect=self.py_rect+0.25* Constantes.ALTURA_TELA // 2
                self.indice+=1
              
                


    

        

    def atualiza_estado(self):
        pass

    def desenha(self):
        self.tela.fill((50, 100, 255))
        self.px = Constantes.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        self.py = (0.2 * Constantes.ALTURA_TELA // 2)
        self.tela.blit(self.titulo, (self.px, self.py))
        self.px = Constantes.LARGURA_TELA // 2 - \
        self.selecao1.get_size()[0] // 2
        self.py = (0.5 * Constantes.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao1, (self.px, self.py))
        self.px = Constantes.LARGURA_TELA // 2 - \
        self.selecao2.get_size()[0] // 2
        self.py = (0.75 * Constantes.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao2, (self.px, self.py))
        self.px = Constantes.LARGURA_TELA // 2 - \
        self.selecao3.get_size()[0] // 2
        self.py = (1 * Constantes.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao3, (self.px, self.py))
        self.px = Constantes.LARGURA_TELA // 2 - \
        self.selecao4.get_size()[0] // 2
        self.py = (1.25 * Constantes.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao4, (self.px, self.py))
        self.rect()
        pg.display.flip()
    def rect(self):
        pg.draw.rect(
            surface=self.tela,
            color=(255,255,255),
            rect=(self.px-0.02*Constantes.LARGURA_TELA,self.py_rect,self.px+0.13*Constantes.LARGURA_TELA
        // 2 , 0.1*Constantes.ALTURA_TELA),
            width=3)
    def escolha(self):
        return self.indice
