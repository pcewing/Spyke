import random


class Fruit:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class FruitSpawner:
    def __init__(self, game_board):
        self.game_board = game_board
        self.spawn()

    def should_spawn(self):
        return self.fruit is None

    def spawn(self):
        x = random.randint(self.game_board.x + 1,
                           self.game_board.width + self.game_board.x - 2)
        y = random.randint(self.game_board.y + 1,
                           self.game_board.height + self.game_board.y - 2)
        self.fruit = Fruit(x, y)

    def render(self, stdscr):
        if self.fruit is not None:
            stdscr.addch(self.fruit.y, self.fruit.x, '@')
