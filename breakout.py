from graphics import BulletinBoard
from graphics import Rectangle, Circle, TextBox


class BreakoutGame:

    def __init__(self, config):
        self.board = BulletinBoard(config.get_board_width(),
                                   config.get_board_height())
        brick = Rectangle(self.board.get_width(), 
                          self.board.get_height() * 0.3, 
                          "#0000FF",
                          filled=True, 
                          outlined=config.outline_bricks())
        self.board.pin(brick, 0, 0.1 * self.board.get_height())

    def start(self):
        pass