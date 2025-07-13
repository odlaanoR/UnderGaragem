import pygame
pygame.init()

largura = 640
altura = 480
velocidade = 3.2
x = 65
y = 450
transicaoTempo = 0
mostraTransicao = False
fps = pygame.time.Clock()
vida = 92
vidaAtual = 70

fonte = pygame.font.SysFont('arial', 30, True, False)
fonteBatalha = pygame.font.SysFont('comicsans', 20, True, False)
pygame.display.set_caption('Poggers')
icon = pygame.image.load('assets/images.png')
pygame.display.set_icon(icon)
musicaFundo = pygame.mixer.music.load('assets/Project147.mp3')
pygame.mixer.music.set_volume(0.45)
pygame.mixer.music.play(-1)
