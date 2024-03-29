import os
import sys

import pygame
from game_files.settings import *
from game_files.level1 import load_level1
from game_files.level2 import load_level2

pygame.init()


def load_main():
    pygame.init()

    # Установка размеров окна
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    sound = pygame.mixer.Sound("game_files/sounds/sound_bg.mp3")
    sound.play(-1)

    # Установка заголовка окна
    pygame.display.set_caption("Платформер Time")

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

    bg = pygame.image.load("game_files/images/background.jpg").convert()
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))

    # Создание кнопок
    button1 = pygame.Rect(300, 600, button_width, button_height)
    button2 = pygame.Rect(500, 600, button_width, button_height)
    button3 = pygame.Rect(700, 600, button_width, button_height)

    with open("game_files/base.txt", "r", encoding="utf-8") as file:
        data = file.read().split("\n")
        _moneys = data[0]
        _ghosts = data[1]
    file.close()


    # Отрисовка кнопок
    pygame.draw.ellipse(screen, button_color, button1)
    pygame.draw.ellipse(screen, button_color, button2)
    pygame.draw.ellipse(screen, button_color, button3)

    # Отрисовка текста на кнопках
    name = font_name.render("Платформер Time", True, (0, 0, 0))
    text1 = font.render("Уровень 1", True, background_color)
    text2 = font.render("Играть!", True, background_color)
    text3 = font.render("Уровень 2", True, background_color)
    get_moneys = font.render(f"Собрано монет: {_moneys}", True, background_color)
    kill_ghosts = font.render(f"Убито врагов: {_ghosts}", True, background_color)
    screen.blit(name, (400, 50))
    screen.blit(text1, (button1.x + 10, button1.y + 10))
    screen.blit(text2, (button2.x + 30, button2.y + 10))
    screen.blit(text3, (button3.x + 10, button3.y + 10))
    pygame.draw.ellipse(screen, (255, 255, 255), (430, 235, 300, 200))
    screen.blit(get_moneys, (450, 300))
    screen.blit(kill_ghosts, (450, 350))

    pygame.display.flip()

    return button1, button2, button3, sound


def load_levels(button1, button2, button3, sound):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    sound.stop()
                    load_level1()
                    return
                elif button2.collidepoint(event.pos):
                    sound.stop()
                    load_level1()
                    return
                elif button3.collidepoint(event.pos):
                    sound.stop()
                    load_level2()
                    return



def main():
    while True:
        load_levels(*load_main())


if __name__ == "__main__":
    main()