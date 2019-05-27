import pygame
import GUI.pygame_textinput as pygame_textinput

from Swiat import *

import random

pygame.init()
# Create TextInput-object
textinput = pygame_textinput.TextInput()


clock = pygame.time.Clock()


class Game:
    def __init__(self, window_size):
        self.window_size = window_size
        self.screen = pygame.display.set_mode(window_size)

        self.width = window_size[0]
        self.height = window_size[1]

        self.color = [pygame.Color('white'), pygame.Color('black'),
                      pygame.Color('red'), pygame.Color('blue'), pygame.Color('grey')]

        self.game_started = False
        self.world_width = 0
        self.world_height = 0

        self.border_size = 120
        self.cell_size = 30
        self.y_draw_delta = 5

        self.width_x = 0
        self.height_y = 0

        # buttons
        self.but_x = 10
        self.but_y = 10
        self.but_w = 100
        self.but_h = 35

        self.next_tour_button = pygame.Rect(self.but_x, self.but_y, self.but_w, self.but_h)
        self.save_game_button = pygame.Rect(self.but_x, self.but_y + self.but_h + 5, self.but_w, self.but_h)
        self.komentator_button = pygame.Rect(self.but_x, self.but_y + (self.but_h + 5)*2, self.but_w, self.but_h)
        self.start_new_game_button = pygame.Rect(self.but_x, self.but_y + (self.but_h + 5)*3, self.but_w, self.but_h)

        self.buttons = []
        self.buttons.append(self.next_tour_button)
        self.buttons.append(self.save_game_button)
        self.buttons.append(self.komentator_button)
        self.buttons.append(self.start_new_game_button)

        # text for buttons

        ft_font = pygame.font.Font('Blogger_Sans.otf', 18)

        self.next_tour_surf = ft_font.render("Next tour", 1, self.color[1])
        self.save_game_surf = ft_font.render("Save game", 1, self.color[1])
        self.komentator_surf = ft_font.render("Commentator", 1, self.color[1])
        self.start_new_game_surf = ft_font.render("New Game", 1, self.color[1])

        self.buttons_text = []
        self.buttons_text.append(self.next_tour_surf)
        self.buttons_text.append(self.save_game_surf)
        self.buttons_text.append(self.komentator_surf)
        self.buttons_text.append(self.start_new_game_surf)

        self.swiat = None

        self.go()

    def transform_size(self, data):
        try:
            self.world_width = int(data.split(" ")[0])
            self.world_height = int(data.split(" ")[1])

            if self.world_width > 0 and self.world_height > 0:
                self.swiat = Swiat(self.world_width, self.world_height)
                self.game_started = True
                self.screen = pygame.display.set_mode([self.world_width * 50, self.world_height * 45])

                self.width_x = self.world_width * self.cell_size + self.border_size
                self.height_y = self.world_height * self.cell_size

        except ValueError:
            print("It is not an integer")

    def draw_grid(self):
        for i in range(self.y_draw_delta, self.height_y + self.y_draw_delta + 1, self.cell_size):
            pygame.draw.line(self.screen, self.color[2], (self.border_size, i), (self.width_x, i))

        for i in range(self.border_size, self.width_x + self.y_draw_delta + 1, self.cell_size):
            pygame.draw.line(self.screen, self.color[2], (i, self.y_draw_delta), (i, self.height_y + self.y_draw_delta))

    def draw_animals(self):
        for i in range(0, self.swiat.height):
            for k in range(0, self.swiat.width):
                if self.swiat.moje_organizmy[i][k] is not None:
                    pygame.draw.rect(self.screen, self.swiat.moje_organizmy[i][k].color,
                                     pygame.Rect(self.border_size + k * self.cell_size,
                                                 self.y_draw_delta + 1 + i * self.cell_size,
                                                 self.cell_size, self.cell_size))

    def go(self):
        while True:
            self.screen.fill((225, 225, 225))

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_started:
                        if self.next_tour_button.collidepoint(pygame.mouse.get_pos()):
                            self.swiat.wykonaj_ture()
                            # print("NEW TOUR")
                elif event.type == pygame.KEYDOWN:
                    if self.game_started:
                        #           3    4      2     1
                        # direction (UP, DOWN , LEFT, RIGHT)
                        if event.key == pygame.K_UP:
                            self.swiat.set_czlowiek_direction_global(3)
                        elif event.key == pygame.K_DOWN:
                            self.swiat.set_czlowiek_direction_global(4)
                        elif event.key == pygame.K_LEFT:
                            self.swiat.set_czlowiek_direction_global(2)
                        elif event.key == pygame.K_RIGHT:
                            self.swiat.set_czlowiek_direction_global(1)


            # Feed textinput with events every frame
            if textinput.update(events):
                self.transform_size(textinput.get_text())

            if not self.game_started:
                self.screen.blit(textinput.get_surface(), (10, 10))
            else:
                for button in self.buttons:
                    pygame.draw.rect(self.screen, self.color[4], button, 0)

                for i in range(0, len(self.buttons_text)):
                    self.screen.blit(self.buttons_text[i], (10, i * (self.but_h + 5) + self.but_y))

                self.draw_grid()
                self.draw_animals()

            pygame.display.update()
            clock.tick(30)


test = Game([200, 200])
