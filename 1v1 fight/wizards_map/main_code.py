
import pygame
from pygame import mixer
from fighters_code import Fighter

mixer.init()
pygame.init()

# Get the screen's width and height
screen_width = 1000
screen_height = 600

# Create the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brawlers")

# set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours and load health bar
RED = (255, 0, 0)
BLACK = (0, 0, 0)
health_bar_left = pygame.image.load("wizards_map/assets_1/images_1/icons/health_bar_left.png")
health_bar_left = pygame.transform.scale(health_bar_left, (400, 40))
health_bar_right = pygame.image.load("wizards_map/assets_1/images_1/icons/health_bar_right.png")
health_bar_right = pygame.transform.scale(health_bar_right, (400, 40))

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000


#define fighter variables
wizard_size = 250
wizard_scale = 3.7
wizard_offset = [112, 105]
wizard_data = [wizard_size, wizard_scale, wizard_offset]
worrior_size = 128
worrior_scale = 3
worrior_offset = [20, 50]
worrior_data = [worrior_size, worrior_scale, worrior_offset]  
               
#load music and sounds
pygame.mixer.music.load("wizards_map/assets_1/sounds_1/game_loop.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
fireball = pygame.mixer.Sound("wizards_map/assets_1/sounds_1/fireball.mp3")
fireball.set_volume(0.6)
electric_shock = pygame.mixer.Sound("wizards_map/assets_1/sounds_1/electric-shock.mp3")
electric_shock.set_volume(0.6)

#load background image
bg_image = pygame.image.load("wizards_map/assets_1/images_1/theme_3.jpeg").convert_alpha()


#load spritesheets
wizard_sheet = pygame.image.load("wizards_map/assets_1/images_1/wizard/wizard.png").convert_alpha()
worrior_sheet = pygame.image.load("wizards_map/assets_1/images_1/worrior/warrior.png").convert_alpha()


#load vicory image
victory_img = pygame.image.load("wizards_map/assets_1/images_1/icons/victory.png").convert_alpha()


#define number of steps in each animation
wizard_steps = [8, 8, 1, 8, 8, 3, 7]
worrior_steps = [8, 8, 8, 7, 9, 4, 4]


#define font
count_font = pygame.font.Font("wizards_map/assets_1/fonts_1/turok.ttf", 80)
score_font = pygame.font.Font("wizards_map/assets_1/fonts_1/turok.ttf", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0, 0))

#function for drawing fighter LEFT health bars
def draw_left_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, BLACK, (x, y, 350, 20))
  pygame.draw.rect(screen, RED, (x, y, 350 * ratio, 20))
  screen.blit(health_bar_left, (10, 20))

#function for drawing fighter RIGHT health bars
def draw_right_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, BLACK, (x, y, 350, 20))
  pygame.draw.rect(screen, RED, (x, y, 350 * ratio, 20))
  screen.blit(health_bar_right, (590, 20))

#create two instances of fighters
fighter_1 = Fighter(1, 200, 310, False, wizard_data, wizard_sheet, wizard_steps, fireball)
fighter_2 = Fighter(2, 700, 310, True, worrior_data, worrior_sheet, worrior_steps, electric_shock)

# Game loop
run = True
while run:

  clock.tick(FPS)

  #draw background
  draw_bg()

  #show player stats
  draw_left_health_bar(fighter_1.health, 50, 30)
  draw_right_health_bar(fighter_2.health, 595, 30)
  draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
  draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)

  #update countdown
  if intro_count <= 0:
    #move fighters
    fighter_1.move(screen_width, screen_height, screen, fighter_2, round_over)
    fighter_2.move(screen_width, screen_height, screen, fighter_1, round_over)
  else:
    #display count timer
    draw_text(str(intro_count), count_font, RED, screen_width / 2, screen_height / 3)
    #update count timer
    if (pygame.time.get_ticks() - last_count_update) >= 1000:
      intro_count -= 1
      last_count_update = pygame.time.get_ticks()

  #update fighters
  fighter_1.update()
  fighter_2.update()

  #draw fighters
  fighter_1.draw(screen)
  fighter_2.draw(screen)

  #check for player defeat
  if round_over == False:
    if fighter_1.alive == False:
      score[1] += 1
      round_over = True
      round_over_time = pygame.time.get_ticks()
    elif fighter_2.alive == False:
      score[0] += 1
      round_over = True
      round_over_time = pygame.time.get_ticks()
  else:
    #display victory image
    screen.blit(victory_img, (360, 150))
    if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
      round_over = False
      intro_count = 3
      fighter_1 = Fighter(1, 200, 310, False, wizard_data, wizard_sheet, wizard_steps, fireball)
      fighter_2 = Fighter(2, 700, 310, True, worrior_data, worrior_sheet, worrior_steps, electric_shock)

  #event handler
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

  # Update display
  pygame.display.update()

# Exit Pygame
pygame.quit()
