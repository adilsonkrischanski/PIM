import cv2

class Pixel():
    def __init__(self, value, i, j):
        self.i = i
        self.j = j
        self.value = value

    def is_marked(self):
        return self.rot != 0

    def to_string(self):
        return f"posicao{self.i}:{self.j} valor{self.value} lable = {self.rot}"
