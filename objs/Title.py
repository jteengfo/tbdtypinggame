import sys
import pygame


class Title:

    def __init__(self, surface):
        # objects in the game
        self.surface = surface
        self.bg_color = pygame.Color('black')
        # window dimension
        self.title_width = self.surface.get_width()
        self.title_height = self.surface.get_height()
        # infinite loop break; transition to game parameters
        self.main_menu_stay = True
        self.close_clicked = False
        # title parameters
        self.tbd_font = pygame.font.Font(None, 100)
        self.tbd_img = self.tbd_font.render('TBD Typing Game', True, pygame.Color('white'))
        self.tbd_pos = [self.title_width / 2 - self.tbd_img.get_width() / 2,
                        self.title_height + self.tbd_img.get_height() / 2]
        # instruction parameters
        self.ins_font = pygame.font.Font(None, 50)
        self.ins_img = self.ins_font.render('Press Enter to start game', True, pygame.Color('white'))
        self.ins_pos = [self.title_width / 2 - self.ins_img.get_width() / 2,
                        self.title_height / 3 + self.ins_img.get_height() / 2]

    def main_execute(self):
        while self.main_menu_stay:
            self.handle_events()
            self.draw_title()
            self.tbd_move()

            self.draw_instruction()

            self.update()

    def draw_title(self):
        # this method draws the title screen

        tbd_img = self.tbd_img
        self.surface.fill((0, 0, 0))
        self.surface.blit(tbd_img, self.tbd_pos)

    def draw_instruction(self):
        # this method draws the title screen

        ins_img = self.ins_img
        # self.surface.fill((0, 0, 0))

        self.surface.blit(ins_img, self.ins_pos)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.main_menu_stay = False

    def update(self):
        #
        pygame.display.update()

    def tbd_move(self):
        # screen_width = self.surface.get_width()
        screen_height = self.surface.get_height()

        tbd_velocity = 1 / 4

        if self.tbd_pos[1] >= screen_height / 2:
            self.tbd_pos[1] -= tbd_velocity
