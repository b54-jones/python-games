class Square:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def get_color(self):
        if self.value == 0:
            return (192, 192, 192)
        elif self.value == 2:
            return (224,224,224)
        elif self.value == 4:
            return (229,255,204)
        elif self.value == 8:
            return (255,204,153)
        elif self.value == 16:
            return (255,128,0)
        elif self.value == 32:
            return (255,102,102)
        elif self.value == 64:
            return(255,0,0)
        elif self.value == 128:
            return(255,255,102)
        elif self.value == 256:
            return(204,204,0)
        else:
            return (153,255,255)