from spyke.ui.base import UiObject
from spyke.ui.text import Text
from spyke.ui.colors import Colors


class Line(UiObject):
    def __init__(self):
        UiObject.__init__(self)
        self.length = 0
        self.orientation = 'horizontal'
        self.char = ' '
        self.fg = Colors.WHITE
        self.bg = Colors.GREEN

    def draw(self, stdscr):
        if self.orientation == 'horizontal':
            for i in range(self.x, self.x + self.length):
                Text.print_at(stdscr, i, self.y, self.char, self.fg,
                              self.bg)
        elif self.orientation == 'vertical':
            for i in range(self.y, self.y + self.length):
                Text.print_at(stdscr, self.x, i, self.char, self.fg,
                              self.bg)


class Rectangle(UiObject):
    def __init__(self):
        UiObject.__init__(self)
        self.width = 0
        self.height = 0

        self.border_char = ' '
        self.border_fg = Colors.BACKGROUND
        self.border_bg = Colors.FOREGROUND
        self.fill_char = ' '
        self.fill_fg = Colors.FOREGROUND
        self.fill_bg = Colors.BACKGROUND

    def draw(self, stdscr):
        self._draw_border(stdscr)
        self._draw_fill(stdscr)

    def _draw_border(self, stdscr):
        border_top = self._create_border_line()
        border_top.x = self.x
        border_top.y = self.y
        border_top.length = self.width
        border_top.orientation = 'horizontal'
        border_top.draw(stdscr)

        border_bottom = self._create_border_line()
        border_bottom.x = self.x
        border_bottom.y = self.y + self.height - 1
        border_bottom.length = self.width
        border_bottom.orientation = 'horizontal'
        border_bottom.draw(stdscr)

        border_left = self._create_border_line()
        border_left.x = self.x
        border_left.y = self.y
        border_left.length = self.height
        border_left.orientation = 'vertical'
        border_left.draw(stdscr)

        border_right = self._create_border_line()
        border_right.x = self.x + self.width - 1
        border_right.y = self.y
        border_right.length = self.height
        border_right.orientation = 'vertical'
        border_right.draw(stdscr)

    def _create_border_line(self):
        l = Line()
        l.char = self.border_char
        l.fg = self.border_fg
        l.bg = self.border_bg
        return l

    def _create_fill_line(self):
        l = Line()
        l.char = self.fill_char
        l.fg = self.fill_fg
        l.bg = self.fill_bg
        return l

    def _draw_fill(self, stdscr):
        for y in range(self.y + 1, self.y + self.height - 1):
            fill_line = self._create_fill_line()
            fill_line.x = self.x + 1
            fill_line.y = y
            fill_line.length = self.width - 2
            fill_line.orientation = 'horizontal'
            fill_line.draw(stdscr)
