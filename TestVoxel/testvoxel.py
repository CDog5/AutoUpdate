import pygame
import handler, consts

class Cube:
    def __init__(self,x=0,y=0,z=0):
        self.rl_pos = consts.Position(x,y,z)
        self.ig_sizes = consts.Position(1,1,1)
        self.rl_sizes = self.ig_sizes.to_scrsize()
    def draw(self):
        rect = pygame.Rect(self.rl_pos.x,self.rl_pos.y,self.rl_sizes.x,self.rl_sizes.y)
        pygame.draw.rect(WINDOW,consts.C_GREEN,rect)
WINDOW = pygame.display.set_mode(consts.SIZE)
pygame.display.set_caption('Voxel Sim')
def draw(objects):
    WINDOW.fill(consts.C_BLUE)
    for obj in objects:
        obj.draw()
    pygame.display.update()
def main():
    objects = [Cube()]
    run = True
    while run:
    
        handler.handleEvents(pygame.event.get(),objects)
            
        draw(objects)
    pygame.quit()
if __name__ == '__main__':
    main()