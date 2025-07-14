import pygame
from modulos.janelas import janela

class ataque():
    def __init__(self, cor, ataque_x, ataque_y, ataque_w, ataque_h, mov_x, mov_y):
        self.retangulo = pygame.Rect(ataque_x, ataque_y, ataque_w, ataque_h)
        self.y = ataque_y
        self.x = ataque_x
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.cor = cor
        self.mostrar = True
    
    def atualizar(self, alma_rect, escudo, alma_estado):
        if self.mostrar:
            self.retangulo.x += self.mov_x
            self.retangulo.y += self.mov_y
            if self.retangulo.x >= janela.tela.get_width() or self.retangulo.x < 0:
                self.retangulo.x = self.x
            if self.retangulo.y >= janela.tela.get_height() or self.retangulo.y < 0:
                self.retangulo.y = self.y
            if self.retangulo.colliderect(alma_rect):
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
    ataque('white', 220, 550, 40, 40, 10, 0),
    ataque('white', 500, 500, 40, 40, 10, 0 ),
    ataque('red', 150, 150, 30, 30, 0, 0),
    ataque('green', 0, (janela.tela.get_height()/2), 40, 40, 3, 0),
    ataque('green', 1200, (janela.tela.get_height()/2), 40, 40, -5, 0),
    ]

def rodada2():
    return[
    ataque('blue', 220, 550, 40, 40, 10, 0),
    ataque('blue', 500, 500, 40, 40, 10, 0 ),
    ataque('blue', 150, 150, 30, 30, 10, 10),
    ataque('blue', 0, 0, 30, 30, 10, 10),
    ataque('blue', 50, 0, 30, 30, 10, 10),
    ataque('blue', 150, 80, 30, 30, 10, 20),
    ataque('blue', 300, 100, 30, 30, 10, 20),
    ]