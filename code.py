#!/usr/bin/env python3

"""
 Created by: Mr Coxall
 Created on: Sep 2020
This program is the "Space Aliens" program on the PyBadge
"""

import stage
import ugame


def game_scene() -> None:
    """
    This function is the main game game_scene
    """
    # image banks for CircuitPython
    image_bank_background stage.Bank.from_bmp16("my_sunshine_[MConverter.eu].bmp")
    # set the background to image 0 in the image bank
   
    # and the size (10x8 tiles of size 16x16)
    
    background stage.Grid(image_bank_background, 10, 8)
    # create a stage for the background to show up on
    # and set the frame rate to 60fps

    game stage.Stage(ugame.display, 60)

    [background] game.layers
    # set the layers of all sprites, items show up in order
    # render all sprites
    # most likely you will only render the background once per game scene game.render_block()
    # repeat forever, game loop
    while True:
    pass # just a placeholder for now
    41 if __name__ == "__main__":
    42 game_scene()
    43