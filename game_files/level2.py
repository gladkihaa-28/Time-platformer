import os
import sys
import time
import pygame


def load_win(screen, sound):
    trophy = pygame.image.load("game_files/images/trophy.png").convert_alpha()
    sound.stop()
    sound_win = pygame.mixer.Sound("game_files/sounds/win.wav")
    sound_win.play()
    screen.blit(trophy, (500, 200))
    pygame.display.update()
    time.sleep(2)
    return


def load_level2():
    with open("game_files/base.txt", "r", encoding="utf-8") as file:
        data = file.read().split("\n")
    file.close()

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("2 уровень")
    clock = pygame.time.Clock()
    icon = pygame.image.load("game_files/images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)

    sound_zawarudo = pygame.mixer.Sound("game_files/sounds/zawarudo.mp3")
    sound_requiem = pygame.mixer.Sound("game_files/sounds/requiem.mp3")
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

    fireball = pygame.image.load("game_files/images/fireball.png").convert_alpha()
    fireball_x = 1000
    fireball_y = 580
    fireball_speed = 25
    fireballs = []

    stopwatch = pygame.image.load("game_files/images/stopwatch.png").convert_alpha()
    stopwatch = pygame.transform.scale(stopwatch, (80, 80))
    zawarudo_timer = None
    zawarudo = False
    zawarudo_count = 5
    requiem_timer = None
    requiem = False

    bullet = pygame.image.load("game_files/images/bullet.png").convert_alpha()
    bullet2 = pygame.image.load("game_files/images/bullet2.png").convert_alpha()
    bullets = []
    bullet_speed = 60
    bullets_left = 4
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
            fireball_rect = fireball.get_rect(topleft=(fireball_x, fireball_y))

            if ghosts >= ghosts_sum_for_win:
                ghost_speed = 0
                player_speed = 0
                load_win(screen, sound_bg)
                return

            for i in range(lives):
                screen.blit(heart, (1115 - (50 * i), 30))

            if ghost_list_in_game:
                for i, el in enumerate(ghost_list_in_game):
                    screen.blit(ghost, el)
                    el.x -= ghost_speed

                    if el.x < -20:
                        ghost_list_in_game.pop(i)
                        ghosts += 1

                    if el.x in range(1000, 1015):
                        fireballs.append(fireball_rect)

                    if player_rect.colliderect(el):
                        if lives <= 1:
                            gameplay = False
                        else:
                            lives -= 1
                            ghost_list_in_game.pop(i)
                        ghosts += 1
                        data[1] = str(int(data[1]) + 1)
                        open("game_files/base.txt", "w", encoding="utf-8").write("\n".join(data))

            if fireballs:
                for i, ball in enumerate(fireballs):
                    screen.blit(fireball, ball)
                    ball.x -= fireball_speed

                    if player_rect.colliderect(ball):
                        if lives <= 1:
                            gameplay = False
                        else:
                            lives -= 1
                        fireballs.pop(i)

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
                                try:
                                    bullets.pop(i)
                                except:
                                    pass
                                ghosts += 1
                                data[1] = str(int(data[1]) + 1)
                                open("game_files/base.txt", "w", encoding="utf-8").write("\n".join(data))

            animation += 1
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
                walk = walk_left
            elif keys[pygame.K_RIGHT] and player_x < 1100:
                player_x += player_speed
                walk = walk_right
            elif keys[pygame.K_q]:
                sound_bg.stop()
                return


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
                bullets_left = 4
                lives = 3
                ghosts = 0
                zawarudo_count = 5
            elif quit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                sound_bg.stop()
                return

        try:
            pygame.display.update()
        except:
            pass


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    screen.fill((255, 255, 255))
            elif event.type == ghost_timer and not zawarudo:
                ghost_list_in_game.append(ghost.get_rect(topleft=(1300, ghost_y)))
                fireball_x = 1000
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
                fireball_speed = 0
                bullet_speed = 0
                zawarudo_count -= 1
                sound_bg.set_volume(0)
                sound_zawarudo.play()
                zawarudo_timer = pygame.USEREVENT + 2
                pygame.time.set_timer(zawarudo_timer, 5000)
            elif event.type == zawarudo_timer and zawarudo:
                platform_img = platform_img1
                ghost_speed = 15
                bullet_speed = 60
                fireball_speed = 25
                zawarudo = False
                sound_bg.set_volume(50)
            elif gameplay and event.type == pygame.KEYUP and event.key == pygame.K_x and not requiem and zawarudo_count > 0:
                for i, ghost_ in enumerate(ghost_list_in_game):
                    if ghost_.x in range(player_rect.x, player_rect.x + 250):
                        ghost_.x -=  300
                        screen.blit(ghost, ghost_)

                for i, fireball_ in enumerate(fireballs):
                    if fireball_.x in range(player_rect.x, player_rect.x + 450):
                        fireball_.x -= 370
                        screen.blit(fireball, fireball_)
                zawarudo_count -= 1
                ghost_speed = 0
                bullet_speed = 0
                fireball_speed = 0
                sound_bg.set_volume(0)
                sound_requiem.play()
                platform_img = platform_img2
                requiem = True
                requiem_timer = pygame.USEREVENT + 3
                pygame.time.set_timer(requiem_timer, 3000)
            elif event.type == requiem_timer and requiem:
                platform_img = platform_img1
                ghost_speed = 15
                fireball_speed = 25
                bullet_speed = 60
                requiem = False
                sound_bg.set_volume(50)
        clock.tick(30)

