import pygame
from constantes import WIDTH, HEIGHT

class Bolinha:
    def __init__(self, x, y, cor, raio, vel_x, vel_y):
        self.x = x
        self.y = y
        self.cor = cor
        self.r = raio
        self.velocidade_x = vel_x
        self.velocidade_y = vel_y
        self.t0 = 0

    def desenha(self, window):
        pygame.draw.circle(window, self.cor, (self.x, self.y), self.r)

    def atualiza(self):
        t1 = pygame.time.get_ticks()
        dt = (t1 - self.t0)/1000
        self.t0 = t1

        self.x += self.velocidade_x * dt
        self.y += self.velocidade_y * dt

        if self.x + self.r > WIDTH:
            self.velocidade_x *= -1
            self.x = WIDTH - self.r
        if self.x - self.r < 0:
            self.velocidade_x *= -1
            self.x = self.r

        if self.y + self.r > HEIGHT:
            self.velocidade_y *= -1
            self.y = HEIGHT - self.r
        if self.y - self.r < 0:
            self.velocidade_y *= -1
            self.y = self.r
