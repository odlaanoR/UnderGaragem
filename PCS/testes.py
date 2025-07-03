import pygame
from pygame.locals import *

pygame.init()
#Iniciando e setando as bases do jogo
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0


player_pos = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2)


icone = pygame.image.load('PCS/assets/alma.png')
pygame.display.set_caption("Teste,teste, isso aqui ta ligado?")
pygame.display.set_icon(icone)

class Alma(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('PCS/assets/alma.png'))
        self.sprites.append(pygame.image.load('PCS/assets/almaazul.png'))
        self.sprites.append(pygame.image.load('PCS/assets/almaverde.png'))       
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = player_pos.x, player_pos.y

    def update(self):
        self.rect.center = player_pos.x, player_pos.y
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (50, 50))

alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)


while True:
    if alma.estado == 1:
        player_pos.y += 100 * dt
        pygame.display.set_caption("Você está azul agora!")
            
    elif alma.estado == 2 :
        speed = 0
        pygame.display.set_caption("Você está verde!")
    else:
        pygame.display.set_caption("Você se enche de DETERMINAÇÃO")
        speed = 300

    tela.fill('black')

    artes.draw(tela)
    artes.update()



    keys = pygame.key.get_pressed()

    if keys[pygame.K_x]:
        speed -= 150

    if keys[pygame.K_UP]:
        player_pos.y -= speed * dt

    if keys[pygame.K_DOWN]:
        player_pos.y += speed * dt

    if keys[pygame.K_LEFT]:
        player_pos.x -= speed * dt

    if keys[pygame.K_RIGHT]:
        player_pos.x += speed * dt

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            #print("Apertou algo!")
            if event.key == K_F11:
                #print("Pondo em tela cheia...")
                pygame.display.toggle_fullscreen()
            elif event.key == K_j:
                print('mudando o estado da alma para ', {alma.estado})
                alma.estado += 1
                if alma.estado == 3:
                    alma.estado = 0

    
    dt = clock.tick(60)/1000
