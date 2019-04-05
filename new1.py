import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
 
class MainChar(pygame.sprite.Sprite):
#class represents the sprite that is playing the game

#def __init__(self):
 #   super().__init__()
   # MainPerson = pygame.image.load("MainSprite.jpeg")
        # Load the image
  #  self.image = pygame.image.load("player.png").convert()
 
    # Set our transparent color
   # self.image.set_colorkey(WHITE)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("sleepyheadZZZ")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

text_rotate_degrees = 0
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    font = pygame.font.SysFont('Calibri', 40, True, False)
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(60, 60, 60, 150))
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(120, 210, 150, 60))
    pygame.draw.rect(screen, (128 ,128, 128), pygame.Rect(500, 500, 200, 50))
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(700, 700, 300, 400))

    # --- Drawing code should go here
     # Animated rotation
    text = font.render("sleepyheadZZZ", True, WHITE)
    #text = pygame.transform.rotate(text, text_rotate_degrees)
    #text_rotate_degrees += 1
    screen.blit(text, [100, 50])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
