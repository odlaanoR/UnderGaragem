import pygame
pygame.init()

#Definições Padrões
largura = 1280
altura = 720
velocidade = 3.2
x = 65
y = 450
transicaoTempo = 0
mostraTransicao = False
fps = pygame.time.Clock()
vida = 92
vidaAtual = 70
direcao = None

#relogio de ataques
ataque_iniciou = False
fim_do_ataque = pygame.event.custom_type()

#Fontes
fonte = pygame.font.SysFont('arial', 30, True, False)
fonteBatalha = pygame.font.SysFont('comicsans', 20, True, False)
pygame.display.set_caption('Undergaragem')

#Imagens
gameoverImg = pygame.image.load('assets/sprites/gameover.png')
icon = pygame.image.load('assets/sprites/alma.png')
pygame.display.set_icon(icon)

#Sons/Músicas
musicaFundo = pygame.mixer.music.load('assets/sounds/Project147.mp3')
pygame.mixer.music.set_volume(0.45)
pygame.mixer.music.play(-1)
dano_snd = pygame.mixer.Sound('assets/sounds/dano.mp3')
parry_snd = pygame.mixer.Sound('assets/sounds/parry.mp3')

print('preparando constantes...')
