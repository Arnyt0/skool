import pygame
import random

sirka = 800
vyska = 800
okno = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("Hviezdne lietanie")
pocet_hviezd = 300
hviezdy = []

for i in range(pocet_hviezd):
    x = random.uniform(-sirka, sirka)
    y = random.uniform(-vyska, vyska)
    z = random.uniform(1, sirka)
    hviezdy.append([x, y, z])

bezi = True
hodiny = pygame.time.Clock()

while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

    okno.fill((0, 0, 0))
    stredu_x = sirka // 2
    stredu_y = vyska // 2

    mouse_x, _ = pygame.mouse.get_pos()
    rychlost = 2 + (mouse_x / sirka) * 18

    for hviezda in hviezdy:
        hviezda[2] -= rychlost
        if hviezda[2] < 1:
            hviezda[0] = random.uniform(-sirka, sirka)
            hviezda[1] = random.uniform(-vyska, vyska)
            hviezda[2] = sirka
        sx = int(hviezda[0] / hviezda[2] * sirka + stredu_x)
        sy = int(hviezda[1] / hviezda[2] * vyska + stredu_y)
        velkost = int((sirka - hviezda[2]) / sirka * 8)

        pygame.draw.circle(okno, (255, 255, 255), (sx, sy), velkost)

    pygame.display.flip()
    hodiny.tick(60)
pygame.quit()
