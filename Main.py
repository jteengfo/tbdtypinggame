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
#

def main():
    # initialize all pygame modules
    pygame.init()
    # set window of certain width and height
    pygame.display.set_mode((1280, 720))
    # create a title in the window, "TBD Typing Game"
    pygame.display.set_caption("TBD Typing Game")
    # create a surface
    a_surface = pygame.display.get_surface()
    # create an object
    game = Game(a_surface)
    #main
    game.play()

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

    def handle_events(self):
        # method that handles event by user that changes the state of the game
        # self is the game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def play(self):
        # pygame.display.flip()

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            self.draw_input_rectangle()
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
        pygame.draw.rect(self.surface, pygame.Color('black'),self.rectangle_black)

    def draw_input_chat(self):
        # this method draws the
        pass
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
