class Color:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def get_color(self):
        return self.red, self.green, self.blue
