import pygame
import engine as eng
import rect as rect
import animations as anim
import tilemap as tm

test_img = None

# Base class for all characters
class Character():
    box_collider = None
    draw_rect = None
    animations = None
    health = 0
    stamina = 0
    attack_speed = 0
    move_speed = 0
    dodge_speed = 0
    
# Returns instantiated character
def init_character(box_collider, draw_rect, animations, health,
                    stamina, attack_speed, move_speed, dodge_speed):
    new_character = Character()
    new_character.box_collider = box_collider
    new_character.draw_rect = draw_rect
    new_character.animations = animations
    new_character.health = health
    new_character.stamina = stamina
    new_character.attack_speed = attack_speed
    new_character.move_speed = move_speed
    new_character.dodge_speed = dodge_speed
    return new_character

player = None
enemy = None
current_tilemap = None

def game_init():
    #global player
    #player = init_character(rect.Rect(), rect.Rect(), anim.Animations(), 20, 20, 20, 20, 20)
    #global enemy
    #enemy = init_character(rect.Rect(), rect.Rect(), anim.Animations(), 20, 20, 20, 20, 20)
    
    #global test_img
    #test_img = pygame.image.load("../assets/tileset.png")
    
    global current_tilemap
    tile_ids = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                1,61,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,1,
                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #temporarily using tile ids for both drawing and collision
    current_tilemap = tm.tilemap_init(20, 10, 16, 16, 10, 10, tile_ids, tile_ids,
                                        "../assets/tileset.png", None, None)
    if current_tilemap == None:
        print("no")
    else:
        print("yes")
    current_tilemap.src_rect = rect.init_rect(0, 0, current_tilemap.tile_width, current_tilemap.tile_height)
    current_tilemap.dst_rect = current_tilemap.src_rect
def game_update():
    pass

def game_render():
    #eng.screen.blit(test_img, (10, 10), (10, 10, 16, 16))
    tm.tilemap_render(current_tilemap)
    pass

