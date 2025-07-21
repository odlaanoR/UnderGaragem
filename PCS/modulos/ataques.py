import pygame
from modulos.janelas import *
import modulos.constantes as cos

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
    def __init__(self, rodada, mudaalma=0, duracao=10):
        self.rodada = rodada
        self.ataques = self.rodada    
        self.mudaalma = mudaalma#declara o tipo de alma que será usado no ataque
        self.duracao = duracao*1000


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
    #nova leva de ataques
    ataque('white', 1, (janela.tela.get_height()/2 + 40), 20, 20, 5, 0, 2),
    ataque('white', 1, (janela.tela.get_height()/2 + 30), 20, 20, 5, 0, 2),
    ataque('white', 1, (janela.tela.get_height()/2 + 10), 20, 20, 5, 0, 2),
    ataque('white', 1, (janela.tela.get_height()/2 + 50), 20, 20, 5, 0, 2),
    ataque('white', 1, (janela.tela.get_height()/2 + 70), 20, 20, 5, 0, 2),
    #outra leva da direita para a esquerda
    ataque('white', (janela.tela.get_width()), (janela.tela.get_height()/2 - 10), 20, 20, -5, 0, 3),
    ataque('white', (janela.tela.get_width()), (janela.tela.get_height()/2 - 30), 20, 20, -5, 0, 3),
    ataque('white', (janela.tela.get_width()), (janela.tela.get_height()/2 + 70), 20, 20, -5, 0, 3),
    ataque('white', (janela.tela.get_width()), (janela.tela.get_height()/2 + 90), 20, 30, -5, 0, 3),
    ]

def rodada2():
    return[
    ataque('blue', 220, 0, 20, 20, 0, 5, 0),
    ataque('blue', 300, 0, 20, 20, 0, 7, 0),
    ataque('blue', 350, 0, 20, 20, 0, 5, 0),
    ataque('blue', 460, 0, 20, 20, 0, 7, 0),
    ataque('blue', 380, 0, 20, 20, 0, 5, 0),
    ataque('blue', 400, 0, 20, 20, 0, 7, 0),
    ataque('blue', 600, 0, 20, 20, 0, 5, 0),
    ataque('blue', 120, 0, 20, 20, 0, 5, 0),
    ataque('blue', 170, 0, 20, 20, 0, 7, 0),
    ataque('blue', 200, 0, 20, 20, 0, 5, 0),
    ataque('blue', 100, 0, 20, 20, 0, 5, 0),
    ataque('blue', 80, 0, 20, 20, 0, 5, 1),
    
    ataque('cyan', 300, (janela.tela.get_height()), 20, 20, 0, -5, 3),#nova leva de ataques vindas de baixo
    ataque('cyan', 260, (janela.tela.get_height()), 20, 20, 0, -3, 3),
    ataque('cyan', 240, (janela.tela.get_height()), 20, 20, 0, -4, 3),
    ataque('cyan', 460, (janela.tela.get_height()), 20, 20, 0, -5, 3),
    ataque('cyan', 350, (janela.tela.get_height()), 20, 20, 0, -7, 3),
    ataque('cyan', 400, (janela.tela.get_height()), 20, 20, 0, -5, 3),
    ataque('cyan', 380, (janela.tela.get_height()), 20, 20, 0, -7, 3),
    ataque('cyan', 550, (janela.tela.get_height()), 20, 20, 0, -5, 3),
    ataque('cyan', 120, (janela.tela.get_height()), 20, 20, 0, -5, 3),
    ataque('cyan', 170, (janela.tela.get_height()), 20, 20, 0, -7, 3),
    ataque('cyan', 200, (janela.tela.get_height()), 20, 20, 0, -5, 3),
    ]

def rodada3():#ataque com a alma verde
    return[
    ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 1, 0, 0), #esses 5 vem da lateral
    ataque('yellow', (janela.tela.get_width()), (janela.tela.get_height()/2), 20, 20, -2, 0, 2), #esse e os três abaixo vem da direita para a esquerda
    ataque('yellow', (janela.tela.get_width()), (janela.tela.get_height()/2), 20, 20, -6, 0, 7), 
    ataque('yellow', (janela.tela.get_width()), (janela.tela.get_height()/2), 20, 20, -2, 0, 4), 
    ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 3, 0, 3),
    ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 3, 0,5),
    ataque('yellow', 0, (janela.tela.get_height()/2), 20, 20, 3, 0, 6),
    ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 1, 1), #esses 5 de cima/baixo
    ataque('yellow', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, -5, 2),#esse e os dois abaixos vem de baixo
    ataque('yellow', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, -5, 5),
    ataque('yellow', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, -5, 6),
  
    ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 1, 3),
    ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 3, 5),
    ataque('yellow', (janela.tela.get_width()/2), 0, 20, 20, 0, 3, 6)
    ]

def rodada4():
    return[
        ataque('red', (janela.tela.get_width()/2), (janela.tela.get_height()/2-90), 20, 20, 0, 0, 0),
        ataque('red', 20, (janela.tela.get_height()/2-90), 20, 20, 3, 3, 0),
        ataque('red', 50, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 2),
        ataque('red', 70, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 0),
        ataque('red', 100, (janela.tela.get_height()/2-90), 20, 20, 3, 3, 4),
        ataque('red', 30, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 6),
        ataque('red', 10, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 4),
        ataque('red', 65, (janela.tela.get_height()/2-90), 20, 20, 3, 3, 8),
        ataque('red', 91, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 10),
        ataque('red', 0, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 8),

        ataque('orange', 0, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 2),
        ataque('orange', 0, (janela.tela.get_height()/2-90), 20, 20, 3, 3, 4),
        ataque('orange', 0, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 6),
        ataque('orange', 15, (janela.tela.get_height()/2-90), 20, 20, 3, 3, 0),
        ataque('orange', 30, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 2),
        ataque('orange', 50, (janela.tela.get_height()/2-90), 20, 20, 2, 2, 1),

        ataque('yellow', (janela.tela.get_width()/2-20), (janela.tela.get_height()/2-90), 20, 20, 0, 3, 0),
        ataque('yellow', (janela.tela.get_width()/2-30), (janela.tela.get_height()/2-90), 20, 20, 0, 2, 2),
        ataque('yellow', (janela.tela.get_width()/2-40), (janela.tela.get_height()/2-90), 20, 20, 0, 2, 1),

        ataque('yellow', (janela.tela.get_width()/2+20), (janela.tela.get_height()/2-90), 20, 20, 0, 3, 0),
        ataque('yellow', (janela.tela.get_width()/2+30), (janela.tela.get_height()/2-90), 20, 20, 0, 2, 2),
        ataque('yellow', (janela.tela.get_width()/2+40), (janela.tela.get_height()/2-90), 20, 20, 0, 2, 1),
    ]

def rodada5():
    return[
        ataque('purple', 40, (janela.tela.get_height()/2-50), 20, 20, 4, 0, 0),#onda de ataques da direita para a esquerda
        ataque('purple', 35, (janela.tela.get_height()/2-30), 20, 20, 4, 0, 0),
        ataque('purple', 30, (janela.tela.get_height()/2-10), 20, 20, 4, 0, 0),
        ataque('purple', 25, (janela.tela.get_height()/2+10), 20, 20, 4, 0, 0),
        ataque('purple', 20, (janela.tela.get_height()/2+30), 20, 20, 4, 0, 0),
        ataque('purple', 15, (janela.tela.get_height()/2+50), 20, 20, 4, 0, 0),
        ataque('purple', 10, (janela.tela.get_height()/2+70), 20, 20, 4, 0, 0),


        ataque('purple', (janela.tela.get_width()-40), (janela.tela.get_height()/2+100), 20, 20, -4, 0, 1),#onda de ataques da esquerda pra direita
        ataque('purple',  (janela.tela.get_width()-35), (janela.tela.get_height()/2+80), 20, 20, -4, 0, 1),
        ataque('purple', (janela.tela.get_width()-30), (janela.tela.get_height()/2+60), 20, 20, -4, 0, 1),
        ataque('purple', (janela.tela.get_width()-25), (janela.tela.get_height()/2+40), 20, 20, -4, 0, 1),
        ataque('purple', (janela.tela.get_width()-20), (janela.tela.get_height()/2+20), 20, 20, -4, 0, 1),
        ataque('purple', (janela.tela.get_width()-15), (janela.tela.get_height()/2), 20, 20, -4, 0, 1),
        ataque('purple', (janela.tela.get_width()-10), (janela.tela.get_height()/2-20), 20, 20, -4, 0, 1),

        ataque('pink', (janela.tela.get_width()), (janela.tela.get_height()/2+40), 20, 20, -5, 0, 3), #ataques 'aleatorios' que dificultam a passagem
        ataque('pink', (janela.tela.get_width()), (janela.tela.get_height()/2-40), 20, 20, -5, 0, 2),
        ataque('pink', 0, (janela.tela.get_height()/2-20), 20, 20, 5, 0, 3),
        ataque('pink', 0, (janela.tela.get_height()/2), 20, 20, 5, 0, 2),
        ataque('pink', 0, (janela.tela.get_height()/2+20), 20, 20, 5, 0, 3),
    ]

def rodada6():#esse ataque deveria obrigar o player a girar, mas to começando a repensar e talvez eu remova, ta dificil codar
    return[
        ataque('brown', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, -2, 0),#ataque que sobe
        ataque('red', (janela.tela.get_width()/2+80), (janela.tela.get_height()-40), 20, 20, -2, -2, 0),#ataque da direita que sobe
        ataque('blue', (janela.tela.get_width()), (janela.tela.get_height()/2), 20, 20, -2, 0, 0),#ataque da direita que vem reto
        ataque('purple', (janela.tela.get_width()/2+80), (janela.tela.get_height()/2-80), 20, 20, -2, 2, 0),#ataque da direita que desce
        ataque('yellow', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, 2, 0),
        ataque('white', (janela.tela.get_width()/2), (janela.tela.get_height()), 20, 20, 0, 2, 0),
    ]