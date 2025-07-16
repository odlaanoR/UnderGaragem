import pygame
from modulos.janelas import *

class ataque():
    def __init__(self, cor, ataque_x, ataque_y, ataque_w, ataque_h, mov_x, mov_y, delay):
        self.retangulo = pygame.Rect(ataque_x, ataque_y, ataque_w, ataque_h)
        self.y = ataque_y
        self.x = ataque_x
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.cor = cor
        self.mostrar = False #se der MUITO errado resetar pra True e inverter a lógica dnv
        self.relogio = pygame.time.Clock()
        self.delay = delay * 1000
        self.ataque = False
        self.tempoInicio = 0
        self.ativado = False
    
    def iniciar(self):
        self.tempoInicio = pygame.time.get_ticks()
        self.ativado = False
        self.mostrar = False  # sempre começa invisível
        print("ataque iniciar executado")
        print(f"Ataque iniciado: delay={self.delay}ms, tempoInicio={self.tempoInicio}")
        
    def atualizar(self, alma, escudo, alma_estado):
        self.tempo_atual = pygame.time.get_ticks()
        #print(self.tempo_atual - self.tempoInicio)
        #print(f"[DEBUG] tempo_atual={self.tempo_atual}, tempoInicio={self.tempoInicio}, delta={self.tempo_atual - self.tempoInicio}, delay={self.delay}")
        if self.ativado == False and (self.tempo_atual - self.tempoInicio) >= self.delay:
            self.mostrar = True
            self.ativado = True
            #print("ativou com delay de: ", self.delay)
            
        if self.mostrar:
            self.retangulo.x += self.mov_x
            self.retangulo.y += self.mov_y
            if self.retangulo.x >= janela.tela.get_width() or self.retangulo.x < 0:
                self.retangulo.x = self.x
            if self.retangulo.y >= janela.tela.get_height() or self.retangulo.y < 0:
                self.retangulo.y = self.y
            if self.retangulo.colliderect(alma) and alma.acertavel:
                print("colidiu!")
                self.mostrar = False
                return "dano"
            elif self.retangulo.colliderect(escudo) and alma_estado == 2:
                print("Parry!")
                self.mostrar = False
                return "parry"         
        return False        

    def draw(self, surface):
        if self.mostrar:
            pygame.draw.rect(surface, self.cor, self.retangulo)

class Gerarataques():
    def __init__(self, rodada, duracao):
        self.duracao = duracao
        self.rodada = rodada
        self.ataques = self.rodada    

def rodada1():
    return[
    ataque('white', 1, (janela.tela.get_height()/2 + 30), 20, 20, 5, 0, 0),
    ataque('white', 1, (janela.tela.get_height()/2 - 30), 20, 20, 5, 0, 0 ),
    #ataque('red', 150, 150, 30, 30, 0, 0, 0), QUADRADO VERMELHO FARMANDO AURA
    ataque('green', 0, (janela.tela.get_height()/2), 20, 20, 3, 0, 0),
    ataque('green', (janela.tela.get_width()), (janela.tela.get_height()/2), 20, 20, -5, 0, 0),
    ataque('white', 1, (janela.tela.get_height()/2 - 50), 20, 20, 3, 0, 0 ),
    ataque('red', (janela.tela.get_width()), 200, 30, 30, 0, 0, 0),
    ataque('green', 0, ((janela.tela.get_height()/2) + 50), 20, 20, 3, 0, 0),
    ataque('white', 1, (janela.tela.get_height()/2 + 75), 20, 20, 3, 0, 0),
    ataque('green', (janela.tela.get_width()), ((janela.tela.get_height()/2)+ 100), 20, 20, -5, 0, 0),
    ]

def rodada2():
    return[
    ataque('blue', 220, 0, 20, 20, 0, 5, 0),
    ataque('blue', 300, 0, 20, 20, 0, 10, 0),
    ataque('blue', 350, 0, 20, 20, 0, 5, 0),
    ataque('blue', 460, 0, 20, 20, 0, 10, 0),
    ataque('blue', 380, 0, 20, 20, 0, 5, 0),
    ataque('blue', 400, 0, 20, 20, 0, 10, 0),
    ataque('blue', 600, 0, 20, 20, 0, 5, 0),
    ataque('blue', 120, 0, 20, 20, 0, 5, 0),
    ataque('blue', 170, 0, 20, 20, 0, 10, 0),
    ataque('blue', 200, 0, 20, 20, 0, 5, 0),
    ]

def rodada3():#ataque com a alma verde
    return[
    ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 1, 0, 1), #esses 5 vem da lateral
    ataque('yellow', 0, (janela.tela.get_height()/2), (janela.tela.get_width()), 20, 20, -2, 2), #esse da direita pra esquerda
    #ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 3, 0, 3),
    #ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 4, 0,4),
    #ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 5, 0, 5),
    #ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 1, 1), #esses 5 de cima/baixo
    #ataque('yellow', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, -5, 2),#esse em especifico vem de baixo
    #ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 3, 3),
    ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 4, 4),
    ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 5, 5)
    ]
