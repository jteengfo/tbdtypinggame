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

import pygame

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
    # game = Game(a_surface)


class Game:

    def __init__(self):
        # parameters to handle events
        self.closed_clicked = False
        self.continue_game = True

    def handle_events(self):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.closed_clicked = True

    def play(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def decide_continue(self):
        pass


main()