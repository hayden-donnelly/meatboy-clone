import pygame
import game as gme

# Global Engine Variables
screen_width = 500
screen_height = 500
display_caption = "Dark Souls Demake"
screen = None
running = True

# Initialize Engine
def engine_init():
    pygame.init()
    global screen
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption(display_caption)

# Render
def engine_render():
    # Clear screen
    screen.fill([0, 0, 0])
    # Render
    gme.game_render()
    # Flip buffer
    pygame.display.flip()

# Game Loop
def loop():
    global running
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    gme.up = True
                if event.key == pygame.K_s:
                    gme.down = True
                if event.key == pygame.K_a:
                    gme.left = True
                if event.key == pygame.K_d:
                    gme.right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    gme.up = False
                if event.key == pygame.K_s:
                    gme.down = False
                if event.key == pygame.K_a:
                    gme.left = False
                if event.key == pygame.K_d:
                    gme.right = False

        if running == False:
            break
        
        gme.game_update()
        engine_render()
        #TODO: add proper timer
        pygame.time.delay(20)