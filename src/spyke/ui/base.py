class UiObject:
    def __init__(self):
        self.x = 0
        self.y = 0


class UiControl(UiObject):
    def __init__(self):
        UiObject.__init__(self)
        self.x = 0
        self.y = 0
