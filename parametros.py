import pygame
from math import *
import os

pygame.mixer.init()
pygame.init()

FPS = 60 # Frames por segundo

velocidade_de_rotaca_p_frame = radians(1) # do personagem, ao cair

JANELA = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Hello World!')

####TAMANHOS
#JANELA
LARGURA_JANELA = 1000 # Largura da tela - A DEFINIR
ALTURA_JANELA =  600# Altura da tela - A DEFINIR

#FUNDO
LARGURA_FUNDO = LARGURA_JANELA
ALTURA_FUNDO = LARGURA_JANELA 

#ESPINHOS
LARGURA_ESPINHOS = 30 #A DEFINIR
ALTURA_ESPINHOS = 20 #A DEFINIR

#JOGADOR
ALTURA_JOGADOR= 20 #A DEFINIR
LARGURA_JOGADOR = 7 #A DEFINIR

#PLATAFORMA
ALTURA_PLATAFORMA = 20 #A DEFINIR
LARGURA_PLATAFORMA = 20 #A DEFINIR

#MOEDA
ALTURA_MOEDA = 5
LARGURA_MOEDA = 5

#IMAGEM DA TELA INCIAL
LARGURA_INICIO = LARGURA_JANELA
ALTURA_INICIO = ALTURA_JANELA

#IMAGEM DA TELA FINAL
LARGURA_FINAL = LARGURA_JANELA
ALTURA_FINAL = ALTURA_JANELA


#LINHA DE CHEGADA
ALTURA_CHEGADA = 20
LARGURA_CHEGADA = 10

#VITORIA
ALTURA_VITORIA = ALTURA_JANELA
LARGURA_VITORIA = LARGURA_JANELA

#VITORIA FINAL
ALTURA_VITORIA_FINAL = ALTURA_JANELA
LARGURA_VITORIA_FINAL = LARGURA_JANELA

#CORAÇÕES
LARGURA_CORACAO = 10
ALTURA_CORACAO = 10

# Estabelecer as figuras
img_personagem = pygame.image.load('imagens_e_sons/imagens/garoto/garoto_parado/Idle (1).png').convert_alpha()
img_fundo = pygame.image.load('imagens_e_sons/fundo/Fundo_jogo.jpg').convert_alpha()
img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataforma.png').convert_alpha()
img_moeda = pygame.image.load('imagens_e_sons/imagens/moeda.png').convert_alpha()
img_espinhos = pygame.image.load('imagens_e_sons/imagens/espinho.png').convert_alpha()
img_coracoes = pygame.image.load('imagens_e_sons/imagens/coracao.png').convert_alpha()   #de vida faltante
img_inicio = pygame.image.load('imagens_e_sons/imagens/inicio.png').convert_alpha() #tela inicial 
img_fim = pygame.image.load('imagens_e_sons/imagens/fim.png').convert_alpha()    #tela do game over
img_chegada = pygame.image.load('imagens_e_sons/imagens/portal.png').convert_alpha() #linha de chegada/porta/portal ... = objetivo final da fase
img_vitoria = pygame.image.load('imagens_e_sons/imagens/vitoria.webp').convert_alpha()    #tela do parabens, voce passou de fase
img_vitoria_final = pygame.image.load('imagens_e_sons/imagens/vitoria.webp').convert_alpha()    #tela de parabens, voce concluiu o jogo

#REDIMENSIONANDO AS FIGURAS
#redimensionando as imagens
#image = pygame.transform.scale(image, (125, 166)) para obter uma nova imagem de 125 X 166 pixels.
img_fundo = pygame.transform.scale(img_fundo, (LARGURA_FUNDO, ALTURA_FUNDO))
img_personagem = pygame.transform.scale(img_personagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
img_plataformas = pygame.transform.scale(img_plataformas, (LARGURA_PLATAFORMA, ALTURA_PLATAFORMA))
img_moeda = pygame.transform.scale(img_moeda, (LARGURA_MOEDA, ALTURA_MOEDA))
img_espinhos = pygame.transform.scale(img_espinhos, (LARGURA_ESPINHOS, ALTURA_ESPINHOS))
img_inicio =  pygame.transform.scale(img_inicio, (LARGURA_INICIO, ALTURA_INICIO))
img_fim =  pygame.transform.scale(img_fim, (LARGURA_FINAL, ALTURA_FINAL))
img_chegada = pygame.transform.scale(img_chegada, (LARGURA_CHEGADA, ALTURA_CHEGADA))
img_vitoria = pygame.transform.scale(img_vitoria, (LARGURA_VITORIA, ALTURA_VITORIA))
img_vitoria_final = pygame.transform.scale(img_vitoria_final, (LARGURA_VITORIA_FINAL, ALTURA_VITORIA_FINAL))
img_coracoes = pygame.transform.scale(img_coracoes, (LARGURA_CORACAO, ALTURA_CORACAO))

#TEXTO
fonte_pontos =  pygame.font.Font('imagens_e_sons/imagens/pontos.ttf', 28)


#ESTABELECER OS SONS
som_fundo = pygame.mixer.music.load('imagens_e_sons/sons/som_de_fundo.mp3') #Fonte: https://youtu.be/dDOfzfifwGE?si=GfIuDBJCHU0t26uN
pygame.mixer.music.set_volume(0.4)

som_caindo = pygame.mixer.Sound('imagens_e_sons/sons/caindo.mp3')

#Falta esses aqui
som_pegando_moedas = pygame.mixer.Sound('imagens_e_sons/sons/coin.mp3') #Fonte: https://pixabay.com/pt/sound-effects/search/game%20coin/
som_caido = pygame.mixer.music.load('imagens_e_sons/sons/caindo.mp3') #quando o cara cai no chao, de fato
som_morrendo = pygame.mixer.music.load('imagens_e_sons/sons/morrendo.mp3') #Fonte: https://pixabay.com/pt/sound-effects/search/dead/
som_game_over =pygame.mixer.music.load('imagens_e_sons/sons/game_over.mp3') #acaba as vidas #Fonte: https://pixabay.com/pt/sound-effects/search/game%20over/
#som_perdendo_vida =  pygame.mixer.music.load('imagens_e_sons/sons/perdendo_vida.ogg') 
som_vitoria =  pygame.mixer.music.load('imagens_e_sons/sons/vitoria.mp3') #quando passa de fase #Fonte: https://pixabay.com/pt/sound-effects/search/win/

#POSIÇÃO INICIAL DO JOGADOR - A DEFINIR
x_meio_inicial_do_personagem = 32
y_peh_inicial_do_personagem = 23


# CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)



#ORIENTAÇÕES
de_peh = radians(0)
de_ponta_cabeca = radians(180)
virado_para_a_esquerda = radians(90)
virado_para_a_direita = radians(270)



# Estados para controle do fluxo da aplicação
GAME_OVER  = 0
JOGANDO = 1
MORRENDO = 2
DONE = 3
INICIO = 4
VITORIA = 5
VITORIA_FINAL = 6


####################******************ANIMAÇÕES - PRO GRAND FINALE
anim_morrendo = []
morrendo = 0
arquivo_morrendo = 'imagens_e_sons/imagens/garoto/garoto_morrendo'
for i in range(15):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(arquivo_morrendo, f'Dead ({i+1}).png')
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        anim_morrendo.append(img)

parado = 1
anim_parado = []
arquivo_parado = 'imagens_e_sons/imagens/garoto/garoto_parado'
for i in range(15):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(arquivo_parado, f'Idle ({i+1}).png')
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        anim_parado.append(img)

pulando= 2
anim_pulando = []
arquivo_pulando = 'imagens_e_sons/imagens/garoto/garoto_pulando'
for i in range(15):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(arquivo_pulando, f'Jump ({i+1}).png')
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        anim_parado.append(img)




#########################################################CENÁRIO FASE 1 ###################################################

import sprites_e_classes
F1 = {}

#OBJETOS - ISSO PODE INCLUIR PAREDES E OUTROS
F1['objetos']= pygame.sprite.Group() 


#PLATAFORMAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
F1['plataformas'] = pygame.sprite.Group()
F1['plataforma1'] = objeto(100, 400, pygame.transform.rotate(img_plataformas, 0))

F1['plataformas'].add(F1['plataforma1'])

F1['objetos'].add(F1['plataformas'])

#ESPINHOS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR)
F1['espinhos'] = pygame.sprite.Group()
F1['espinho1'] = objeto(200,300, pygame.transform.rotate(img_espinhos, 0))

F1['espinhos'].add(F1['espinho1'])

F1['objetos'].add(F1['espinhos'])


#MOEDAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
F1['moedas'] = pygame.sprite.Group()


F1['moeda1'] = objeto(23,12, img_moeda)
F1['moedas'].add(moeda1)

#CHEGADA
F1['chegada'] = objeto(90, 0, img_chegada)

# Função para reposicionar as moedas
def resetar_moedas(moedas):
    for moeda in moedas:
        moeda.rect.x = moeda.x_original
        moeda.rect.y = moeda.y_original

F1['all_sprites'] = pygame.sprite.Group()

F1['all_sprites'].add(F1['objetos'], F1['moedas'],F1['chegada'])


#########################################################CENÁRIO FASE 2 ###################################################


F2 = {}

#OBJETOS - ISSO PODE INCLUIR PAREDES E OUTROS
F2['objetos']= pygame.sprite.Group() 

#PLATAFORMAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
F2['plataformas'] = pygame.sprite.Group()
F2['plataforma1'] = objeto(100, 400, pygame.transform.rotate(img_plataformas))

F2['plataformas'].add(F2['plataforma1'])

F2['objetos'].add(F2['plataformas'])

#ESPINHOS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR)
F2['espinhos'] = pygame.sprite.Group()
F2['espinho1'] = objeto(200,300, pygame.transform.rotate(img_espinhos, 0))

F2['espinhos'].add(F2['espinho1'])

F2['objetos'].add(F2['espinhos'])


#MOEDAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
F2['moedas'] = pygame.sprite.Group()


F2['moeda1'] = objeto(23,12, img_moeda)
F2['moedas'].add(moeda1)

#CHEGADA
F2['chegada'] = objeto(90, 0, img_chegada)

# Função para reposicionar as moedas
def resetar_moedas(moedas):
    for moeda in moedas:
        moeda.rect.x = moeda.x_original
        moeda.rect.y = moeda.y_original

F2['all_sprites'] = pygame.sprite.Group()

F2['all_sprites'].add(F2['objetos'], F2['moedas'],F2['chegada'])


#########################################################CENÁRIO FASE 3 ###################################################


F3 = {}

#OBJETOS - ISSO PODE INCLUIR PAREDES E OUTROS
F3['objetos']= pygame.sprite.Group() 

#PLATAFORMAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
F3['plataformas'] = pygame.sprite.Group()
F3['plataforma1'] = objeto(100, 400, pygame.transform.rotate(img_plataformas))

F3['plataformas'].add(F3['plataforma1'])

F3['objetos'].add(F3['plataformas'])

#ESPINHOS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR)
F3['espinhos'] = pygame.sprite.Group()
F3['espinho1'] = objeto(200,300, pygame.transform.rotate(img_espinhos, 0))

F3['espinhos'].add(F3['espinho1'])

F3['objetos'].add(F3['espinhos'])


#MOEDAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
F3['moedas'] = pygame.sprite.Group()


F3['moeda1'] = objeto(23,12, img_moeda)
F3['moedas'].add(moeda1)

#CHEGADA
F3['chegada'] = objeto(90, 0, img_chegada)

# Função para reposicionar as moedas
def resetar_moedas(moedas):
    for moeda in moedas:
        moeda.rect.x = moeda.x_original
        moeda.rect.y = moeda.y_original

F3['all_sprites'] = pygame.sprite.Group()

F3['all_sprites'].add(F3['objetos'], F3['moedas'],F3['chegada'])
