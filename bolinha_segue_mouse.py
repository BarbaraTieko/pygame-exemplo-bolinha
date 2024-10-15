# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import math

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Exemplo Bolinha')

# ----- Inicia assets
font = pygame.font.SysFont(None, 30)
text = font.render('Click em qualquer lugar na tela', True, (255, 255, 255))

# ----- Inicia estruturas de dados
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 15

# ===== Loop principal =====
# A bola só começa a se movimentar depor do primeiro click
comeca_movimento = False
#Velocidade inicial da bola
ball_speed_x = 0
ball_speed_y = 0
#Posição inicial da bola
ball_x = 100
ball_y = 150
ACELERACAO = .5
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            comeca_movimento = True

            #Calculando direção da bola
            x = event.pos[0]
            y = event.pos[1]
            
            angulo = math.atan((ball_y - y) / (ball_x - x))

            # altere a foça e veja o que acontece
            forca = 20
            ball_speed_x = math.cos(angulo) * forca
            ball_speed_y = math.sin(angulo) * forca

            # Caso o click seja em uma posição contrária inverte a velocidade
            if ball_x > x:
                ball_speed_x *= (-1)
                ball_speed_y *= (-1)

    # ----- Atualiza estado do jogo
    # Atualizando a posição da bola
    if comeca_movimento:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

    # Caso a bola bata nas paredes, inverte o sentido
    if ball_x > WIDTH or ball_x < 0:
        ball_speed_x *= (-1)
    if ball_y > HEIGHT or ball_y < 0:
        ball_speed_y *= (-1)
    
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(text, (10, 10))
    #Desenhando bola na tela
    pygame.draw.circle(window, (255, 0, 0), (ball_x, ball_y), 10)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

