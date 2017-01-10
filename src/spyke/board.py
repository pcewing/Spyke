from spyke.ui.geometry import Rectangle


class GameBoard:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.x = 2
        self.y = 2

    def render(self, stdscr):
        rect = Rectangle()
        rect.x = self.x
        rect.y = self.y
        rect.width = self.width
        rect.height = self.height
        rect.draw(stdscr)
