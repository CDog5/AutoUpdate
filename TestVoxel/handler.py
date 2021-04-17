import pygame

def handleEvents(events,objects):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pass
            #print(f'Unhandled keydown: {pygame.key.name(event.key)}')
    return objects

    
        
            