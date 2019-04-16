import pygame
from sleepy import Sleepy
from awake import Awake
from teacher import Teacher
from student import Student

pygame.init()

clock = pygame.time.Clock()
score =0
black = (0, 0, 0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

size = (1200, 650)
screen = pygame.display.set_mode(size)
background = [210, 180, 140]
screen.fill(background)
pygame.display.set_caption("Game Background")
pygame.display.flip()

desk = (124, 74, 59)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
    crash_sound = pygame.mixer.Sound(r'C:\Users\KimZa\Desktop\Into to Python\game\teacherCrash.wav')
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Busted! Game over!", largeText)
    TextSurf2, TextRect2 = text_objects("Score: {}".format(score), largeText)
    TextRect.center = ((1200 / 2), (650 / 2))
    TextRect2.center = ((1200 / 4), (650 / 4))
    screen.blit(TextSurf, TextRect)
    screen.blit(TextSurf2, TextRect2)
    pygame.display.update()

def win():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You win!", largeText)
    TextSurf2, TextRect2 = text_objects("Score: {}".format(score), largeText)
    TextRect.center = ((1200 / 2), (650 / 2))
    TextRect2.center = ((1200 / 4), (650 / 4))
    screen.blit(TextSurf, TextRect)
    screen.blit(TextSurf2, TextRect2)
    pygame.display.update()

def nextLevel():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Time for level 2!", largeText)
    TextRect.center = ((1200 / 2), (650 / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def gameMenu():
    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("SleepyHeadzZZz", largeText)
        TextRect.center = ((1200 / 2), (650 / 2))
        screen.blit(TextSurf, TextRect)

        global score
        score = 0

        button("GO!", 150, 450, 100, 50, green, bright_green, levelOne)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

def increment_score():
    global score
    score += 1

def quitgame():
    pygame.quit()
    quit()

def levelOne():
    # build all sleeping student sprites and set locations
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

    # build the awake student sprites
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

    # build the teacher sprite
    allTeacher_sprites_list = pygame.sprite.Group()
    teacher = Teacher(10, 10)
    teacher.rect.x = 690
    teacher.rect.y = 180
    allTeacher_sprites_list.add(teacher)

    teacher2 = Teacher(10, 10)
    teacher2.rect.x = 330
    teacher2.rect.y = 150
    allTeacher_sprites_list.add(teacher2)

    # build the stucent sprite
    allPlayer_sprites_list = pygame.sprite.Group()
    player = Student(10, 10)
    player.rect.x = 10
    player.rect.y = 550
    allPlayer_sprites_list.add(player)

    # background music
    pygame.mixer.music.load(r'C:\Users\KimZa\Desktop\Into to Python\game\UpbeatFunk.wav')
    pygame.mixer.music.play(-1)

    player.rect.x = 10
    player.rect.y = 550

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    run = False
            elif len(allSleepy_sprites_list) == 0:
                nextLevel()
                pygame.time.wait(1800)
                levelTwo()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5)
        if keys[pygame.K_UP]:
            player.moveUp(5)
        if keys[pygame.K_DOWN]:
            player.moveDown(5)

        #if player collides with a teacher game ends
        collideWithFirstTeacher = pygame.sprite.collide_rect(player,teacher)
        if collideWithFirstTeacher == True:
            crash()
            pygame.time.wait(1800)
            run = False
        # if player collides with a teacher game ends
        collideWithSecondTeacher = pygame.sprite.collide_rect(player, teacher2)
        if collideWithSecondTeacher == True:
            crash()
            pygame.time.wait(1800)
            run = False

         # if player colides with sleeping student remove it from screen
        collideWithSleepy1 = pygame.sprite.collide_rect(player, sleepy_student1)
        if collideWithSleepy1 == True:
            if sleepy_student1 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student1)
            awake8 = Awake(10, 10)
            awake8.rect.x = 20
            awake8.rect.y = 30
            allAwake_sprites_list.add(awake8)



        collideWithSleepy2 = pygame.sprite.collide_rect(player, sleepy_student2)
        if collideWithSleepy2 == True:
            if sleepy_student2 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student2)
            awake9 = Awake(10, 10)
            awake9.rect.x = 150
            awake9.rect.y = 300
            allAwake_sprites_list.add(awake9)


        collideWithSleepy3 = pygame.sprite.collide_rect(player, sleepy_student3)
        if collideWithSleepy3 == True:
            if sleepy_student3 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student3)
            awake10 = Awake(10, 10)
            awake10.rect.x = 800
            awake10.rect.y = 350
            allAwake_sprites_list.add(awake10)




        collideWithSleepy4 = pygame.sprite.collide_rect(player, sleepy_student4)
        if collideWithSleepy4 == True:
            if sleepy_student4 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student4)
            awake11 = Awake(10, 10)
            awake11.rect.x = 810
            awake11.rect.y = 100
            allAwake_sprites_list.add(awake11)


        collideWithSleepy5 = pygame.sprite.collide_rect(player, sleepy_student5)
        if collideWithSleepy5 == True:
            if sleepy_student5 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student5)
            awake12 = Awake(10, 10)
            awake12.rect.x = 150
            awake12.rect.y = 30
            allAwake_sprites_list.add(awake12)


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



def levelTwo():
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

    sleepy_student6 = Sleepy(10, 10)
    sleepy_student6.rect.x = 915
    sleepy_student6.rect.y = 230
    allSleepy_sprites_list.add(sleepy_student6)



    # build the awake student sprites
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

    # build the teacher sprite
    allTeacher_sprites_list = pygame.sprite.Group()
    teacher = Teacher(10, 10)
    teacher.rect.x = 690
    teacher.rect.y = 180
    allTeacher_sprites_list.add(teacher)

    teacher2 = Teacher(10, 10)
    teacher2.rect.x = 310
    teacher2.rect.y = 100
    allTeacher_sprites_list.add(teacher2)

    teacher3 = Teacher(10, 10)
    teacher3.rect.x = 200
    teacher3.rect.y = 500
    allTeacher_sprites_list.add(teacher3)

    # build the stucent sprite
    allPlayer_sprites_list = pygame.sprite.Group()
    player = Student(10, 10)
    player.rect.x = 10
    player.rect.y = 550
    allPlayer_sprites_list.add(player)

    # background music
    pygame.mixer.music.load(r'C:\Users\KimZa\Desktop\Into to Python\game\ShakeYourBootay.wav')
    pygame.mixer.music.play(-1)

    player.rect.x = 10
    player.rect.y = 550

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    run = False
            elif len(allSleepy_sprites_list) == 0:
                win()
                pygame.time.wait(1800)
                gameMenu()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5)
        if keys[pygame.K_UP]:
            player.moveUp(5)
        if keys[pygame.K_DOWN]:
            player.moveDown(5)

        # if player collides with a teacher game ends
        collideWithFirstTeacher = pygame.sprite.collide_rect(player, teacher)
        if collideWithFirstTeacher == True:
            crash()
            pygame.time.wait(1800)
            gameMenu()
        # if player collides with a teacher game ends
        collideWithSecondTeacher = pygame.sprite.collide_rect(player, teacher2)
        if collideWithSecondTeacher == True:
            crash()
            pygame.time.wait(1800)
            gameMenu()
        collideWithThirdTeacher = pygame.sprite.collide_rect(player, teacher3)
        if collideWithThirdTeacher == True:
            crash()
            pygame.time.wait(1800)
            gameMenu()

        # if player collides with sleeping student remove it from screen
        collideWithSleepy1 = pygame.sprite.collide_rect(player, sleepy_student1)
        if collideWithSleepy1 == True:
            if sleepy_student1 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student1)
            awake8 = Awake(10, 10)
            awake8.rect.x = 20
            awake8.rect.y = 30
            allAwake_sprites_list.add(awake8)


        collideWithSleepy2 = pygame.sprite.collide_rect(player, sleepy_student2)
        if collideWithSleepy2 == True:
            if sleepy_student2 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student2)
            awake9 = Awake(10, 10)
            awake9.rect.x = 150
            awake9.rect.y = 300
            allAwake_sprites_list.add(awake9)


        collideWithSleepy3 = pygame.sprite.collide_rect(player, sleepy_student3)
        if collideWithSleepy3 == True:
            if sleepy_student3 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student3)
            awake10 = Awake(10, 10)
            awake10.rect.x = 800
            awake10.rect.y = 350
            allAwake_sprites_list.add(awake10)


        collideWithSleepy4 = pygame.sprite.collide_rect(player, sleepy_student4)
        if collideWithSleepy4 == True:
            if sleepy_student4 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student4)
            awake11 = Awake(10, 10)
            awake11.rect.x = 810
            awake11.rect.y = 100
            allAwake_sprites_list.add(awake11)


        collideWithSleepy5 = pygame.sprite.collide_rect(player, sleepy_student5)
        if collideWithSleepy5 == True:
            if sleepy_student5 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student5)
            awake12 = Awake(10, 10)
            awake12.rect.x = 150
            awake12.rect.y = 30
            allAwake_sprites_list.add(awake12)


        collideWithSleepy6 = pygame.sprite.collide_rect(player, sleepy_student6)
        if collideWithSleepy6 == True:
            if sleepy_student6 in allSleepy_sprites_list:
                increment_score()
            allSleepy_sprites_list.remove(sleepy_student6)
            awake13 = Awake(10, 10)
            awake13.rect.x = 915
            awake13.rect.y = 230
            allAwake_sprites_list.add(awake13)


        allSleepy_sprites_list.update()
        allAwake_sprites_list.update()
        allTeacher_sprites_list.update()
        allPlayer_sprites_list.update()
        screen.fill(background)

        # game layout
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


gameMenu()
levelOne()
pygame.quit()
