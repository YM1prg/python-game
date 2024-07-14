import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")
# Load the image
image_path = "path/to/your/image.png"
image = pygame.image.load("wow.png")

image1 = pygame.image.load("wow1.png")

# Get the rect object for the image to retrieve its width and height
image_rect = image.get_rect()

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (242, 140, 40)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN=(10,186,181)
#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 3
WARRIOR_OFFSET = [72, 26]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 200
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 54]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#load music and sounds
#load music and sounds
pygame.mixer.music.load("b.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("magic.wav")
magic_fx.set_volume(0.75)

#load background image
bg_image = pygame.image.load("6.png").convert_alpha()

#load spritesheets
warrior_sheet = pygame.image.load("warrior3.png").convert_alpha()
wizard_sheet = pygame.image.load("one5.png").convert_alpha()

#load vicory image
victory_img = pygame.image.load("victory2.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 2, 6, 6, 3, 7]

#define font
count_font = pygame.font.Font("G.otf", 80)
score_font = pygame.font.Font("turok.ttf", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#function for drawing background
def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#function for drawing fighter health bars
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 172, 34))
  pygame.draw.rect(screen, YELLOW, (x, y, 170,30))
  pygame.draw.rect(screen, RED, (x, y, 170 * ratio, 30))


#create two instances of fighters
fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)



#game loop
run = True
while run:

  clock.tick(FPS)

  #draw background
  draw_bg()

  #show player stats
  draw_health_bar(fighter_1.health, 50, 20)
  draw_health_bar(fighter_2.health, 805, 20)
  draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
  draw_text("P2: " + str(score[1]), score_font, RED, 940, 60)

  #update countdown
  if intro_count <= 0:
    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
    fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
  else:
    #display count timer
    draw_text(str(intro_count), count_font, CYAN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
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
  scaled_image = pygame.transform.scale(image, (200, 50))
  screen.blit(scaled_image, (20, 10))
  scaled_image1 = pygame.transform.scale(image1, (200, 50))
  screen.blit(scaled_image1, (800, 10))
  flipped_image = pygame.transform.flip(image1,True,False)

        # Blit the flipped image onto the screen at the specified position
  

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
    screen.blit(victory_img, (280, 150))
    if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
      round_over = False
      intro_count = 3
      fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
      fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  #update display
  pygame.display.update()

#exit pygame
pygame.quit()