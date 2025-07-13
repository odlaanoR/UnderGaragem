import pygame
from pygame.locals import *
from modulos.janelas import janela
from modulos.acoes import *
from modulos.item import *
from modulos.alma import alma
from modulos.ataques import *
import modulos.funcoes as func
import modulos.constantes as cos
from sys import exit
                
while True:
    cos.fps.tick((60))
    pygame.display.update()
    eventos = pygame.event.get()
    confirmaAtaque = None
    for evento in eventos:
        if evento.type == KEYDOWN and janela.telaAtual == 'ações':
            confirmaAtaque = evento.key
            if evento.key == K_RIGHT and not alma.rect.colliderect(botoes[3].botao) and not any(botao.mostraMsg for botao in botoes):
                cos.x += 140
            if evento.key == K_LEFT and not alma.rect.colliderect(botoes[0].botao) and not any(botao.mostraMsg for botao in botoes):
                cos.x -= 140
        
            if evento.key == K_z:
                cos.x = 30
                cos.y = 220
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
                cos.x = 65
                cos.y = 450
        if evento.type == KEYDOWN and janela.telaAtual == 'inventário': #A movimentação ainda não está limitada (ajeitar depois)
            if evento.key == K_DOWN:
                cos.y += 35
            if evento.key == K_UP:
                cos.y -= 35
            if evento.key == K_RIGHT:
                cos.x += 200
            if evento.key == K_LEFT:
                cos.x -= 200
            if evento.key == K_z:
                func.consomeItem(evento.key)
            if evento.key == K_x:
                janela.mudarTela('ações')
                cos.x = 65
                cos.y = 450
        if evento.type == KEYDOWN and janela.telaAtual == 'lutaAcontecendo':
            if evento.key == K_e and ataque.mostrar == False: #isso só vai ficar por enquanto (lembrar de tirar depois)
                janela.mudarTela('ações')
                cos.x = 65
                cos.y = 450
        if evento.type == QUIT:
            pygame.quit()
            exit()
   
    janela.corFundo()
    janela.escreveTexto(f'HP:{cos.vidaAtual}/{cos.vida}', cos.fonte, (255,255,255),(260,385))
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
        botao.acoesMensagem(cos.fonteBatalha)
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
            cos.x += 1 * velocidade
        if teclas[pygame.K_LEFT]:
            cos.x -= 1  * velocidade
        if teclas[pygame.K_UP]:
            cos.y -= 1 * velocidade
        if teclas[pygame.K_DOWN]:
            cos.y += 1 * velocidade
        if ataque.mostrar:
            ataque.draw()
            if ataque.contador == 3: #botei isso aqui pra caso o ataque seja resetado pro começo da tela 3 vezes ele parar o ataque e voltar pra tela inicial
                janela.mudarTela('ações')
                janela.atualizaTela()
                cos.x = 65
                cos.y = 450
                botoes[0].naBatalha = False  
                botoes[0].comecaBatalha = False
                ataque.mostrar = False  
                    
            if ataque.atualizar(alma.rect) and ataque.mostrar == False:
                cos.vidaAtual -= 1
                somColisao = pygame.mixer.Sound('assets/sounds/dano.mp3')
                somColisao.set_volume(0.4)
                somColisao.play()
                
        if ataque.mostrar == False or contadorTurno >= 2: #isso ta piscando depois do 1° turno (preocupante)
            janela.escreveTexto("Tomou soft lock né KKKKKKKKKKKK", cos.fonte, (255,255,255),(90, 250))
            janela.escreveTexto("Aperta E pra sair vai", cos.fonte, (255,255,255),(90, 280))
            
    if janela.telaAtual == 'inventário':
        func.printaItens()
        for item in itens:
            item.checaAlma()
        
    if janela.telaAtual == 'transiçãoItens': #No segundo item usado a tela congela por conta do ataque que também só vai até o primeiro (ajeitar depois)
        janela.escreveTexto(f'Você usou {func.itemSelecionado.nome}', cos.fonteBatalha, (255,255,255), (90,230))
        janela.escreveTexto(f'{func.itemSelecionado.descricao}', cos.fonteBatalha, (255,255,255), (90,260))
        func.itemSelecionado.usar()
        if func.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - func.transicaoTempo > 2000:
                mostraTransicao = False
                botoes[0].comecaBatalha = True
                
    if cos.vidaAtual <= 0:
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
            janela.escreveTexto('Pressione R para reiniciar', cos.fonte, (255,255,255), (50, 400))
            janela.atualizaTela()
                   
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        func.reiniciar_jogo()
                        
    janela.atualizaTela()
