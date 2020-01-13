import pygame
import engine as eng
import rect as rect
import animations as anim
import tilemap as tm
import character as char

player = None
current_tilemap = None

up = False
down = False
left = False
right = False

def game_init():
    global player
    player_rect = rect.init_rect(70, 70, 15, 15)
    player = char.init_character(player_rect, player_rect, anim.Animations(), 20, 20, 20, 20, 20)
    
    global current_tilemap
    tile_ids = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,1,-1,-1,5,5,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

    current_tilemap = tm.tilemap_init(20, 10, 16, 16, 10, 10, tile_ids, collision,
                                        "../assets/bricks2.png", None)
    current_tilemap.src_rect = rect.init_rect(0, 0, current_tilemap.tile_width, current_tilemap.tile_height)

def game_update():
    global player
    x = y = 0
    if up == True:
        y = -1
    elif down == True:
        y = 1
    if left == True:
        x = -1
    elif right == True:
        x = 1
    movement = tm.tilemap_collision(x *5, y *5, player.box_collider, current_tilemap)
    player.box_collider.x += movement.x
    player.box_collider.y += movement.y

def game_render():
    tm.tilemap_render(current_tilemap)
    pygame.draw.rect(eng.screen, [255, 0, 0], [player.box_collider.x, player.box_collider.y, player.box_collider.w, player.box_collider.h])

