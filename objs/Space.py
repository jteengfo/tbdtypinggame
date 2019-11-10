# this class handles the movement and
# the collision detection of space objects

import pygame
import random


class Space:
    def __init__(self, is_earth, surface):

        # Initializes a space object.
        # - self is the space object to initialize
        # - center is the center of the object
        # - radius is the radius of the dot
        # - velocity is a list containing the x and y speed
        # - surface is the window's pygame.surface object

        self.surface = surface

        width, height = pygame.display.get_surface().get_size()

        if is_earth:
            self.center = (int(width / 2), int(height / 2))
            self.radius = 20
            self.velocity = (0, 0)
            self.color = pygame.Color("blue")
            self.word = ''
        else:

            self.radius = random.randint(20, 100)
            self.word = get_random_word('words.txt')

            x_pos = 0
            y_pos = 0
            rand = random.randint(0,2)

            # determines which side the ball comes from depending on a random int
            if rand == 0:
                x_pos = -self.radius
                y_pos = random.randint(-self.radius, height + self.radius)
            elif rand == 1:
                x_pos = width + self.radius
                y_pos = random.randint(-self.radius, height + self.radius)
            elif rand == 2:
                x_pos = random.randint(-self.radius, width + self.radius)
                y_pos = -self.radius

            self.center = [x_pos, y_pos]

            # ensures the obstacles go towards the center of the screen
            x_velocity = (width / 2 - self.center[0]) / 500
            y_velocity = (height / 2 - self.center[1]) / 500
            self.velocity = (x_velocity, y_velocity)

            list_of_colors = ["red", "orange", "green", "brown"]
            self.color = pygame.Color(random.choice(list_of_colors))

    def move(self):
        # changes the locations of the space object by adding the
        # x and y speed values to the x and y coordinates of the center

        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    def draw(self):
        # Draw the object on the surface
        # self is the space object
        pygame.draw.circle(self.surface, self.color, (int(self.center[0]), int(self.center[1])), self.radius)
        self.draw_word()

    def is_collide(self, other):
        sum_of_radii = self.radius + other.radius
        a = self.center[0] - other.center[0]
        b = self.center[1] - other.center[1]
        c = (a**2 + b**2) ** 0.5

        if c < sum_of_radii:
            return True

        return False

    def draw_word(self):
        # draws the word underneath the obstacle
        # and has it follow the obstacle

        font_color = pygame.Color('white')
        font_bg = pygame.Color('black')
        font = pygame.font.SysFont('arial', 14)
        text_img = font.render(self.word, True, font_color, font_bg)
        text_pos = (self.center[0] - self.radius, self.center[1] + (self.radius + 20))
        self.surface.blit(text_img, text_pos)

    def get_word(self):
        return self.word

def get_random_word(filename):
    # opens and reads words txt file
    # - filename is the file being read from

    words_txt = open(filename, 'r')  # opens the txt file
    words_list_content = words_txt.readlines()  # reads all words and creates list of strings
    for i in range(len(words_list_content)):  # for each element in the list
        words_list_content[i] = words_list_content[i].strip()  # removes all whitespace
    words_txt.close()
    # set content; chosen word is the randomized word
    chosen_word = random.choice(words_list_content)
    return chosen_word
