import pygame

pygame.init()


class AddOrganismByMouse:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 300))
        self.go()

    def go(self):
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()
