import pygame, random, curses, time
import map, people, menu, items

terminal_view = True

def main_window():
    pygame.init()
    display = pygame.display.set_mode((840, 480))
    clock = pygame.time.Clock()

    person_info_panel = menu.PersonPanel(640, 0, 840, 480)
    person_selected = None
    item_info_panel = menu.ItemPanel(640, 25, 840, 455)
    item_selected = None
    time_paused = False
    world_map = map.Map(640, 480)

    running = True
    while running:
        pygame.display.set_caption("FPS: " + str(int(clock.get_fps())) + " Objects: " + str(len(world_map.objects)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    world_map.objects.append(people.Person(245, 245))
                if event.key == pygame.K_i:
                    world_map.objects.append(items.Item("Test"))
                    world_map.objects[-1].set_cord(245, 245)
                if event.key == pygame.K_SPACE:
                    time_paused = not time_paused
        
        mouse_pos = pygame.mouse.get_pos()
        person_selected = None
        item_selected = None
        for obj in world_map.objects:
            if type(obj) == people.Person:
                if mouse_pos[0] > obj.x - 5 and mouse_pos[0] < obj.x + 5 and mouse_pos[1] > obj.y - 5 and mouse_pos[1] < obj.y + 5:
                    person_selected = obj
            if issubclass(type(obj), items.Item) or obj == items.Item:
                if mouse_pos[0] > obj.x - 5 and mouse_pos[0] < obj.x + 5 and mouse_pos[1] > obj.y - 5 and mouse_pos[1] < obj.y + 5:
                    item_selected = obj
        
        display.fill((0, 255, 0))
        person_info_panel.draw(display)
        person_info_panel.display_person_info(display, person_selected)
        item_info_panel.draw(display)
        item_info_panel.display_item_info(display, item_selected)
        world_map.show_lines(display)
        for obj in world_map.objects:
            obj.draw(display)
            if random.randint(0, 50) == 0 and not time_paused and type(obj) == people.Person:
                obj.random_move()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def main_terminal():
    world_map = map.TerminalMap(119, 30)

    stdscr = curses.initscr()
    curses.start_color()
    curses.curs_set(0)
    while True:

        # Add to terminal here
        world_map.draw(stdscr)

        stdscr.refresh()
        time.sleep(0.1)
        stdscr.clear()

if __name__ == "__main__":
    if terminal_view:
        main_terminal()
    else:
        main_window()