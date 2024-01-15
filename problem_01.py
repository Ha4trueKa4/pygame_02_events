import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    v = 10  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((0, 0, 255))
    drawing = None
    pos = None
    r = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 255))
                pos = event.pos
                drawing = True
                r = 0
        if drawing:
            pygame.draw.circle(screen, pygame.Color('yellow'), pos, r)
            r += v / 1000
        pygame.display.flip()
    pygame.quit()
