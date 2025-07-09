import pygame
from pygame.locals import *

pygame.init()
#Iniciando e setando as bases do jogo
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

dano_snd = pygame.mixer.Sound('PCS/assets/sounds/dano.mp3')
txt_snd = pygame.mixer.Sound('PCS/assets/sounds/txt.mp3')
parry_snd = pygame.mixer.Sound('PCS/assets/sounds/parry.mp3')

player_pos = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2)


icone = pygame.image.load('PCS/assets/sprites/alma.png')
pygame.display.set_caption("ataque,ataque, isso aqui ta ligado?")
pygame.display.set_icon(icone)

#Tudo isso aqui é uma tentativa de fazer o sprite da alma funcionar
class Alma(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('PCS/assets/sprites/alma.png'))
        self.sprites.append(pygame.image.load('PCS/assets/sprites/almaazul.png'))
        self.sprites.append(pygame.image.load('PCS/assets/sprites/almaverde.png')) 
        self.game_over = pygame.image.load('PCS/assets/sprites/almaquebrada.png')      
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = player_pos.x, player_pos.y

    def update(self):
        self.rect.center = player_pos.x, player_pos.y
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (50, 50))

    def morte(self):
        self.image = self.game_over
        self.image = pygame.transform.scale(self.image, (50, 50))



def mostratexto(texto, finalizada):
    texto_final = ""
    global texto_completo
    global textbox
    if finalizada == False:
        for letra in texto:
                texto_final = texto_final + letra
                txt_snd.play()
                #print(texto_final)
                textbox = fonte.render(texto_final, False, 'white')
        if texto_final == texto:
                print("Concluido!")
                finalizada = True
        if finalizada == True:
            texto_completo = True



class Ataque():
    def __init__(self, cor , ataque_x, ataque_y, ataque_w, ataque_h, mov_x, mov_y, vel):
        self.retangulo = pygame.Rect(ataque_x, ataque_y, ataque_w, ataque_h)
        self.y = ataque_y
        self.x = ataque_x
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.vel = vel
        self.cor = cor
        self.mostrar = True

    def atualizar(self, alma_rect, escudo):
        if self.mostrar == True:
            self.retangulo.x += self.mov_x
            self.retangulo.y += self.mov_y
            if self.retangulo.x >= tela.get_width() or self.retangulo.x < 0:
                self.retangulo.x = self.x
            if self.retangulo.y >= tela.get_height() or self.retangulo.y < 0:
                self.retangulo.y = self.y
            if self.retangulo.colliderect(alma_rect):
                print("colidiu!")
                self.mostrar = False
                return("dano")
            elif self.retangulo.colliderect(escudo) and alma.estado == 2:
                print("Parry!")
                self.mostrar = False
                return ("parry")
            return False
            
    def draw(self):
        if self.mostrar == True:
            self.sla1 = pygame.draw.rect(tela, self.cor, self.retangulo)




def verde():
    global escudo
    if direcao == "cima":
        escudo = pygame.draw.line(tela, 'green', (((tela.get_width() / 2)-50), ((tela.get_height() / 2)-50)), (((tela.get_width() / 2)+50), ((tela.get_height() / 2)-50)), 4)
    elif direcao == "baixo":
        escudo = pygame.draw.line(tela, 'yellow', (((tela.get_width() / 2)-50), ((tela.get_height() / 2)+50)), (((tela.get_width() / 2)+50), ((tela.get_height() / 2)+50)), 4)
    elif direcao == "esquerda":
        escudo = pygame.draw.line(tela, 'red', (((tela.get_width() / 2)-50), ((tela.get_height() / 2)+50)), (((tela.get_width() / 2)-50), ((tela.get_height() / 2)-50)), 4)
    elif direcao == "direita":
        escudo = pygame.draw.line(tela, 'blue', (((tela.get_width() / 2)+50), ((tela.get_height() / 2)+50)), (((tela.get_width() / 2)+50), ((tela.get_height() / 2)-50)), 4)


ataque1 = Ataque ('white', 220, 550, 40, 40, 10, 0, (75*dt))
ataque2 = Ataque ('white', 500, 500, 40, 40, 10, 0, (75*dt))
ataque3 = Ataque ('red', 150, 150, 30, 30, 0, 0, 0)
ataque4 = Ataque ('green', 0, (tela.get_height()/2), 40, 40, 3, 0, 3)
ataque5 = Ataque ('green', 1200, (tela.get_height()/2), 40, 40, -5, 0, 3)


escudo = pygame.draw.line(tela, 'blue', (0,0), (0,0), 1)

fonte = pygame.font.SysFont('arial', 40, False)

alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)


#variaveis diversas vão aqui
ataques = []#Adicionar isso em um módulo a parte
dialogos = ["*Aqui acabou.", "*Ola", "*Esse é o fim", "*C O N T I N U E  A T A C A N D O"]#Adicionar isso em um módulo a parte
dialogo_atual = 0
x = 0
y = 0
Mostrar_ataque1 = True
texto_completo = False
direcao = ""

##Variaveis de vida e etc
vida = 92
vida_max = 92
barra_x = (tela.get_width()/2)
barra_y = 650
barra_largura = 200
barra_altura = 40



while True:
    tela.fill('black')
    #checar o estado da alma para aplicar
    if alma.estado == 1:
        player_pos.y += 100 * dt
        pygame.display.set_caption("Você está azul agora!")
            
    elif alma.estado == 2 :
        player_pos.x = (tela.get_width())/2
        player_pos.y = (tela.get_height())/2
        speed = 0
        verde()
        pygame.display.set_caption("Você está verde!")
    else:
        pygame.display.set_caption("Você se enche de DETERMINAÇÃO")
        speed = 300

    if vida < 0:
        print("Você morreu")
        vida = 92
        alma.morte()



    artes.draw(tela)
    artes.update()
    ataques.clear()

    if ataque1.mostrar:
        ataque1.draw()     
        resultado = ataque1.atualizar(alma.rect, escudo) 
        if resultado == "dano":
            vida -= 10
            dano_snd.play()

    if ataque2.mostrar:
        ataque2.draw()      
        resultado = ataque2.atualizar(alma.rect, escudo)
        if resultado == "dano":
            dano_snd.play()
            vida -= 10

    if ataque3.mostrar:
        ataque3.draw()
        resultado = ataque3.atualizar(alma.rect, escudo)
        if resultado == "dano":
            vida -= 20
            dano_snd.play()        

    if ataque4.mostrar:
        ataque4.draw()
        resultado = ataque4.atualizar(alma.rect, escudo)
        if resultado == "dano":
            vida -= 10
            dano_snd.play()     
        elif resultado == "parry":
            parry_snd.play()

    if ataque5.mostrar:
        ataque5.draw()
        resultado = ataque5.atualizar(alma.rect, escudo)
        if resultado == "dano":
            vida -= 10
            dano_snd.play()     
        elif resultado == "parry":
            parry_snd.play()



    #tratamento de teclas e eventos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        speed -= 150

    if keys[pygame.K_UP]:
        player_pos.y -= speed * dt
        direcao = "cima"
    if keys[pygame.K_DOWN]:
        player_pos.y += speed * dt
        direcao = "baixo"

    if keys[pygame.K_LEFT]:
        player_pos.x -= speed * dt
        direcao = "esquerda"

    if keys[pygame.K_RIGHT]:
        player_pos.x += speed * dt
        direcao = "direita"

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
            elif event.key == K_k:
                dialogo_atual += 1
                texto_completo = False
                    

    #Barra de vida
    barra_total = pygame.draw.rect(tela, (255, 0, 0), (barra_x, barra_y, barra_largura, barra_altura))
    largura_atual = int((vida / vida_max) * barra_largura)
    barra_atual = pygame.draw.rect(tela, (0, 255, 0), (barra_x, barra_y, largura_atual, barra_altura))
    stts_vida = f"{vida}/{vida_max} : "
    txtf = fonte.render(stts_vida, False, 'white')
    tela.blit(txtf, ((barra_x)-100,(barra_y)))

    #tentativa de mostrar um texto
    if texto_completo == False:
        mostratexto(dialogos[dialogo_atual], False)  
    else:
        tela.blit(textbox, (400, 400))

    pygame.display.flip()    
    dt = clock.tick(60)/1000
