

class SnakeSegment:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    segments = []
    direction = 'right'

    def __init__(self):
        self.should_grow = False

    def add_segment(self, x, y):
        self.segments.append(SnakeSegment(x, y))

    def render(self, stdscr):
        head = True
        for segment in self.segments:
            if head is True:
                stdscr.addch(segment.y, segment.x, 'O')
                head = False
            else:
                stdscr.addch(segment.y, segment.x, '+')

    def update(self):
        if self.should_grow is True:
            self.grow()
            self.should_grow = False
        else:
            self.move()

    def move(self):
        current_head = None
        if len(self.segments) < 1:
            return
        if len(self.segments) == 1:
            current_head = self.segments.pop(len(self.segments) - 1)
        elif len(self.segments) > 1:
            self.segments.pop(len(self.segments) - 1)
            current_head = self.segments[0]

        x = current_head.x
        y = current_head.y

        if self.direction == "up":
            self.segments.insert(0, SnakeSegment(x, y - 1))
        elif self.direction == "down":
            self.segments.insert(0, SnakeSegment(x, y + 1))
        elif self.direction == "left":
            self.segments.insert(0, SnakeSegment(x - 1, y))
        elif self.direction == "right":
            self.segments.insert(0, SnakeSegment(x + 1, y))

    def grow(self):
        current_head = None
        if len(self.segments) < 1:
            return
        else:
            current_head = self.segments[0]

        x = current_head.x
        y = current_head.y

        if self.direction == "up":
            self.segments.insert(0, SnakeSegment(x, y - 1))
        elif self.direction == "down":
            self.segments.insert(0, SnakeSegment(x, y + 1))
        elif self.direction == "left":
            self.segments.insert(0, SnakeSegment(x - 1, y))
        elif self.direction == "right":
            self.segments.insert(0, SnakeSegment(x + 1, y))

    def change_direction(self, direction):
        head = self.segments[0]
        neck = self.segments[1]

        if direction == "up":
            if not head.y == neck.y + 1:
                self.direction = "up"
        elif direction == "down":
            if not head.y == neck.y - 1:
                self.direction = "down"
        elif direction == "left":
            if not head.x == neck.x + 1:
                self.direction = "left"
        elif direction == "right":
            if not head.x == neck.x - 1:
                self.direction = "right"

    def head(self):
        return self.segments[0]
