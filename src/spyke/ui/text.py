from spyke.ui.colors import Colors


class Text():
    @staticmethod
    def print_at(stdscr, x, y, text, fg=Colors.FOREGROUND,
                 bg=Colors.BACKGROUND):
        stdscr.addstr(y, x, text, Colors.color_pair(bg, fg))
