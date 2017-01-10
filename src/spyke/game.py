import time

from spyke.fruit import FruitSpawner
from spyke.board import GameBoard
from spyke.snake import Snake
from spyke.ui.text import Text


class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr

        # Initialize game options and stats.
        self.loop_duration_ms = 120
        self.loop_count = 0
        self.debug_str = ''
        self.score = 0
        self.running = True

        # Initialize game objects.
        self.game_board = GameBoard()
        self.fruit_spawner = FruitSpawner(self.game_board)
        self.snake = Snake()
        self.snake.add_segment(self.game_board.x + 4, self.game_board.y + 2)
        self.snake.add_segment(self.game_board.x + 3, self.game_board.y + 2)
        self.snake.add_segment(self.game_board.x + 2, self.game_board.y + 2)
        self.snake.direction = 'right'
        self.stdscr.addstr('Game loop {0}'.format(self.loop_count))

    def run(self):
        while self.running is True:
            # Calculate the end of the current frame.
            frame_end = self.time_ms() + self.loop_duration_ms

            self.debug_str = 'Score = {0}'.format(self.score)
            self.loop_count = self.loop_count + 1

            # Update the snake's position/size.
            self.snake.update()

            # Handle collisions.
            self.handle_collisions()

            # Render the screen.
            self.render()

            # Handle input until the end of the frame.
            remaining_ms = frame_end - self.time_ms()
            while remaining_ms > 0:
                self.handle_input(remaining_ms)
                remaining_ms = frame_end - self.time_ms()

    def handle_collisions(self):
        head = self.snake.head()

        # Check for collision with fruit.
        if (self.fruit_spawner.fruit is not None and
                head.x == self.fruit_spawner.fruit.x and
                head.y == self.fruit_spawner.fruit.y):
            self.snake.should_grow = True
            self.score = self.score + 1
            self.fruit_spawner.spawn()

        # Check for collision with self.
        for i in range(1, len(self.snake.segments) - 1):
            segment = self.snake.segments[i]
            if head.x == segment.x and head.y == segment.y:
                self.end()

        # Check for collision with walls.
        if (head.x <= self.game_board.x or
                head.x >= self.game_board.x + self.game_board.width - 1 or
                head.y <= self.game_board.y or
                head.y >= self.game_board.y + self.game_board.height - 1):
            self.end()

    def render(self):
        # Clear the screen
        self.stdscr.clear()

        # Print game stats.
        Text.print_at(self.stdscr, 0, 0, self.debug_str)

        # Print game board and objects.
        self.game_board.render(self.stdscr)
        self.snake.render(self.stdscr)
        self.fruit_spawner.render(self.stdscr)

    def handle_input(self, timeout):
        self.stdscr.timeout(timeout)
        c = self.stdscr.getch()

        if c == ord('q'):
            exit()
        if c == ord(' '):
            self.pause()
        elif c == ord('w'):
            self.snake.change_direction("up")
        elif c == ord('a'):
            self.snake.change_direction("left")
        elif c == ord('s'):
            self.snake.change_direction("down")
        elif c == ord('d'):
            self.snake.change_direction("right")

    def pause(self):
        # TODO: This should store the current time and then recalculate the
        # end of the frame once the game is resumed.
        self.stdscr.timeout(-1)

        self.stdscr.clear()
        Text.print_at(self.stdscr, 0, 0,
                      'Game paused; press <SPACE> to continue...')

        while True:
            c = self.stdscr.getch()

            if c == ord(' '):
                break

        self.render()

    def end(self):
        self.running = False
        self.stdscr.clear()
        Text.print_at(self.stdscr, 0, 0,
                      'Game over! Your score was {0}.'.format(self.score))
        Text.print_at(self.stdscr, 0, 1, 'Press <q> to quit....')

        while True:
            c = self.stdscr.getch()

            if c == ord('q'):
                break
    def time_ms(self):
        return int(time.time() * 1000)
