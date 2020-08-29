import pygame
from pygame import mouse
from snowflake import Snowflake

def main():
    pygame.init()

    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    done = False

    snowflake = Snowflake()
    
    while not done:
        time_passed_seconds = clock.tick(120)/1000.0
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                
                if event.key == pygame.K_SPACE:
                    snowflake = Snowflake()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                snowflake.addPoint(mousePos)

        screen.fill((0, 0, 0))
        snowflake.render(screen, mousePos)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
    
