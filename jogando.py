import pygame
from parametros import *

from sprites_e_classes import *

#########################################################CENÁRIO###################################################
#OBJETOS - ISSO PODE INCLUIR PAREDES E OUTROS
objetos= pygame.sprite.Group() 

#PLATAFORMAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
plataformas = pygame.sprite.Group()
plataforma1 = objeto(100, 400, pygame.transform.rotate(img_plataformas))

plataformas.add(plataforma1)

objetos.add(plataformas)

#ESPINHOS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR)
espinhos = pygame.sprite.Group()
espinho1 = objeto(200,300, pygame.transform.rotate(img_espinhos, 0))

espinhos.add(espinho1)

objetos.add(espinhos)


#MOEDAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
moedas = pygame.sprite.Group()


moeda1 = objeto(23,12, img_moeda)
moedas.add(moeda1)



# Função para reposicionar as moedas
def resetar_moedas(moedas):
    for moeda in moedas:
        moeda.rect.x = moeda.x_original
        moeda.rect.y = moeda.y_original

all_sprites = pygame.sprite.Group()

all_sprites.add(objetos, moedas)


###########################################################JOGO#################################################


def jogando(JANELA):
    cronometro = pygame.time.Clock()

    personagem = personagem()
    all_sprites.add(personagem)

    vidas = 3
    pontos = 0


    DONE = 0
    JOGANDO = 1
    MORRENDO = 2

    keys_down = {}

    pygame.mixer.som_fundo.play(loops=-1)
    estado_do_jogo = JOGANDO
    
    while estado_do_jogo != DONE:
        clock.tick(FPS)



        #EVENTOS

        for event in pygame.event.get():
            #APERTOU NO X DE SAIR:
            if event.type == pygame.QUIT:
                estado_do_jogo = DONE
            
            #MOVIMENTANDO O PERSONAGEM
            if estado_do_jogo == JOGANDO:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # DEPENDENDO DA TECLA E SE ALGUM OUTRO MOVIMENTO JÁ ESTÁ ACONTECENDO
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_d and velocidadey == 0 :
                        personagem.velocidadex -= 8
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_a and velocidadey == 0 :
                        personagem.velocidadex += 8
                    if event.key == pygame.K_UP or event.key == pygame.K_w and velocidadex == 0 :
                        personagem.velocidadey -= 8
                    if event.key == pygame.DOWN or event.key == pygame.K_s and velocidadex == 0 :
                        personagem.velocidadey +=8


        #ROTACIONANDO EM RELAÇÃO AO SEU MOVIMENTO - ***CALIBRAR A VELO DISSO
        if personagem.velocidadey>0 and personagem.rotacao != 180:
            personagem.rotacao += velocidade_de_rotaca_p_frame
        if personagem.velocidadey<0 and personagem.rotacao != 0:
            personagem.rotacao -= velocidade_de_rotaca_p_frame
        if personagem.velocidadex >0 and personagem.rotacao != 270:
            personagem.rotacao +=velocidade_de_rotaca_p_frame
        if personagem.velocidadex<1 and personagem.rotacao != 90:
            personagem.rotacao -= velocidade_de_rotaca_p_frame

        
        all_sprites.update()


        if estado_do_jogo == JOGANDO:

        #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
            colisoes_plataformas = pygame.sprite.spritecollide(personagem, plataformas, False, pygame.sprite.collide_mask)
            if colisoes_plataformas:
                if personagem.velocidadex !=0:
                    personagem.velocidadex -= personagem.velocidadex  # para o jogador
                elif personagem.velocidadey !=0:
                    personagem.velocidadey -= personagem.velocidadey  # para o jogador
                som_caido.play()



        
        
        #COLISÃO COM OS ESPINHOS
            colisoes_espinhos = pygame.sprite.spritecollide(personagem, espinhos, False, pygame.sprite.collide_mask)
            if colisoes_espinhos:        
                som_morrendo.play()
                personagem.kill()
                vidas -= 1
                morte = morrendo(personagem.rect.center)

                all_sprites.add(morte)
                keys_down = {}
                estado_do_jogo = MORRENDO
                hora_da_morte = pygame.time.Clock()
                duracao_da_morte = t_dos_frames_de_morte*len(morte.anim_da_morte) + 400
            elif estado_do_jogo == MORRENDO:
                agora = pygame.time.get_ticks()


                if agora - hora_da_morte > duracao_da_morte:
                    if vidas == 0:
                        estado_do_jogo = DONE
                    else: 
                        estado_do_jogo = JOGANDO
                        personagem = personagem()
                        all_sprites.add(personagem)

                        resetar_moedas(moedas)


        #COLISÃO COM MOEDAS
            colisoes_moedas = pygame.sprite.spritecollide(personagem, moedas, True, pygame.sprite.collide_mask)
            if colisoes_moedas:
                pontos+=50
                som_pegando_moedas.play()

        #GERANDO SAIDAS
        JANELA.fill(PRETO)
        JANELA.blit(img_fundo,(0,0))

        all_sprites.draw(JANELA)

        #PONTUAÇÃO
        perfil_texto = fonte_pontos.render("{:08d}".format(pontos), True, AMARELO)
        texto_rect = perfil_texto.get_rect()
        texto_rect.midtop = (LARGURA_JANELA / 2,  10)
        JANELA.blit(perfil_texto, texto_rect)

        #VIDAS
        perfil_texto = fonte_pontos.render(chr(9829) * vidas, True, VERMELHO)
        texto_rect = perfil_texto.get_rect()
        texto_rect.bottomleft = (10, ALTURA_JANELA - 10)
        JANELA.blit(perfil_texto, texto_rect)


        pygame.display.update()

