import pygame
from modulos.janelas import janela

class Ataque():
    def __init__(self, cor , ataque_x, ataque_y, ataque_w, ataque_h, mov_x, mov_y, vel):
        self.retangulo = pygame.Rect(ataque_x, ataque_y, ataque_w, ataque_h)
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.vel = vel
        self.cor = cor
        self.mostrar = True
        self.contador = 0 #opa coisa nova, não sei se vai ficar aqui por mt tempo, mas nesse ataque padrão vai servir (explico lá embaixo)

    def atualizar(self, alma_rect):
        if self.mostrar == True:
            self.retangulo.x += self.mov_x
            self.retangulo.y += self.mov_y
            if self.retangulo.x >= 530:
                self.retangulo.x = 80
                self.contador += 1
            if self.retangulo.colliderect(alma_rect):
                print("colidiu!")
                self.mostrar = False
                return True
            return False
            
    def draw(self):
        if self.mostrar:
            self.sla1 = pygame.draw.rect(janela.tela, self.cor, self.retangulo)
    
ataque = Ataque((255,255,255), 80, 220, 20, 20, 3, 0, 5)
ataque2 = Ataque('white', 90, 250, 40, 40, 10, 0, 5)
ataque3 = Ataque('red', 150, 150, 30, 30, 0, 0, 0)

print('carregando ataques...')
