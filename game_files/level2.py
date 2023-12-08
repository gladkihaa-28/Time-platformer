import os
import sys
import time

import pygame
from game_files.settings import *

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


def load_win(screen, sound):
    trophy = pygame.image.load("game_files/images/trophy.png").convert_alpha()
    sound.stop()
    sound_win = pygame.mixer.Sound("game_files/sounds/win.wav")
    sound_win.play()
    screen.blit(trophy, (500, 200))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    os.system("python main.py")


def load_level2():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Платформер")
    clock = pygame.time.Clock()
    icon = pygame.image.load("game_files/images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)

    sound_zawarudo = pygame.mixer.Sound("game_files/sounds/zawarudo.mp3")
    sound_bg = pygame.mixer.Sound("game_files/sounds/sound_bg.mp3")
    sound_bg.play(-1)

    bg = pygame.image.load("game_files/images/background.jpg").convert()
    bg_lose = pygame.image.load("game_files/images/background_lose.jpg").convert()
    bg = pygame.transform.scale(bg, (1200, 800))
    bg_lose = pygame.transform.scale(bg_lose, (1200, 800))

    ghost = pygame.image.load("game_files/images/ghost.png").convert_alpha()
    ghost = pygame.transform.scale(ghost, (80, 80))
    ghost_x = 1300
    ghost_y = 580
    ghost_speed = 15
    ghost_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 3000)
    ghost_list_in_game = []
    ghosts_sum_for_win = 10
    ghosts = 0

    stopwatch = pygame.image.load("game_files/images/stopwatch.png").convert_alpha()
    stopwatch = pygame.transform.scale(stopwatch, (80, 80))
    zawarudo_timer = None
    zawarudo = False
    zawarudo_count = 3

    bullet = pygame.image.load("game_files/images/bullet.png").convert_alpha()
    bullet2 = pygame.image.load("game_files/images/bullet2.png").convert_alpha()
    bullets = []
    bullet_speed = 60
    bullets_left = 10
    sound_shot = pygame.mixer.Sound("game_files/sounds/shot.mp3")


    walk_right = [
        pygame.transform.scale(pygame.image.load("game_files/images/right_player1.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("game_files/images/right_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("game_files/images/right_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("game_files/images/right_player1.png").convert_alpha(), (100, 100)),
    ]
    walk_left = [
        pygame.transform.scale(pygame.image.load("game_files/images/left_player1.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("game_files/images/left_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("game_files/images/left_player2.png").convert_alpha(), (100, 100)),
        pygame.transform.scale(pygame.image.load("game_files/images/left_player1.png").convert_alpha(), (100, 100)),
    ]
    walk = walk_right

    player_speed = 15
    player_x = 150
    player_y = 580
    is_jump = False
    jump_count = 10

    heart = pygame.image.load("game_files/images/heart.png").convert_alpha()
    heart = pygame.transform.scale(heart, (50, 50))
    lives = 3

    platform_img1 = pygame.transform.scale(pygame.image.load("game_files/images/platform.png").convert_alpha(), (1200, 50))
    platform_img2 = pygame.transform.scale(pygame.image.load("game_files/images/platform2.png").convert_alpha(), (1200, 50))
    platform_img = platform_img1

    animation = 0
    bg_x = 0
    gameplay = True
    label = pygame.font.Font(None, 60)
    lose_label = label.render("Вы проиграли!", False, (255, 255, 255))
    restart_label = label.render("Начать заново", False, (193, 196, 199))
    quit_label = label.render("Выйти", False, (193, 196, 199))
    restart_label_rect = restart_label.get_rect(topleft=(430, 400))
    quit_label_rect = restart_label.get_rect(topleft=(520, 500))


    running = True
    while running:
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 1199, 0))
        screen.blit(walk[animation], (player_x, player_y))
        pygame.draw.line(screen, (56, 3, 4), (980, 175), (1200, 175), 350)
        pygame.draw.line(screen, (56, 3, 4), (0, 100), (300, 100), 200)
        bullets_label = label.render(str(bullets_left), False, (255, 255, 255))
        ghosts_label = label.render(str(ghosts), False, (255, 255, 255))
        zawarudo_label = label.render(str(zawarudo_count), False, (255, 255, 255))
        text_label = label.render("Цель:", False, (255, 255, 255))
        text_label2 = label.render(f"{ghosts_sum_for_win}", False, (255, 255, 255))
        screen.blit(bullet, (1030, 90))
        screen.blit(bullets_label, (1110, 100))
        screen.blit(ghost, (1020, 150))
        screen.blit(ghosts_label, (1120, 170))
        screen.blit(stopwatch, (1020, 240))
        screen.blit(zawarudo_label, (1120, 260))
        pygame.draw.line(screen, (0, 0, 0), (980, 0), (980, 350), 10)
        pygame.draw.line(screen, (0, 0, 0), (976, 350), (1200, 350), 10)
        pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 200), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (305, 200), 10)
        screen.blit(text_label, (70, 30))
        screen.blit(ghost, (40, 100))
        screen.blit(text_label2, (130, 120))
        screen.blit(platform_img, (0, 670))


        if gameplay:
            player_rect = walk[0].get_rect(topleft=(player_x, player_y))
            ghost_rect = ghost.get_rect(topleft=(ghost_x, ghost_y))

            if ghosts >= ghosts_sum_for_win:
                ghost_speed = 0
                player_speed = 0
                load_win(screen, sound_bg)


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
            screen.blit(bg_lose, (0, 0))
            screen.blit(lose_label, (430, 300))
            screen.blit(restart_label, restart_label_rect)
            screen.blit(quit_label, quit_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 150
                ghost_list_in_game.clear()
                bullets.clear()
                bullets_left = 10
                lives = 3
                ghosts = 0
                zawarudo_count = 3
            elif quit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
                os.system("python ../main.py")

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    screen.fill((255, 255, 255))
            elif event.type == ghost_timer and not zawarudo:
                ghost_list_in_game.append(ghost.get_rect(topleft=(1300, ghost_y)))
            elif gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_left > 0:
                sound_shot.play()
                if walk == walk_right:
                    bullets.append((bullet.get_rect(topleft=(player_x + 100, player_y + 30)), "right"))
                else:
                    bullets.append((bullet2.get_rect(topleft=(player_x - 60, player_y + 30)), "left"))
                bullets_left -= 1
            elif gameplay and event.type == pygame.KEYUP and event.key == pygame.K_z and not zawarudo and zawarudo_count > 0:
                platform_img = platform_img2
                zawarudo = True
                ghost_speed = 0
                zawarudo_count -= 1
                sound_bg.stop()
                sound_zawarudo.play()
                zawarudo_timer = pygame.USEREVENT + 2
                pygame.time.set_timer(zawarudo_timer, 5000)
            elif event.type == zawarudo_timer and zawarudo:
                platform_img = platform_img1
                ghost_speed = 15
                zawarudo = False
                sound_bg.play(-1)

        clock.tick(30)

