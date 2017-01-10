import curses


class Colors:
    BLACK = 0x0
    DARK_BLACK = 0x8
    RED = 0x1
    DARK_RED = 0x9
    GREEN = 0x2
    DARK_GREEN = 0xa
    YELLOW = 0x3
    DARK_YELLOW = 0xb
    BLUE = 0x4
    DARK_BLUE = 0xc
    MAGENTA = 0x5
    DARK_MAGENTA = 0xd
    CYAN = 0x6
    DARK_CYAN = 0xe
    WHITE = 0x7
    DARK_WHITE = 0xf

    FOREGROUND = 0xc
    BACKGROUND = 0x8

    color_pairs = {}

    @staticmethod
    def init():
        for i in range(0, 16):
            for j in range(0, 16):
                if i == 0 and j == 0:
                    Colors.color_pairs[(0, 0)] = 0
                else:
                    index = i * 16 + j
                    Colors.color_pairs[(i, j)] = index
                    curses.init_pair(index, j, i)

    @staticmethod
    def color_pair(foreground, background):
        return curses.color_pair(Colors.color_pairs[(foreground, background)])
