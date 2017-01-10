import curses

from spyke.game import Game
from spyke.ui.colors import Colors


def main(stdscr):
    Colors.init()
    curses.curs_set(0)

    game = Game(stdscr)
    game.run()


if __name__ == "__main__":
    curses.wrapper(main)
