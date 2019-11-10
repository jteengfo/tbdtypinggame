import pygame, random, math
#1280x720

MIN_RADIUS = 10

width = 1280
height = 720


class Object():
    def __init__(self):
        self.xPos = random.random() * width
        self.yPos = height

        self.xVel = (width/2 - self.xPos)/20
        self.yVel = (height/2 - self.yPos)/20

        self.radius = (random.random() + 1) * MIN_RADIUS

        print((self.xPos - width/2) + (self.yPos - height/2))
        print("x = " + str(self.yPos - height/2))
        print("y = " + str(self.xPos - width/2))

    def update(self):
        self.xPos += self.xVel
        self.yPos += self.yVel


def main():
    asteroid = Object()

    while(abs((asteroid.xPos - width/2)) + abs((asteroid.yPos - height/2)) > 10):
        print(asteroid.xPos)
        asteroid.update()

    print("done")
    print((asteroid.xPos - width/2) + (asteroid.yPos - height/2))
    print("x = " + str(asteroid.yPos-height/2))
    print("y = " + str(asteroid.xPos-width/2))

    return 0


main()
