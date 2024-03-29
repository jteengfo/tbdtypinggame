# This is the main python file consisting the version 1 of the typing game
#
#
#
# VERSION 1:
# a window appears 1280 x 720
# white ball appears in the center
# an orange ball appears in a fixed random spot
# a word 'python' is drawn on top of the orange ball
# when the word is typed -- the orange ball disappears
#


from objs.Space import *
from objs.Title import *


# import pygame
# import random


def main():
    # initialize all pygame modules
    pygame.init()
    pygame.font.init()
    # set window of certain width and height
    pygame.display.set_mode((1280, 720))
    # create a title in the window, "TBD Typing Game"
    pygame.display.set_caption("TBD Typing Game")
    # create a surface
    a_surface = pygame.display.get_surface()
    # create a main menu
    main_menu = Title(a_surface)
    # create an object
    game = Game(a_surface)

    # main
    main_menu.main_execute()
    while game.play():
        game.play()
    # create a game over screen
    gameover = Endgame(game.get_score(), a_surface)
    gameover.endgame_execute()


class Endgame:

    def __init__(self, score, surface):
        # objects in the game
        self.surface = surface
        self.bg_color = pygame.Color('black')
        # window dimension
        self.title_width = self.surface.get_width()
        self.title_height = self.surface.get_height()
        # infinite loop break; transition to game parameters
        self.main_menu_stay = True
        self.close_clicked = False
        # score parameters
        game = Game(self.surface)
        self.score_value = score
        self.score_font = pygame.font.Font(None, 50)
        self.score_img = self.score_font.render('Your Score: ' + str(self.score_value), True, pygame.Color('white'))
        self.score_pos = [(self.title_width / 2 - self.score_img.get_width() / 2) - 10,
                          (self.title_height / 3 + self.score_img.get_height() / 3) + 75]

        # endgame parameters
        self.ins_font = pygame.font.Font(None, 50)
        self.endgame_img = self.ins_font.render('Game Over', True, pygame.Color('white'))
        self.endgame_pos = [self.title_width / 2 - self.endgame_img.get_width() / 2,
                            self.title_height / 3 + self.endgame_img.get_height() / 2]


    def endgame_execute(self):
        while self.main_menu_stay:
            self.handle_events()
            self.draw_score()
            # self.tbd_move()

            self.draw_endgame()

            self.update()

    def draw_score(self):
        # this method draws the title screen

        score_img = self.score_img
        self.surface.fill((0, 0, 0))
        self.surface.blit(score_img, self.score_pos)

    def draw_endgame(self):
        # this method draws the title screen

        endgame_img = self.endgame_img
        # self.surface.fill((0, 0, 0))

        self.surface.blit(endgame_img, self.endgame_pos)

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

    # def tbd_move(self):
    #     # screen_width = self.surface.get_width()
    #     screen_height = self.surface.get_height()
    #
    #     tbd_velocity = 1 / 4
    #
    #     if self.tbd_pos[1] >= screen_height / 2:
    #         self.tbd_pos[1] -= tbd_velocity


class Game:

    def __init__(self, surface):
        self.health = 10
        self.max_health = 10

        self.score = 0

        # objects in the game
        self.close_clicked = False
        self.surface = surface
        self.bg_color = pygame.Color('black')
        # parameters to handle events
        self.closed_clicked = False
        self.continue_game = True
        # FPS the game is gonna run to
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        # earth object
        self.earth = Space(True, self.surface)
        self.asteroids = []
        self.asteroids.append(Space(False, self.surface))
        self.answers = []
        self.answers.append(self.asteroids[0].get_word())
        # player input objects
        self.white_rect_pos = (320, 670)
        self.white_rect_size = (640, 50)

        self.black_rect_pos = (325, 675)
        self.black_rect_size = (630, 40)

        player_rect_white = (
            self.white_rect_pos[0], self.white_rect_pos[1], self.white_rect_size[0], self.white_rect_size[1])
        player_rect_black = (
            self.black_rect_pos[0], self.black_rect_pos[1], self.black_rect_size[0], self.black_rect_size[1])
        self.rectangle_white = pygame.Rect(player_rect_white)
        self.rectangle_black = pygame.Rect(player_rect_black)
        self.player_input = ""

    def handle_events(self):
        # method that handles event by user that changes the state of the game
        # self is the game whose events will be handled
        transparent_green = (0, 255, 0, 100)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.player_input = self.player_input.lower()
                    if self.player_input in self.answers:
                        print(True)
                        for i in range(len(self.asteroids)):
                            if self.asteroids[i].get_word() == self.player_input:
                                self.answers.remove(self.player_input)

                                self.update_score()
                                self.add_obstacle()
                                self.surface.fill(transparent_green)
                                pygame.display.update()
                                self.asteroids[i] = Space(False, self.surface)
                                self.answers.append(self.asteroids[i].get_word())
                    else:
                        print('try again')
                    self.player_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.player_input = self.player_input[:-1]
                else:
                    self.player_input += event.unicode

    def play(self):
        # pygame.display.flip()

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            self.draw_input_rectangle()
            self.draw_input_chat()
            if self.continue_game:
                if not self.decide_continue():
                    self.continue_game = False
                    return self.continue_game
                self.update()

            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def update(self):

        for i in range(len(self.asteroids)):
            self.asteroids[i].move()

        pygame.display.update()

        for i in range(len(self.asteroids)):
            if self.asteroids[i].is_collide(self.earth):
                self.asteroids[i] = Space(False, self.surface)
                self.answers.append(self.asteroids[i].get_word())
                self.health -= 1
                transparent_red = (255, 0, 0, 100)
                self.surface.fill(transparent_red)
                pygame.display.update()

    def add_obstacle(self):
        if self.score > len(self.asteroids) * 20:
            self.asteroids.append(Space(False, self.surface))

    def update_score(self):
        self.score += len(self.player_input)



    def draw(self):
        # draws all objects
        # self is the game whose objects will be drawn
        self.surface.fill(self.bg_color)
        self.earth.draw()
        self.draw_health_bar()
        self.draw_score()

        for i in range(len(self.asteroids)):
            self.asteroids[i].draw()

    def draw_score(self):
        font_size = 50
        font = pygame.font.SysFont('arial', font_size)
        text_img = font.render('Score: ' + str(self.score), True, pygame.Color('white'), pygame.Color('black'))
        text_img_pos = ((self.surface.get_width() / 2) + 115, self.white_rect_pos[1] - font_size - 5)
        self.surface.blit(text_img, text_img_pos)

    def decide_continue(self):
        if self.health == 0:
            return False
        return True

    def draw_input_rectangle(self):
        # this method draws a rectangle at the bottom of the screen
        pygame.draw.rect(self.surface, pygame.Color('white'), self.rectangle_white)
        pygame.draw.rect(self.surface, pygame.Color('black'), self.rectangle_black)

    def draw_health_bar(self):
        # this method draws a rectangle at the bottom of the screen
        length_factor = 5 * self.health / 8 / self.max_health
        health_bar = pygame.Rect(self.white_rect_pos[0], self.white_rect_pos[1] - 35,
                                 self.white_rect_size[0] * length_factor, self.white_rect_size[1] / 2)
        pygame.draw.rect(self.surface, pygame.Color('red'), health_bar)

    def draw_input_chat(self):
        #
        font = pygame.font.Font(None, 60)
        player_input_image = font.render(self.player_input, True, pygame.Color('white'))
        player_input_image_pos = (325, 720 - 45)
        self.surface.blit(player_input_image, player_input_image_pos)

    def get_score(self):
        return self.score

main()
