import pygame
import map

def main():
    pygame.init()
    display = pygame.display.set_mode((640, 480))

    world_map = map.Map(640, 480)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display.fill((0, 255, 0))
        world_map.show_lines(display)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()