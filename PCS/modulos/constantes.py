import pygame

pygame.init()

#Definições Padrões
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
direcao = None
zerouJogo = False
#telainicial = True

#Tela do Menu
botaoIniciar = pygame.Rect(270, 250, 120, 40)
botaoCreditos = pygame.Rect(270, 295, 120, 40)

#Variaveis de ataques e etc
ataque_iniciou = False
fim_do_ataque = pygame.event.custom_type()
fimInv = pygame.event.custom_type()
fase_atual = 0
dialogo_atual = 0
ataques_acabaram = False #só se torna True quando todos os ataques criados acabam
tempoInv = 900

jogador_def = 0
jogador_atk = 1

wilson_def = 99#LEMBRA DE MUDAR ISSO PELO AMOR DE DEUS
wilson_atk = 10
wilson_vida_max = 14000
wilson_vida_atual = 14000


caixa_combate = pygame.Rect(70, 190, 500, 180)

dano_mensagem = None
dano_cor = None
dano_tempo = 0

#definições de itens
efeito100limite = False
vidaAntes100limite = False
efeitoVerde = False
efeitoMcInfeliz = False
consumiuItem = False
encontrouBigaragem = False
encontrouMc = False
encontrouRevolver = False

#Contador de Ações
usouConversar = 0
usouVasculhar = 0
acaoSelecionada = None
usouAcao = False

#Fontes
fonte = pygame.font.SysFont('arial', 30, True, False)
fonteCustomizada = pygame.font.Font('PCS/assets/fonte2.ttf', 23)
fonteBatalha = pygame.font.SysFont('comicsans', 20, True, False)
pygame.display.set_caption('Undergaragem')

#Imagens
gameoverImg = pygame.image.load('PCS/assets/sprites/gameover.png')
gameoverImg = pygame.transform.scale(gameoverImg, (600, 300))
icon = pygame.image.load('PCS/assets/sprites/alma.png')
pygame.display.set_icon(icon)

WilsonIddle = pygame.image.load('PCS/assets/sprites/Wilsoniddle.png')

#Sons/Músicas
musicaFundo = pygame.mixer.music.load('PCS/assets/sounds/Project147.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
dano_snd = pygame.mixer.Sound('PCS/assets/sounds/dano.mp3')
parry_snd = pygame.mixer.Sound('PCS/assets/sounds/parry.mp3')
clica_som = pygame.mixer.Sound('PCS/assets/sounds/snd_select.mp3')
cura_som = pygame.mixer.Sound('PCS/assets/sounds/snd_heal.wav')

#textos
dialogos = (
    "*Aqui acabou",
    "*Quem é esse cara?",
    ("*diversas caixas e coisas estão próximas", "Use VASCULHAR para procurar por algo útil ao seu redor"),
    ("*Wilson Tremba parece tão confuso quanto você", "talvez CONVERSAR possa torna-lo amistoso?"),
    ("*Sr. Tremba mexeu no seu relógio", "o tempo parece se alterar levemente"),
    "*O ar estrala de puro terror",
    "*Caminhões tombam ao seu redor",
    "*Você escuta uma notificação de email ao longe",
    "*Que lugar é esse....?",
    ". . .",
    "CONTINUE VASCULHANDO, DEVE TER ALGO AQUI",
    "*Panelas batem em algum lugar a sua direita",
    "*Você escuta uma moto cortando um giro em outra realidade",
    "*ratos fazem barulho ao seu redor",
    ("*Alguém está batendo gravetos na caixa registradora" , "por algum motivo, tem cheiro de água sanitária"),
)


print('preparando constantes...')
