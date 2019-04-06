import pygame
from sleepy import Sleepy
from awake import Awake
from teacher import Teacher
from student import Student
pygame.init()

size = (1200, 650)
screen = pygame.display.set_mode(size)
background = [210, 180, 140]
screen.fill(background)
pygame.display.set_caption("Game Background")
pygame.display.flip()

desk = (124, 74, 59)

#build all sleeping student sprites and set locations
allSleepy_sprites_list = pygame.sprite.Group()

sleepy_student1 = Sleepy(10, 10)
sleepy_student1.rect.x = 20
sleepy_student1.rect.y = 30
allSleepy_sprites_list.add(sleepy_student1)

sleepy_student2 = Sleepy(10, 10)
sleepy_student2.rect.x = 150
sleepy_student2.rect.y = 300
allSleepy_sprites_list.add(sleepy_student2)

sleepy_student3 = Sleepy(10, 10)
sleepy_student3.rect.x = 800
sleepy_student3.rect.y = 350
allSleepy_sprites_list.add(sleepy_student3)

sleepy_student4 = Sleepy(10, 10)
sleepy_student4.rect.x = 810
sleepy_student4.rect.y = 100
allSleepy_sprites_list.add(sleepy_student4)

sleepy_student5 = Sleepy(10, 10)
sleepy_student5.rect.x = 150
sleepy_student5.rect.y = 30
allSleepy_sprites_list.add(sleepy_student5)

#build the awake student sprites
allAwake_sprites_list = pygame.sprite.Group()

awake1 = Awake(10, 10)
awake1.rect.x = 90
awake1.rect.y = 180
allAwake_sprites_list.add(awake1)

awake2 = Awake(10, 10)
awake2.rect.x = 1100
awake2.rect.y = 180
allAwake_sprites_list.add(awake2)

awake3 = Awake(10, 10)
awake3.rect.x = 300
awake3.rect.y = 270
allAwake_sprites_list.add(awake3)

awake4 = Awake(10, 10)
awake4.rect.x = 400
awake4.rect.y = 270
allAwake_sprites_list.add(awake4)

awake5 = Awake(10, 10)
awake5.rect.x = 400
awake5.rect.y = 390
allAwake_sprites_list.add(awake5)

awake6 = Awake(10, 10)
awake6.rect.x = 900
awake6.rect.y = 500
allAwake_sprites_list.add(awake6)

awake7 = Awake(10, 10)
awake7.rect.x = 700
awake7.rect.y = 500
allAwake_sprites_list.add(awake7)

#build the teacher sprite
allTeacher_sprites_list = pygame.sprite.Group()
teacher = Teacher(10, 10)
teacher.rect.x = 890
teacher.rect.y = 180
allTeacher_sprites_list.add(teacher)

#build the stucent sprite
allPlayer_sprites_list = pygame.sprite.Group()
player = Student(10, 10)
player.rect.x = 10
player.rect.y = 550
allPlayer_sprites_list.add(player)


run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        player.moveRight(5)
    if keys[pygame.K_UP]:
        player.moveUp(5)
    if keys[pygame.K_DOWN]:
        player.moveDown(5)

    allSleepy_sprites_list.update()
    allAwake_sprites_list.update()
    allTeacher_sprites_list.update()
    allPlayer_sprites_list.update()
    screen.fill(background)

    #game layout
    pygame.draw.rect(screen, desk, (100, 25, 200, 50))
    pygame.draw.rect(screen, desk, (100, 50, 50, 175))
    pygame.draw.rect(screen, desk, (900, 75, 215, 215))
    pygame.draw.rect(screen, desk, (225, 350, 400, 80))
    pygame.draw.rect(screen, desk, (725, 575, 200, 50))
    pygame.draw.rect(screen, desk, (800, 450, 50, 175))

    allSleepy_sprites_list.draw(screen)
    allAwake_sprites_list.draw(screen)
    allTeacher_sprites_list.draw(screen)
    allPlayer_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
