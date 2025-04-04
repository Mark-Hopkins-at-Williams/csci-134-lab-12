from config import SIMPLE, CLASSIC, BUNSEN
from graphics import Window, Rectangle, Circle, Textbox
from random import uniform
from sys import argv

# Reads the command-line argument that specifies the game mode
modes = {'simple': SIMPLE, 'classic': CLASSIC, 'bunsen': BUNSEN}
if len(argv) > 1 and argv[1] in modes:
    config = modes[argv[1]]
else:
    print('Please provide a valid game mode ("simple", "classic", "bunsen").')
    print('Usage: python breakout.py MODE')
    exit()

window = Window(width=config['window width'],
                height=config['window height'],
                title="BREAKOUT!")
brick = Rectangle(width=config['window width'], 
                  height=config['window width'] * 0.3, 
                  fill_color="#0000FF",
                  outline_color="black")
window.paste(brick, 0, 0.1 * config['window height'])

quit_now = False
while not quit_now:
    quit_now = window.refresh()
