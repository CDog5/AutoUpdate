import pygame
WIDTH,HEIGHT = 1300,600
BLACK = (0,0,0)
WHITE = (255,255,255)
SQRSIZE = (int(WIDTH/40),int(HEIGHT/40))
pygame.init()
display = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_grid(window):
    rows = int(HEIGHT / SQRSIZE[1])
    gap = WIDTH // rows
    for i in range(rows):
        pygame.draw.line(window,WHITE,(0,i*gap),(WIDTH,i*gap))
        for j in range(rows):
            pygame.draw.line(window,WHITE,(j*gap,0),(j*gap,WIDTH))
class Vector2:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
class Vector3:
    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
class Object:
    def __init__(self,x,y,size):
        self.pos = Vector2(x,y)
        self.width = size[0] * SQRSIZE[0]
        self.height = size[1]* SQRSIZE[1]
    def move_down(self):
        self.pos.y += SQRSIZE[1]
    def move_up(self):
        self.pos.y -=SQRSIZE[1]
    def move_left(self):
        self.pos.x -=SQRSIZE[0]
    def move_right(self):
        self.pos.x +=SQRSIZE[0]
    def draw(self):
        pygame.draw.rect(display,WHITE,(int(self.pos.x),int(self.pos.y),self.width,self.height))
obj = Object(0,0,(5,5))
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                obj.move_left()
            if event.key == pygame.K_RIGHT:
                obj.move_right()
            if event.key == pygame.K_UP:
                obj.move_up()
            if event.key == pygame.K_DOWN:
                obj.move_down()
    display.fill(BLACK)
    draw_grid(display)
    obj.draw()
    pygame.display.update()
