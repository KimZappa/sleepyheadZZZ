#Class to define main sprite student object
import pygame
WHITE = (255, 255, 255)


class Student(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load(r'C:\Users\KimZa\Desktop\Into to Python\game\mainsprite.png').convert_alpha()


        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveDown(self,dist):
        self.rect.y += dist  # move down

    def moveUp(self,dist):
        self.rect.y -= dist  # move up
