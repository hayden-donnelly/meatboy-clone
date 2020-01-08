import pygame
import engine as eng
import rect as rect
import animations as anim
import tilemap as tm
import character as char

# Tommorrow initialize characters and add input to test tilemap collision

player = None
enemy = None
current_tilemap = None

def game_init():
    #global player
    #player = char.init_character(rect.Rect(), rect.Rect(), anim.Animations(), 20, 20, 20, 20, 20)
    #global enemy
    #enemy = char.init_character(rect.Rect(), rect.Rect(), anim.Animations(), 20, 20, 20, 20, 20)
    
    global current_tilemap
    tile_ids = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,
                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
    current_tilemap = tm.tilemap_init(20, 10, 16, 16, 10, 10, tile_ids, collision,
                                        "../assets/tileset.png", None)
    current_tilemap.src_rect = rect.init_rect(0, 0, current_tilemap.tile_width, current_tilemap.tile_height)
def game_update():
    pass

def game_render():
    tm.tilemap_render(current_tilemap)
    pass

