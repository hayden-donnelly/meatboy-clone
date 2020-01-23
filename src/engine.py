import pygame
import game as gme

# Global Engine Variables
screen_width = 500
screen_height = 500
display_caption = "Meatboy Clone"
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
                elif event.key == pygame.K_s:
                    gme.down = True
                elif event.key == pygame.K_a:
                    gme.left = True
                elif event.key == pygame.K_d:
                    gme.right = True
                elif event.key == pygame.K_SPACE:
                    gme.jump = True
                elif event.key == pygame.K_t:
                    gme.start = True
                elif event.key == pygame.K_r:
                    gme.restart = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    gme.up = False
                elif event.key == pygame.K_s:
                    gme.down = False
                elif event.key == pygame.K_a:
                    gme.left = False
                elif event.key == pygame.K_d:
                    gme.right = False
                elif event.key == pygame.K_SPACE:
                    gme.jump = False
                elif event.key == pygame.K_t:
                    gme.start = False
                elif event.key == pygame.K_r:
                    gme.restart = False

        if running == False:
            break
        
        gme.game_update()
        engine_render()
        #TODO: add proper timer
        pygame.time.delay(20)