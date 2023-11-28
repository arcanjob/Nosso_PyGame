import pygame
import random
from os import path
from variaveis_e_funcoes import *
velocidade_no_eixo_x = 10

pygame.init()
pygame.mixer.init()

janela = pygame.display.set_mode((1350, 680))

#ESTABELECER OS SONS

def bases_carregando(img_dir):
    assets = {}
    assets[bonequinho] = pygame.image.load(path.join('imagens_e_sons/imagens/Walk_(1).png')).convert_alpha()
    assets[B] = pygame.image.load(path.join('imagens_e_sons/imagens/plataforma.png')).convert()
    return assets


def tela_do_jogo(janela):
    pygame.mixer.music.load('imagens_e_sons/sons/som_de_fundo.mp3') #Fonte: https://youtu.be/dDOfzfifwGE?si=GfIuDBJCHU0t26uN
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    
    clock = pygame.time.Clock()
    assets = bases_carregando(img_dir)

    todos_os_sprites= pygame.sprite.Group()
    
    piso_parede = pygame.sprite.Group()

    player = Player(assets[bonequinho], 12, 2, piso_parede)

    for filas in range(len(MAPA)):
        for colunas in range(len(MAPA[filas])):
            tile_type = MAPA[filas][colunas]
            if tile_type == B:
                tile = Tile(assets[tile_type], filas, colunas)
                todos_os_sprites.add(tile)
                piso_parede.add(tile)
          
                
    
    todos_os_sprites.add(player)

    jogando = 0
    DONE = 1

  
    estado_do_jogo = jogando
    while estado_do_jogo != DONE:

        clock.tick(FPS)
    
        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                estado_do_jogo = DONE

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.speedx -= velocidade_no_eixo_x
                elif event.key == pygame.K_RIGHT:
                    player.speedx += velocidade_no_eixo_x
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT:
                    player.speedx += velocidade_no_eixo_x
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= velocidade_no_eixo_x

        #
        todos_os_sprites.update()
        img_fundo = pygame.image.load('imagens_e_sons/imagens/Fundo_jogo.jpg').convert_alpha() #O FUNDO SERÁ UMA ANIMAÇÃO
        img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataforma.png').convert_alpha()
        
        janela.blit(img_fundo, (0,0))
        todos_os_sprites.draw(janela)

        
        pygame.display.flip()





pygame.display.set_caption(TITULO)

try:
    tela_do_jogo(janela)
    #tela_do_jogo(janela)
finally:
    pygame.quit()