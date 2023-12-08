import os
import random
import pygame
import sys
from settings import *
from level2 import load_level2


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


def load_level1():
    # Инициализация Pygame
    pygame.init()
    sound_bg = pygame.mixer.Sound("sounds/sound_bg.mp3")
    sound_bg.play(-1)
    # Определение констант
    WIDTH, HEIGHT = 1200, 800
    PLAYER_SIZE = 50
    PLAYER_COLOR = (0, 128, 255)
    GROUND_COLOR = (0, 255, 0)
    PLATFORM_COLOR = (255, 0, 0)

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Простой платформер")

    bg = pygame.image.load("images/background.jpg").convert()
    bg = pygame.transform.scale(bg, (1200, 800))
    bg_x = 0

    # Определение игрока
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
    player_x = 100
    player_y = 580
    player_rect = walk[0].get_rect(topleft=(player_x, player_y))
    player_y_speed = 0
    player_speed = 10
    gravity = 2
    on_ground = False  # Переменная состояния для отслеживания нахождения персонажа на земле
    animation = 0

    coin_img = pygame.image.load("images/ruble.png").convert_alpha()
    coin_final_img = pygame.image.load("images/ruble_final.png").convert_alpha()
    coins_count = 0
    coins = []

    # Переменные для камеры
    camera_x = 0
    camera_y = 0

    # Определение земли
    ground_rect = pygame.Rect(0, HEIGHT - 50, 100000, 50)

    platform_img = pygame.transform.scale(pygame.image.load("images/platform.png").convert_alpha(), (200, 50))
    platform_rects = [pygame.Rect(0, HEIGHT - 150, 200, 50)]
    start = 0
    label = pygame.font.Font(None, 60)
    lose_label = label.render("Вы проиграли!", False, (193, 196, 199))
    restart_label = label.render("Начать заново", False, (115, 132, 158))
    restart_label_rect = restart_label.get_rect(topleft=(420, 400))
    blocks = 20
    for i in range(blocks):
        start += 300
        n = random.randint(200, 400)
        platform_rects.append(pygame.Rect(start + 100, HEIGHT - n, 200, 30))
        if i % 2 == 0:
            coins.append(pygame.Rect(start + 170, HEIGHT - n - 70, 200, 30))
        start += 100

    start += 300
    n = random.randint(200, 400)
    platform_rects.append(pygame.Rect(start + 100, HEIGHT - n, 200, 30))
    coins.append(pygame.Rect(start + 170, HEIGHT - n - 70, 200, 30))

    gameplay = True

    # Основной цикл игры
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 1199, 0))
        screen.blit(coin_img, (1100, 30))
        coins_label = label.render(f"{coins_count}/{blocks//2}", False, (193, 196, 199))
        if coins_count < 10:
            screen.blit(coins_label, (1010, 45))
        elif coins_count < 100:
            screen.blit(coins_label, (990, 45))

        screen.blit(walk[animation], (player_rect.x - camera_x, player_rect.y - camera_y))

        for platform in platform_rects:
            screen.blit(platform_img, (platform.x - camera_x, platform.y - camera_y))
        for i, coin in enumerate(coins):
            if i + 1 == len(coins):
                screen.blit(coin_final_img, (coin.x - camera_x, coin.y - camera_y))
            else:
                screen.blit(coin_img, (coin.x - camera_x, coin.y - camera_y))
            if player_rect.colliderect(coin):
                coins.pop(i)
                coins_count += 1
                if i == len(coins):
                    print("Done!")
                    pygame.quit()
                    load_level2()


        if gameplay:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player_rect.left > 0:
                player_rect.x -= player_speed
                walk = walk_left
            if keys[pygame.K_RIGHT]:
                player_rect.x += player_speed
                walk = walk_right
                if bg_x != -1200:
                    bg_x -= 2
                else:
                    bg_x = 0
            if keys[pygame.K_q]:
                pygame.quit()
                os.system("python main.py")
            if player_rect.y == 650:
                gameplay = False

            # Применение гравитации
            player_y_speed += gravity
            player_rect.y += player_y_speed
            player_y += player_y_speed

            # Проверка коллизий с землей
            if player_rect.colliderect(ground_rect) and player_y_speed > 0:
                player_rect.y = ground_rect.y - player_rect.height
                player_y_speed = 0
                on_ground = True  # Персонаж на земле
            else:
                on_ground = False  # Персонаж в воздухе

            # Проверка коллизий с дополнительными платформами
            for platform in platform_rects:
                if (
                    player_rect.colliderect(platform)
                    and player_y_speed > 0
                    and player_rect.bottom > platform.top
                ):
                    player_rect.y = platform.y - player_rect.height
                    player_y_speed = 0
                    on_ground = True  # Персонаж на платформе

            # Прыжок
            if keys[pygame.K_UP] and on_ground:
                player_y_speed = -28


            if animation >= 3:
                animation = 0
            else:
                animation += 1

            # Обновление координат камеры
            camera_x = max(0, player_rect.x - WIDTH // 2)
            camera_y = max(0, player_rect.y - HEIGHT // 2)

        else:
            screen.fill((0, 0, 0))
            screen.blit(lose_label, (400, 300))
            screen.blit(restart_label, restart_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_rect.x = 100
                player_rect.y = 580
                coins_count = 0
                coins = []
                platform_rects = [pygame.Rect(0, HEIGHT - 150, 200, 50)]
                start = 0
                for i in range(10):
                    start += 300
                    n = random.randint(200, 400)
                    platform_rects.append(pygame.Rect(start + 100, HEIGHT - n, 200, 30))
                    if i % 2 == 0:
                        coins.append(pygame.Rect(start + 170, HEIGHT - n - 70, 200, 30))
                    start += 100

                start += 300
                n = random.randint(200, 400)
                platform_rects.append(pygame.Rect(start + 100, HEIGHT - n, 200, 30))
                coins.append(pygame.Rect(start + 170, HEIGHT - n - 70, 200, 30))


        pygame.display.update()
        # Установка FPS
        clock.tick(30)


