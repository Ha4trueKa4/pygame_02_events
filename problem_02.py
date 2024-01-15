import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))

    class Circle:
        def __init__(self, x_pos, y_pos):
            self.r = 10
            self.color = pygame.Color('white')
            self.vx = -100
            self.vy = -100
            self.x_pos = x_pos
            self.y_pos = y_pos
            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.r)

        def update(self):

            if self.x_pos - self.r <= 0 or self.x_pos + self.r >= width:
                self.vx = -self.vx
            if self.y_pos - self.r <= 0 or self.y_pos + self.r >= height:
                self.vy = -self.vy
            self.x_pos += self.vx / 1000
            self.y_pos += self.vy / 1000
            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.r)

    balls = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                circle = Circle(*pos)
                balls.append(circle)

        screen.fill((0, 0, 0))
        for i in balls:
            i.update()
        pygame.display.flip()
    pygame.quit()
