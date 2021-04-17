SIZE = (900,500)
C_WHITE = (255,255,255)
C_BLUE = (135,206,235)
C_GREEN = (0,255,0)
class Position:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def to_scrsize(self):
        return Position(self.x*50,self.y*50,self.z*50)
    def __str__(self):
        return f'X: {self.x}, Y: {self.y}, Z: {self.z}'
