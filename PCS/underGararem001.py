import pygame
from pygame.locals import *
from sys import exit
import time

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

class Janelas():
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura,altura))
        self.telaAtual = 'ações'
        
    def mudarTela(self,novaTela):
        self.telaAtual = novaTela
    
    def atualizaTela(self):
        pygame.display.flip()
        
    def escreveTexto(self, texto, fonte, cor, posicao):
        txt = fonte.render(texto,True,cor)
        self.tela.blit(txt,posicao)
        
    def corFundo(self,cor=(0,0,0)):
        self.tela.fill(cor)
        
    def desenhaCaixa(self, caixa):
        self.caixa = pygame.draw.rect(janela.tela, (255,255,255), caixa, width=7)
    
class Acoes(): #to começando a achar que essa classe ta maior doq deveria mas fazer oq
    corPadrao = (150,75,0)
    novaCor = (255,255,0)
    def __init__(self, pos_x, msg): 
        self.botao = pygame.Rect(pos_x, 430, 100, 40)
        self.cor = self.corPadrao
        self.mostraMsg = False #é o que confirma se o texto quando clicar nos botões deve ou não aparecer
        self.mensagem = msg #é o texto que aparece quando clica em algum dos botões de ações
        self.passou = False
        self.gambiarraMsg = pygame.Rect((0,0,0,0)) #ah, esqueci de explicar. Isso aqui foi uma variável que eu criei pq queria que o texto lá das ações fossem clicáveis (talvez tenha um jeito melhor de fazer isso)
        self.mira = pygame.Rect((0,0,0,0))
        self.x_mira = 40
        self.mirando = False
        self.comecaBatalha = False #isso indica se a batalha deve ou não começar
        self.impedeTravaPos = False #e esse aqui impede que o x e o y do jogador seja resetado. EU N AGUENTO MAIS (não pensei em um nome melhor)
        self.comecoMira = 0 #tive que criar isso aqui pq a mira tava selecionando automaticamente
        
    def desenhaAcoes(self):
        pygame.draw.rect(janela.tela, self.cor, self.botao, width=2)

    def checaAlma(self):
        if alma.rect.colliderect(self.botao):
            self.cor = self.novaCor
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.wav')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False   
        else:
            self.cor = self.corPadrao
            self.passou = True
            
    def checaClique(self, tecla):
        if tecla == K_z and alma.rect.colliderect(self.botao):
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.wav')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.gambiarraMsg = pygame.Rect(30, 215, 10, 10)
            if self.mensagem == 'Item':
                global x, y
                x = 155
                y = 220
                janela.mudarTela('inventário') 
            else:
                self.mostraMsg = True
    def mirar(self, tecla):
        global tempoAtual
        if self.mirando:
            self.alvo = pygame.image.load('assets/mira.png')
            self.alvo = pygame.transform.scale(self.alvo, (600, 135))
            janela.tela.blit(self.alvo, (20, 205))
            self.x_mira += 5.6
            self.mira = pygame.Rect(self.x_mira, 205, 7, 140)
            pygame.draw.rect(janela.tela, (255,255,255), self.mira)
            tempoAtual = pygame.time.get_ticks()
            if self.x_mira >= 620 or (tecla == K_z and tempoAtual - self.comecoMira >= 100):
                self.mirando = False
                self.x_mira = 40
                self.comecaBatalha = True
            
    def batalhaAcontece(self):
        global x, y, tempoLuta, contadorTurno
        contadorTurno = 0
        if self.comecaBatalha and self.impedeTravaPos == False:
            tempoLuta = pygame.time.get_ticks()
            janela.mudarTela('lutaAcontecendo')
            x = 320
            y = 260
            self.impedeTravaPos = True
            contadorTurno += 1
            
    def confirmaAcao(self, tecla):
        if self.mostraMsg and tecla == K_z and alma.rect.colliderect(self.gambiarraMsg):
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.wav')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.mostraMsg = False
            return True
        return False

    def cancelaAcao(self):
        self.mostraMsg = False
            
    def acoesMensagem(self, fonte):
        if self.mostraMsg:
            janela.tela.blit(fonte.render(self.mensagem, True, (255,255,255)), (43,205))

    def confirmaLuta(self):
        self.mirando = True
        self.comecoMira = pygame.time.get_ticks()
        
    def confirmaAgir(self):
        print('poggers')
        
    def confirmaTelaItem(self):
        janela.mudarTela('inventário')
            
    def confirmaPiedade(self):
        print('Mas não estava amarelo')
        
class Item():
    def __init__(self, nome, descricao, quantidade=1):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.colisao = pygame.Rect(0,0,0,0)
        self.passou = False
        
    def usar(self):
        global vidaAtual
        if self.nome == 'Bolo de Sushi': 
            vidaAtual = min(vidaAtual + 30, vida)
        elif self.nome == 'Cuscuz Paulista':
            vidaAtual -= 1
        if self.quantidade > 0:
            self.quantidade -= 1
        if self.quantidade <= 0 and self in itens:
            itens.remove(self)

    def checaAlma(self):
        if alma.rect.colliderect(self.colisao):
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.wav')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False
        else:
            self.passou = True
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
    
class Alma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/sprites/alma.png'))
        self.sprites.append(pygame.image.load('assets/sprites/almaazul.png'))
        self.sprites.append(pygame.image.load('assets/sprites/almaverde.png'))       
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def update(self):
        self.rect.center = x, y
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        
janela = Janelas(largura,altura)

itens = [
    Item('Bolo de Sushi', 'Você recupera 30 de vida'),
    Item('Cuscuz Paulista','NAOOOOOOOOOOOOOOOOOOOOOOO'),
    Item('Comida3','sla3'),
    Item('Comida4','sla4'),
    Item('Comida5','sla5'),
    Item('Comida6','sla6'),
    Item('Comida7','sla7'),
    Item('Comida8','sla8'),
    Item('Comida9','sla9'),
]
botoes = [
    Acoes(50, "Wilson Tremba"),
    Acoes(190, "Checar"),
    Acoes(330, "Item"),
    Acoes(470, "Piedade"),
    ]
alma = Alma()
ataque = Ataque((255,255,255), 80, 220, 20, 20, 3, 0, 5)
ataque2 = Ataque('white', 90, 250, 40, 40, 10, 0, 5)
ataque3 = Ataque('red', 150, 150, 30, 30, 0, 0, 0)
artes = pygame.sprite.Group()
artes.add(alma)

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo, itens, ataque, ataque2, ataque3
    vidaAtual = 70
    x = 65
    y = 445
    gameover = False
    musicaFundo = pygame.mixer.music.load('assets/Project147.mp3')
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(-1)
    janela.mudarTela('ações')
    itens = [
        Item('Bolo de Sushi', 'Você recupera 30 de vida'),
        Item('Cuscuz Paulista','brutal'),
        Item('Comida3','sla3'),
        Item('Comida4','sla4'),
        Item('Comida5','sla5'),
        Item('Comida6','sla6'),
        Item('Comida7','sla7'),
        Item('Comida8','sla8'),
        Item('Comida9','sla9'),
    ]
    ataque = Ataque((255,255,255), 80, 220, 20, 20, 3, 0, 5) #o ataque não volta depois do gameover (ajeitar isso depois)
    ataque2 = Ataque('white', 90, 250, 40, 40, 10, 0, 5)
    ataque3 = Ataque('red', 150, 150, 30, 30, 0, 0, 0)
        
def printaItens():
    iy = 0
    ix = 0
    colisaoItens = []
    for item in itens:
        if iy <= 3:
            posicaoItem = (170 + ix * 200, 205 + iy * 35)
            item.colisao = pygame.Rect(posicaoItem[0] - 20, posicaoItem[1] + 10, 50, 10) #isso aqui foi uma das coisas mais absurdas que o gpt me ajudou
            colisaoItens.append(item.colisao)
            janela.escreveTexto(f'{item.nome}', fonteBatalha, (255,255,255), posicaoItem)
            if alma.rect.colliderect(botoes[2].gambiarraMsg):
                botoes[2].mostraMsg = True
            iy += 1
        else:
            iy = 0
            ix += 1
            
def consomeItem(tecla):
    global itemSelecionado, consumiuItem, mostraTransicao, transicaoTempo
    itemSelecionado = None
    consumiuItem = False
    if janela.telaAtual == 'inventário' and tecla == K_z:
        for item in itens:
            if alma.rect.colliderect(item.colisao):
                itemSelecionado = item
                janela.mudarTela('transiçãoItens')
                consumiuItem = True
                transicaoTempo = pygame.time.get_ticks()
                mostraTransicao = True
                clicaItem = pygame.mixer.Sound('assets/sounds/snd_select.wav')
                clicaItem.set_volume(0.4)
                clicaItem.play()
                
while True:
    fps.tick((60))
    pygame.display.update()
    eventos = pygame.event.get()
    confirmaAtaque = None
    for evento in eventos:
        if evento.type == KEYDOWN and janela.telaAtual == 'ações':
            confirmaAtaque = evento.key
            if evento.key == K_RIGHT and not alma.rect.colliderect(botoes[3].botao) and not any(botao.mostraMsg for botao in botoes):
                x += 140
            if evento.key == K_LEFT and not alma.rect.colliderect(botoes[0].botao) and not any(botao.mostraMsg for botao in botoes):
                x -= 140
        
            if evento.key == K_z:
                x = 30
                y = 220
                for botao in botoes:
                    botao.checaClique(evento.key)
                if botoes[0].confirmaAcao(evento.key):
                    botoes[0].confirmaLuta()
                    botoes[0].batalhaAcontece()
                if botoes[1].confirmaAcao(evento.key):
                    botoes[1].confirmaAgir()
                if botoes[2].confirmaAcao(evento.key):
                    botoes[2].confirmaTelaItem()
                if botoes[3].confirmaAcao(evento.key):
                    botoes[3].confirmaPiedade()

            if evento.key == K_x and not any(botao.mirando for botao in botoes):
                for botao in botoes:
                    botao.cancelaAcao()
                x = 65
                y = 450
        if evento.type == KEYDOWN and janela.telaAtual == 'inventário': #A movimentação ainda não está limitada (ajeitar depois)
            if evento.key == K_DOWN:
                y += 35
            if evento.key == K_UP:
                y -= 35
            if evento.key == K_RIGHT:
                x += 200
            if evento.key == K_LEFT:
                x -= 200
            if evento.key == K_z:
                consomeItem(evento.key)
            if evento.key == K_x:
                janela.mudarTela('ações')
                x = 65
                y = 450
        if evento.type == KEYDOWN and janela.telaAtual == 'lutaAcontecendo':
            if evento.key == K_x and ataque.mostrar == False: #isso só vai ficar por enquanto (lembrar de tirar depois)
                janela.mudarTela('ações')
                x = 65
                y = 450
        if evento.type == QUIT:
            pygame.quit()
            exit()
   
    janela.corFundo()
    janela.escreveTexto(f'HP:{vidaAtual}/{vida}', fonte, (255,255,255),(260,385))
    if janela.telaAtual == 'lutaAcontecendo':
        janela.desenhaCaixa((70, 190, 500, 180))
    else:
        janela.desenhaCaixa((10,180,620,180))
        
    almaDesaparece = any(botao.mirando for botao in botoes) or janela.telaAtual == 'transiçãoItens'

    if almaDesaparece == False:
        janela.tela.blit(alma.image, alma.rect)
    alma.update()
            
    for botao in botoes:
        botao.checaAlma()
        botao.desenhaAcoes()
        botao.acoesMensagem(fonteBatalha)
        botao.mirar(confirmaAtaque)
        botao.batalhaAcontece()
    confirmaAtaque = None
        
    if botoes[0].comecaBatalha and janela.telaAtual == 'lutaAcontecendo':
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            velocidade = 2.2
        else:
            velocidade = 3.2
        if teclas[pygame.K_RIGHT]:
            x += 1 * velocidade
        if teclas[pygame.K_LEFT]:
            x -= 1  * velocidade
        if teclas[pygame.K_UP]:
            y -= 1 * velocidade
        if teclas[pygame.K_DOWN]:
            y += 1 * velocidade
        if ataque.mostrar:
            ataque.draw()
            if ataque.contador == 3: #botei isso aqui pra caso o ataque seja resetado pro começo da tela 3 vezes ele parar o ataque e voltar pra tela inicial
                janela.mudarTela('ações')
                janela.atualizaTela()
                x = 65
                y = 450
                botoes[0].naBatalha = False  
                botoes[0].comecaBatalha = False
                ataque.mostrar = False  
                    
            if ataque.atualizar(alma.rect) and ataque.mostrar == False:
                vidaAtual -= 1
                somColisao = pygame.mixer.Sound('assets/sounds/dano.mp3')
                somColisao.set_volume(0.4)
                somColisao.play()
                
        if ataque.mostrar == False or contadorTurno >= 2: #isso ta piscando depois do 1° turno (preocupante)
            janela.escreveTexto("Tomou soft lock né KKKKKKKKKKKK", fonte, (255,255,255),(90, 250))
            janela.escreveTexto("Aperta X pra sair vai", fonte, (255,255,255),(90, 280))
            
    if janela.telaAtual == 'inventário':
        printaItens()
        for item in itens:
            item.checaAlma()
        
    if janela.telaAtual == 'transiçãoItens': #No segundo item usado a tela congela por conta do ataque que também só vai até o primeiro (ajeitar depois)
        janela.escreveTexto(f'Você usou {itemSelecionado.nome}', fonteBatalha, (255,255,255), (90,230))
        janela.escreveTexto(f'{itemSelecionado.descricao}', fonteBatalha, (255,255,255), (90,260))
        itemSelecionado.usar()
        if mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - transicaoTempo > 2000:
                mostraTransicao = False
                botoes[0].comecaBatalha = True
                
    if vidaAtual <= 0:
        janela.mudarTela('gameover')
        tocouGameOver = False
        while janela.telaAtual == 'gameover':
            if not tocouGameOver:
                pygame.mixer.music.fadeout(280)
                gameoverMusica = pygame.mixer.music.load('assets/gameovertheme.mp3')
                pygame.mixer.music.set_volume(0.6)
                pygame.mixer.music.play(-1)
                tocouGameOver = True
                janela.atualizaTela()
            
            janela.corFundo()
            gameoverImg = pygame.image.load('assets/gameover.png')
            janela.tela.blit(gameoverImg, (130,15))
            janela.escreveTexto('Pressione R para reiniciar', fonte, (255,255,255), (50, 400))
            janela.atualizaTela()
                   
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        reiniciar_jogo()
                        
    janela.atualizaTela()
