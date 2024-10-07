import pygame
from constantes import WIDTH, HEIGHT
from Bolinha import Bolinha

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Jogo da Barbara')

    b1 = Bolinha(WIDTH/2, HEIGHT/2, (255, 0, 0), 10, 200, 200)
    b2 = Bolinha(70, 70, (0, 255, 0), 20, 100, 300)

    estado = {
        "t0": 0,
        "gravidade": 98,
        "resistencia": 0.7,
        "bolinhas": [b1, b2]
    }
    return window, estado


def recebe_eventos(estado):
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    for bolinha in estado["bolinhas"]:
        bolinha.atualiza()


    return game


def desenha(window, estado):
    window.fill((0, 0, 0))  # Preenche a tela de preto

    for bolinha in estado["bolinhas"]:
        bolinha.desenha(window)

    pygame.display.update()  # Mostra o novo frame para o jogador


def game_loop(window, estado):
    # ===== Loop principal =====
    while recebe_eventos(estado):
        # ----- Gera saídas
        desenha(window, estado)


# Inicializa o jogo
janela, estado = inicializa()
game_loop(janela, estado)
