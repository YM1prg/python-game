import pygame, sys
from but import Button
import subprocess

pygame.init()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("6.png")

def create_button(image, pos, text_input, base_color, hovering_color):
    return Button(image, pos, text_input, get_font(50), base_color, hovering_color)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("G.otf", size)

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
    SCREEN.blit(scaled_bg, (0, 00))




def main_menu():
    while True:
        
        buttons = [
            create_button(pygame.image.load("Play Rect.png"), (200, 250), "Forest", "#d7fcd4", "White"),
            create_button(pygame.image.load("play Rect.png"), (650, 250), "The Hall", "#d7fcd4", "White"),
            create_button(pygame.image.load("play Rect.png"), (1100, 250), "Wizard Villages", "#d7fcd4", "White"),
             create_button(pygame.image.load("play Rect.png"), (650, 500), "City", "#d7fcd4", "White"),
        ]
        MENU_MOUSE_POS = pygame.mouse.get_pos()
      
       
        
        

        MENU_TEXT = get_font(50).render("MAP Selection", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(BG, (0, 0))
        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(200, 250), 
                            text_input="Forest", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("play Rect.png"), pos=(650, 250), 
                            text_input="The Hall", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("play Rect.png"), pos=(1100, 250), 
                            text_input="Wizard Villages", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        MAP = Button(image=pygame.image.load("play Rect.png"), pos=(650, 500), 
                            text_input="City", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON,MAP]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.checkForInput(MENU_MOUSE_POS):
                        if button.text_input == "Forest":
                            subprocess.run(["python", "main.py"])
                        elif button.text_input == "The Hall":
                            subprocess.run(["python", "giha/brawler_tut-main/main.py"])
                        elif button.text_input == "Wizard Villages":
                            subprocess.run(["python", "wizards_map/main_code.py"])
                        elif button.text_input == "City":
                            subprocess.run(["python", "Abdo/main.py"])

        pygame.display.update()

main_menu()