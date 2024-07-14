import pygame, sys
from but import Button
import subprocess

pygame.init()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("7.jpg").convert_alpha()

def create_button(image, pos, text_input, base_color, hovering_color):
    return Button(image, pos, text_input, get_font(75), base_color, hovering_color)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("turok.ttf", size)

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
    SCREEN.blit(scaled_bg, (0, 0))



def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        draw_bg()
        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

       
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        
        buttons = [
            create_button(pygame.image.load("Play Rect.png"), (640, 250), "PLAY", "#d7fcd4", "White"),
            create_button(pygame.image.load("Options Rect.png"), (640, 400), "OPTIONS", "#d7fcd4", "White"),
            create_button(pygame.image.load("Quit Rect.png"), (640, 550), "QUIT", "#d7fcd4", "White"),
        ]
        MENU_MOUSE_POS = pygame.mouse.get_pos()
      
       
        
        

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(BG, (0, 0))
        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.checkForInput(MENU_MOUSE_POS):
                        if button.text_input == "PLAY":
                            subprocess.run(["python", "map.py"])
                        elif button.text_input == "OPTIONS":
                            options()
                        elif button.text_input == "QUIT":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()

main_menu()