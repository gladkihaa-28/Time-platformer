import os
import sys
import pygame
from settings import *

def load_main():
    pygame.init()

    # Установка размеров окна
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    sound = pygame.mixer.Sound("sounds/sound_bg.mp3")
    sound.play(-1)

    # Установка заголовка окна
    pygame.display.set_caption("Уровни")

    # Установка цвета фона
    background_color = (0, 0, 0)

    # Установка цвета кнопок
    button_color = (255, 255, 255)

    # Установка размеров кнопок
    button_width = 150
    button_height = 50

    # Установка шрифта
    font_name = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 36)

    bg = pygame.image.load("images/background.jpg").convert()
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))

    # Создание кнопок
    button1 = pygame.Rect(300, 600, button_width, button_height)
    button2 = pygame.Rect(500, 600, button_width, button_height)
    button3 = pygame.Rect(700, 600, button_width, button_height)

    # Отрисовка кнопок
    pygame.draw.ellipse(screen, button_color, button1)
    pygame.draw.ellipse(screen, button_color, button2)
    pygame.draw.ellipse(screen, button_color, button3)

    # Отрисовка текста на кнопках
    name = font_name.render("Платформер Time", True, (0, 0, 0))
    text1 = font.render("Уровень 1", True, background_color)
    text2 = font.render("Играть!", True, background_color)
    text3 = font.render("Уровень 2", True, background_color)
    screen.blit(name, (400, 50))
    screen.blit(text1, (button1.x + 10, button1.y + 10))
    screen.blit(text2, (button2.x + 30, button2.y + 10))
    screen.blit(text3, (button3.x + 10, button3.y + 10))

    pygame.display.flip()

    return button1, button2, button3


def load_levels(button1, button2, button3):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    pygame.quit()
                    load_level1()
                elif button2.collidepoint(event.pos):
                    pygame.quit()
                    load_level1()
                elif button3.collidepoint(event.pos):
                    pygame.quit()
                    load_level2()


def load_level2():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Платформер")
    clock = pygame.time.Clock()
    icon = pygame.image.load("images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)

    sound_bg = pygame.mixer.Sound("sounds/sound_bg.mp3")
    sound_bg.play(-1)

    bg = pygame.image.load("images/background.jpg").convert()
    bg = pygame.transform.scale(bg, (1200, 800))

    ghost = pygame.image.load("images/ghost.png").convert_alpha()
    ghost = pygame.transform.scale(ghost, (80, 80))
    ghost_x = 1300
    ghost_y = 580
    ghost_speed = 15
    ghost_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 3000)
    ghost_list_in_game = []
    ghosts = 0

    bullet = pygame.image.load("images/bullet.png").convert_alpha()
    bullet2 = pygame.image.load("images/bullet2.png").convert_alpha()
    bullets = []
    bullet_speed = 25
    bullets_left = 10


    walk_right = [
        pygame.transform.scale(pygame.image.load("images/right_player1.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("images/right_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("images/right_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("images/right_player1.png").convert_alpha(), (100, 100)),
    ]
    walk_left = [
        pygame.transform.scale(pygame.image.load("images/left_player1.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("images/left_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("images/left_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("images/left_player1.png").convert_alpha(), (100, 100)),
    ]
    walk = walk_right

    player_speed = 10
    player_x = 150
    player_y = 580
    is_jump = False
    jump_count = 10

    heart = pygame.image.load("images/heart.png").convert_alpha()
    heart = pygame.transform.scale(heart, (50, 50))
    lives = 3

    platform_img = pygame.transform.scale(pygame.image.load("images/platform.png").convert_alpha(), (1200, 50))

    animation = 0
    bg_x = 0
    gameplay = True
    label = pygame.font.Font(None, 60)
    lose_label = label.render("Вы проиграли!", False, (193, 196, 199))
    restart_label = label.render("Начать заново", False, (115, 132, 158))
    restart_label_rect = restart_label.get_rect(topleft=(420, 400))


    running = True
    while running:
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 1199, 0))
        screen.blit(walk[animation], (player_x, player_y))
        pygame.draw.line(screen, (56, 3, 4), (980, 125), (1200, 125), 250)
        pygame.draw.line(screen, (56, 3, 4), (0, 100), (300, 100), 200)
        screen.blit(bullet, (1030, 90))
        bullets_label = label.render(str(bullets_left), False, (193, 196, 199))
        ghosts_label = label.render(str(ghosts), False, (193, 196, 199))
        text_label = label.render("Цель:", False, (193, 196, 199))
        text_label2 = label.render("20", False, (193, 196, 199))
        screen.blit(bullets_label, (1110, 100))
        screen.blit(ghost, (1020, 150))
        screen.blit(ghosts_label, (1120, 170))
        pygame.draw.line(screen, (0, 0, 0), (980, 0), (980, 250), 10)
        pygame.draw.line(screen, (0, 0, 0), (976, 250), (1200, 250), 10)
        pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 200), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (305, 200), 10)
        screen.blit(text_label, (70, 30))
        screen.blit(ghost, (40, 100))
        screen.blit(text_label2, (130, 120))
        screen.blit(platform_img, (0, 670))


        if gameplay:
            player_rect = walk[0].get_rect(topleft=(player_x, player_y))
            ghost_rect = ghost.get_rect(topleft=(ghost_x, ghost_y))

            if ghosts >= 20:
                print("Done!")
                pygame.quit()
                sys.exit()

            for i in range(lives):
                screen.blit(heart, (1115 - (50 * i), 30))

            if ghost_list_in_game:
                for i, el in enumerate(ghost_list_in_game):
                    screen.blit(ghost, el)
                    el.x -= ghost_speed

                    if el.x < -20:
                        ghost_list_in_game.pop(i)
                        ghosts += 1

                    if player_rect.colliderect(el):
                        if lives <= 1:
                            gameplay = False
                        else:
                            lives -= 1
                            ghost_list_in_game.pop(i)
                        ghosts += 1

            if bullets:
                for i, bul in enumerate(bullets):
                    el = bul[0]
                    if bul[1] == "right":
                        screen.blit(bullet, (el.x, el.y))
                        el.x += bullet_speed
                    else:
                        screen.blit(bullet2, (el.x, el.y))
                        el.x -= bullet_speed

                    if el.x > 1300:
                        bullets.pop(i)

                    if ghost_list_in_game:
                        for index, ghost_el in enumerate(ghost_list_in_game):
                            if el.colliderect(ghost_el):
                                ghost_list_in_game.pop(index)
                                bullets.pop(i)
                                ghosts += 1

            animation += 1
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
                walk = walk_left
            elif keys[pygame.K_RIGHT] and player_x < 1100:
                player_x += player_speed
                walk = walk_right
            elif keys[pygame.K_q]:
                pygame.quit()
                os.system("python main.py")


            if not is_jump:
                if keys[pygame.K_UP]:
                    is_jump = True
            else:
                if jump_count >= -10:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:

                    is_jump = False
                    jump_count = 10

            if animation == 4:
                animation = 0

            if bg_x != -1200:
                bg_x -= 2
            else:
                bg_x = 0
        else:
            screen.fill((0, 0, 0))
            screen.blit(lose_label, (400, 300))
            screen.blit(restart_label, restart_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 150
                ghost_list_in_game.clear()
                bullets.clear()
                bullets_left = 10
                lives = 3
                ghosts = 0

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    screen.fill((255, 255, 255))
            elif event.type == ghost_timer:
                ghost_list_in_game.append(ghost.get_rect(topleft=(1300, ghost_y)))
            elif gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_left > 0:
                if walk == walk_right:
                    bullets.append((bullet.get_rect(topleft=(player_x + 100, player_y + 30)), "right"))
                else:
                    bullets.append((bullet2.get_rect(topleft=(player_x - 60, player_y + 30)), "left"))
                bullets_left -= 1

        clock.tick(30)

