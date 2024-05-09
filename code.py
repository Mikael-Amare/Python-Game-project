#!/usr/bin/env python3

"""
 Created by: Mikael Amare
 Created on: May 2024
This program is the "Space Aliens" program on the PyBadge
"""

import stage
import ugame


def game_scene() -> None:
    """
    This function is the main game game_scene
    """
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # set the background to image 0 in the image bank
   
    # and the size (10x8 tiles of size 16x16)
    
    background = stage.Grid(image_bank_background, 10, 8)
    
    #sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    
    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    game.layers = [ship] + [background]
    # set the layers of all sprites, items show up in order
    # render all sprites
    # most likely you will only render the background once per game scene 
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("B")
        if keys & ugame.K_O:
            print("A")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 2, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 2, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 2)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 2)
        # loops & restrictions
        if ship.x > 160:
           ship.move(-16, ship.y)
        elif ship.x < -16:
           ship.move(160, ship.y)
        if ship.y > 112:
           ship.move(ship.x, 112)
        elif ship.y < 0:
           ship.move(ship.x, 0)

        # update game logic

        # Redraw Sprite
        game.render_sprites([ship])
        game.tick() # wait until refresh rate finishes
if __name__ == "__main__":
    game_scene()
