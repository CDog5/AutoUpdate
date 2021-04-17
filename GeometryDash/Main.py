import pygame,random
WIDTH = 700
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.font.init()
pygame.display.set_caption("Geometry Dash")
class Player:
    def __init__(self):
        self.x = 50
        self.y = 450
        self.score = 0
        self.width = 50
        self.height = 50
        self.colour = (0,255,0)
        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self):
        self.score += 0.001
        self.moveleft()
        scrtxt = pygame.font.SysFont('Arial', 30)
        scrtxt = scrtxt.render(str(round(self.score)), False, (255, 255, 255))
        WINDOW.blit(scrtxt,(WIDTH/2,0))
        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(WINDOW,self.colour,self.obj)
    def moveleft(self):
        if self.x > 650:
            self.x = 0 
        else:
            self.x += 0.1
        if self.y < 450:
            self.y += 0.1 
    def up(self):
        if self.y > 50:
            self.y -= 200
class Obstacle:
    def __init__(self):
        self.lifespan = 0
        self.width = random.randint(5,20)*10
        self.height = random.randint(5,20)*10
        self.x = random.randint(50,450) 
        self.y = 450 - (self.height/2)
        
        self.colour = (255,0,0)
        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self):
        self.lifespan +=1
        pygame.draw.rect(WINDOW,self.colour,self.obj)



player = Player()
run = True
obstacles=[]  
obstacle = Obstacle()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.key_code("space"):
                player.up()
    if player.obj.colliderect(obstacle.obj):
        break
    if obstacle.lifespan > 2500:
        obstacle = Obstacle()
    WINDOW.fill((0,0,0))
    obstacle.draw()
    player.draw()
    
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
