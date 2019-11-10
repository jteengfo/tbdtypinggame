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


# import pygame
# import random

import sys
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
    game.play()


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

    def main_execute(self):
        while self.main_menu_stay:
            self.handle_events()
            self.draw()

            self.update()

    def draw(self):
        # this method draws the title screen
        tbd_font = pygame.font.Font(None, 100)
        tbd_img = tbd_font.render('TBD Typing Game', True, pygame.Color('white'))
        tbd_pos = [self.title_width / 2 - tbd_img.get_width() / 2, self.title_height /2 + tbd_img.get_height() / 2]
        self.surface.blit(tbd_img, tbd_pos)

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
    #     screen_width = self.surface.get_width()
    #     screen_height = self.surface.get_height()
    #     tbd_pos =
    #     tbd_velocity = 4
    #     if


class Game:

    def __init__(self, surface):
        self.counter = 0
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
        # player input objects
        player_rect_white = (320, 720 - 50, 640, 50)
        player_rect_black = (325, 720 - 45, 630, 40)
        self.rectangle_white = pygame.Rect(player_rect_white)
        self.rectangle_black = pygame.Rect(player_rect_black)
        self.player_input = ""

    def handle_events(self):
        # method that handles event by user that changes the state of the game
        # self is the game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            answer = 'dog'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.player_input == answer:
                        print(True)
                    else:
                        print('try again you freaking tard')
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
                self.update()

            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def update(self):

        for i in range(len(self.asteroids)):
            self.asteroids[i].move()

        pygame.display.update()

        for i in range(len(self.asteroids)):
            if self.asteroids[i].is_collide(self.earth):
                self.asteroids[i] = Space(False, self.surface)
                self.counter += 1
                self.check_new_asteroid()

    def check_new_asteroid(self):
        if self.counter >= 3:
            self.asteroids.append(Space(False, self.surface))
            self.counter = 0

    def draw(self):
        # draws all objects
        # self is the game whose objects will be drawn
        self.surface.fill(self.bg_color)
        self.earth.draw()

        for i in range(len(self.asteroids)):
            self.asteroids[i].draw()

    def decide_continue(self):
        return True

    def draw_input_rectangle(self):
        # this method draws a rectangle at the bottom of the screen
        pygame.draw.rect(self.surface, pygame.Color('white'), self.rectangle_white)
        pygame.draw.rect(self.surface, pygame.Color('black'), self.rectangle_black)

    def draw_input_chat(self):
        #
        font = pygame.font.Font(None, 60)
        player_input_image = font.render(self.player_input, True, pygame.Color('white'))
        player_input_image_pos = (325, 720 - 45)
        self.surface.blit(player_input_image, player_input_image_pos)


# class Space:
#     def __init__(self, is_earth, surface):
#
#         # Initializes a space object.
#         # - self is the space object to initialize
#         # - center is the center of the object
#         # - radius is the radius of the dot
#         # - velocity is a list containing the x and y speed
#         # - surface is the window's pygame.surface object
#
#         self.surface = surface
#
#         width, height = pygame.display.get_surface().get_size()
#
#         if is_earth:
#             self.center = (int(width / 2), int(height / 2))
#             self.radius = 100
#             self.velocity = (0, 0)
#             self.color = pygame.Color("blue")
#
#         else:
#             self.center = [random.randint(0, width), random.randint(0, height)]
#             self.velocity = (random.randint(1, 10), random.randint(1, 10))
#             self.radius = random.randint(20, 30)
#             self.color = pygame.Color("orange")
#
#     def move(self):
#         # changes the locations of the space object by adding the
#         # x and y speed values to the x and y coordinates of the center
#
#         self.center[0] += self.velocity[0]
#         self.center[1] += self.velocity[1]
#
#     def draw(self):
#         # Draw the object on the surface
#         # self is the space object
#         pygame.draw.circle(self.surface, self.color, self.center, self.radius)


# class Word:
#
#     def __init__(self):
#
#         # opens and reads words txt file
#         # self is the Word whose words txt is open, read, and listed in a list
#         words_txt = open('words.txt', 'r')  # opens the txt file
#         words_list_content = words_txt.readlines()  # reads all words and creates list of strings
#         for i in range(len(words_list_content)):  # for each element in the list
#             words_list_content[i] = words_list_content[i].strip()  # removes all whitespace
#         words_list_content.close()
#
#         # set content
#         chosen_word = random.choice(words_list_content)
#         print(chosen_word)
#
#     def choose_word(self):
#         pass
#
#     def draw(self):
#         pass
#
#     def move(self):
#         pass


main()
