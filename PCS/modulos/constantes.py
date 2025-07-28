import pygame

pygame.init()

#Definições Padrões
largura = 640
altura = 480
velocidade = 3.2
x = 286
y = 270
fps = pygame.time.Clock()   
vida = 92
vidaAtual = 92
direcao = None
zerouJogo = False
desapareceMensagem = False
#telainicial = True

#transições
transicaoTempo = 0
mostraTransicao = False
transicaoFinal = False
transicaoGradual = 0
fazGradual = False
gradualSurface = pygame.Surface((640,480))

#Tela do Menu
botaoIniciar = pygame.Rect(270, 250, 120, 40)
botaoCreditos = pygame.Rect(270, 295, 120, 40)
#outros botões
botaoSim = pygame.Rect(80, 290, 120, 40)
botaoNao = pygame.Rect(430, 290, 120, 40)
#Variaveis de ataques e etc
ataque_iniciou = False
fim_do_ataque = pygame.event.custom_type()
fimInv = pygame.event.custom_type()
fase_atual = 0
dialogo_atual = 0
ataques_acabaram = False #só se torna True quando todos os ataques criados acabam
tempoInv = 900
velocidade_azul = 6.0
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
fonteDano = pygame.font.Font('PCS/assets/hachicro.TTF', 35)
fonteBatalha = pygame.font.SysFont('comicsans', 20, True, False)
pygame.display.set_caption('Undergaragem')

#Imagens
gameoverImg = pygame.image.load('assets/sprites/gameover.png')
gameoverImg = pygame.transform.scale(gameoverImg, (600, 300))
icon = pygame.image.load('assets/sprites/alma.png')
pygame.display.set_icon(icon)
#WilsonIddle = pygame.image.load('PCS/assets/sprites/Wilson.png')
wilsonsheet = pygame.image.load('assets/sprites/wilsonsheet.png')
tituloMenu = pygame.image.load('assets/sprites/UNDERGARAGEM.png')
tituloMenu = pygame.transform.scale(tituloMenu, (560, 500))
sprite_sheet = pygame.image.load('assets/sprites/ataquesheet3.png')
animandoWilson = True


#Sons/Músicas
musicaFundo = pygame.mixer.music.load("assets/sounds/[Tremba's Contract].mp3")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)
dano_snd = pygame.mixer.Sound('assets/sounds/dano.mp3')
parry_snd = pygame.mixer.Sound('assets/sounds/parry.mp3')
clica_som = pygame.mixer.Sound('assets/sounds/snd_select.mp3')
cura_som = pygame.mixer.Sound('assets/sounds/snd_heal.wav')
transicaoSom = pygame.mixer.Sound('assets/sounds/transicao.ogg')
tocouTransicao = False
tocouMenu = False
tocouFimPacifista = False
tocouGenocida = False
tocouAtaque = False

#textos
dialogos = (
    "*Aqui acabou",
    "*Quem é esse cara?",
    ("*Você olha ao redor, diversas caixas e coisas estão próximas", "Use VASCULHAR para procurar por algo útil"),
    ("*Sr. Tremba mexeu no seu relógio", "o tempo parece se alterar levemente"),
    "C o n t i n u e  a t a c a n d o",
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
