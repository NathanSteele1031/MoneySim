import pygame, random
import map, people, menu

def main():
    pygame.init()
    display = pygame.display.set_mode((840, 480))
    clock = pygame.time.Clock()

    person_info_panel = menu.PersonPanel(640, 0, 840, 480)
    person_selected = None
    time_paused = False
    world_map = map.Map(640, 480)
    world_map.objects.append(people.Person(245, 245))

    running = True
    while running:
        pygame.display.set_caption("FPS: " + str(int(clock.get_fps())) + " Objects: " + str(len(world_map.objects)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    world_map.objects.append(people.Person(245, 245))
                if event.key == pygame.K_SPACE:
                    time_paused = not time_paused
        
        mouse_pos = pygame.mouse.get_pos()
        person_selected = None
        for obj in world_map.objects:
            if type(obj) == people.Person:
                if mouse_pos[0] > obj.x - 5 and mouse_pos[0] < obj.x + 5 and mouse_pos[1] > obj.y - 5 and mouse_pos[1] < obj.y + 5:
                    person_selected = obj
                
        
        display.fill((0, 255, 0))
        person_info_panel.draw(display)
        person_info_panel.display_person_info(display, person_selected)
        world_map.show_lines(display)
        for obj in world_map.objects:
            obj.draw(display)
            if random.randint(0, 50) == 0 and not time_paused:
                obj.random_move()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()