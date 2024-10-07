import pygame

WIDTH = 600
HEIGHT = 600


def inicializa():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Jogo da Barbara')

    estado = {
        "posicao": [WIDTH/2, HEIGHT/2],
        "comeca_movimento": False,
        "velocidade": [200, 200],
        "t0": 0,
        "gravidade": 98,
        "resistencia": 0.7,
        "raio": 10
    }
    return window, estado


def recebe_eventos(estado):
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Se apertar qualquer tecla, começa o movimento
            estado["comeca_movimento"] = True
            estado['t0'] = pygame.time.get_ticks()

    if estado["comeca_movimento"]:

        t1 = pygame.time.get_ticks()
        dt = (t1 - estado['t0'])/1000 # Calculando o tempo (delta t) que passou em segundos

        # aplicando gravidade
        estado['velocidade'][1] += estado['gravidade'] * dt

        # Calculando a nova posição
        estado['posicao'][0] = estado['posicao'][0] + estado['velocidade'][0] * dt
        estado['posicao'][1] = estado['posicao'][1] + estado['velocidade'][1] * dt

        # Atualizando o t0 com o tempo atual
        estado['t0'] = t1

    # Verifica se está saindo da tela pela parede da direita
    if estado['posicao'][0] + estado["raio"] > WIDTH:
        estado['velocidade'][0] *= (-1) # Inverte a velocidade
        estado['velocidade'][0] *= estado['resistencia'] # Aplica a resistência
        estado['posicao'][0] = WIDTH - estado["raio"] # Corrige a posição

    # Verifica se está saindo da tela pela parede da esquerda
    if estado['posicao'][0] - estado["raio"] < 0:
        estado['velocidade'][0] *= (-1) # Inverte a velocidade
        estado['velocidade'][0] *= estado['resistencia'] # Aplica a resistência
        estado['posicao'][0] = estado["raio"] # Corrige a posição

    # Verifica se está saindo da tela pelo chão
    if estado['posicao'][1] + estado["raio"] > HEIGHT:
        estado['velocidade'][1] *= (-1) # Inverte a velocidade
        estado['velocidade'][1] *= estado['resistencia'] # Aplica a resistência
        estado['posicao'][1] = HEIGHT - estado["raio"] # Corrige a posição

    # Verifica se está saindo da tela pelo teto
    if estado['posicao'][1] - estado["raio"] < 0:
        estado['velocidade'][1] *= (-1) # Inverte a velocidade
        estado['velocidade'][1] *= estado['resistencia'] # Aplica a resistência
        estado['posicao'][1] = estado["raio"] # Corrige a posição

    return game


def desenha(window, estado):
    window.fill((0, 0, 0)) # Preenche a tela de preto

    pygame.draw.circle(window, (255, 0, 0), (estado['posicao'][0], estado['posicao'][1]), estado["raio"])
    pygame.display.update()  # Mostra o novo frame para o jogador


def game_loop(window, estado):
    # ===== Loop principal =====
    while recebe_eventos(estado):
        # ----- Gera saídas
        desenha(window, estado)


# Inicializa o jogo
janela, estado = inicializa()
game_loop(janela, estado)
