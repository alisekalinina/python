import pygame
import sys
from game import ImageButton

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Escape Room")
main_background = pygame.image.load("escp.png")

def main_menu():
    green_button = ImageButton(width/2-(295/2), 150, 295, 75, "green_button.jpg", "green_button.jpg", "green_button_hover.jpg", "click.mp3")
    options = ImageButton(width/2-(295/2), 250, 295, 75, "options.jpg", "options.jpg", "options2.jpg", "click2.mp3")
    red_button = ImageButton(width/2-(295/2), 350, 295, 75, "red_button.jpg", "red_button.jpg", "red_button_hover.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0)) 
        screen.blit(main_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == options:
                print("Options button was pressed")
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == red_button:
                running = False
                pygame.quit()
                sys.exit()

        for btn in [green_button, options, red_button]:
            btn.handle_event(event)
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def settings_menu():
    newgame = ImageButton(width/2-(295/2), 250, 295, 75, "newgame.jpg", "newgame.jpg", "newgame2.jpg", "click2.mp3")
    back = ImageButton(width/2-(295/2), 350, 295, 75, "back.jpg", "back.jpg", "back2.jpg", "click.mp3")

    running = True
    while running:
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            
            newgame.handle_event(event)
            back.handle_event(event)

            
            if event.type == pygame.MOUSEBUTTONDOWN and back.is_hovered:
                main_menu()

        
        newgame.check_hover(pygame.mouse.get_pos())
        newgame.draw(screen)
        back.check_hover(pygame.mouse.get_pos())
        back.draw(screen)

        pygame.display.flip()



def new_game():
    back = ImageButton(width/2-(295/2), 350, 295, 75, "back.jpg", "back.jpg", "back2.jpg", "click.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Welcome to the game!", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width/2, height/2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        for btn in [back]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
