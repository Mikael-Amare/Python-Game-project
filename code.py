#!/usr/bin/env python3
"""
Created by: Mikael Amare
Created on: May 2024
This program is the "Space Aliens" program on the PyBadge
"""

import ugame
import stage
import time
import supervisor
import constants
import random


def splash_scene():
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    while True:
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    text = []

    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)

    background.tile(2, 2, 0)
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)

    background.tile(2, 3, 0)
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)

    background.tile(2, 4, 0)
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)

    background.tile(2, 5, 0)
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()

def game_scene():
    # this function is the main game game_scene

    def show_alien():
        # this function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    background = stage.Grid(image_bank_background, constants.SCREEN_X, constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(2, 3)
            background.tile(x_location, y_location, tile_picked)

    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    
    # for score
    alien_count = 0

    score = 0

    score_text = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("score: {0}".format(score))

    # lasers(pew pew)
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # create list of lasers for when we shoot
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # place 1 alien on the screen
    show_alien()

    # create a stage for the background to show up on
    #    and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites, items show up in order
    game.layers = [score_text] + aliens + lasers + [ship] + [background]
    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED
                )
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # each frame move the aliens down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    if score > 0:
                        score -= 1
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))

# each frame check if any of the lasers are touching any of the alien
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y, 
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            # add 1 to the score
                            score += 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            alien_count = alien_count + 1
        # each frame check if any aliens are touching the space ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens [alien_number].y,
                                 aliens[alien_number].x + 15, aliens [alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)
        
        # redraw Sprite
        game.render_sprites(aliens + lasers + [ship])
        game.tick()  # wait until refresh rate finishes

def game_over_scene(final_score):
    # this function is the game ofver scen
    # turn off sound from last scene
    sound = ugame.audio
    sound.stop()

    # image banks for CircutPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # add text objects
    text = []
    
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)
    
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the backgroundto show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show upin order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you willonly render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick # wait until refresh rate finishes


if __name__ == "__main__":
    splash_scene()
