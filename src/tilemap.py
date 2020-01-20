import math
import pygame
import os
import engine as eng
import rect as rect
import vec2 as vec2
import movement_info as mi

class Tilemap():
    map_width = 0
    map_height = 0
    tile_width = 0
    tile_height = 0
    tileset_width = 0
    tileset_height = 0
    # Tileset source img
    source = None
    # Rects for drawing
    src_rect = None
    # IDs for drawing
    tile_ids = []
    # IDs for collision
    collision = []

# Returns instantiated tilemap
def tilemap_init(map_width, map_height, tile_width, tile_height, 
                tileset_width, tileset_height, tile_ids, 
                collision, src_img_name, src_rect):
    print(os.getcwd());
    new_tilemap = Tilemap()
    new_tilemap.map_width = map_width
    new_tilemap.map_height = map_height
    new_tilemap.tile_width = tile_width
    new_tilemap.tile_height = tile_height   
    new_tilemap.tileset_width = tileset_width
    new_tilemap.tileset_height = tileset_height
    new_tilemap.tile_ids = tile_ids
    new_tilemap.collision = collision
    new_tilemap.source = pygame.image.load(os.path.join('assets/', src_img_name))
    new_tilemap.src_rect = src_rect
    return new_tilemap

def tilemap_collision(movement_x, movement_y, collider, tilemap):

    movement_sign = vec2.Vec2()
    movement_sign.x = int(math.copysign(1, movement_x))
    movement_sign.y = int(math.copysign(1, movement_y))

    collider_grid_pos1 = vec2.Vec2() # Top left corner
    collider_grid_pos2 = vec2.Vec2() # Bottom right corner
    movement_info = mi.Movement_Info()
    movement_info.movement = vec2.Vec2()
    modified_movement = vec2.Vec2()
    collision_id_1 = 0
    collision_id_2 = 0

    # Y Collision
    while modified_movement.y != movement_y and movement_y != 0:
        modified_movement.y += movement_sign.y

        # Update collider grid positions
        collider_grid_pos1.x = int((collider.x + modified_movement.x) / tilemap.tile_width)
        collider_grid_pos2.x = int((collider.x + modified_movement.x + collider.w) / tilemap.tile_width)
        collider_grid_pos1.y = int((collider.y + modified_movement.y) / tilemap.tile_height)
        collider_grid_pos2.y = int((collider.y + modified_movement.y + collider.h) / tilemap.tile_height)

        if movement_sign.y < 0:
            collision_id_1 = tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos1.x)]
            collision_id_2 = tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos1.x)]

            if collision_id_1 == 2 or collision_id_2 == 2:
                movement_info.col_lethal = True
                return movement_info
            elif collision_id_1 == 3 or collision_id_2 == 3:
                movement_info.col_finish = True
                return movement_info
            elif collision_id_1 == 1 or collision_id_2 == 1:
                modified_movement.y -= movement_sign.y
                movement_info.col_up = True
                break

        elif movement_sign.y > 0:
            collision_id_1 = tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos1.x)]
            collision_id_2 = tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos2.x)]

            if collision_id_1 == 2 or collision_id_2 == 2:
                movement_info.col_lethal = True
                return movement_info
            elif collision_id_1 == 3 or collision_id_2 == 3:
                movement_info.col_finish = True
                return movement_info
            elif collision_id_1 == 1 or collision_id_2 == 1:
                modified_movement.y -= movement_sign.y
                movement_info.col_down = True
                break

    # X Collision
    while modified_movement.x != movement_x and movement_x != 0:
        modified_movement.x += movement_sign.x

        # Update collider grid positions
        collider_grid_pos1.x = int((collider.x + modified_movement.x) / tilemap.tile_width)
        collider_grid_pos2.x = int((collider.x + modified_movement.x + collider.w) / tilemap.tile_width)
        collider_grid_pos1.y = int((collider.y + modified_movement.y) / tilemap.tile_height)
        collider_grid_pos2.y = int((collider.y + modified_movement.y + collider.h) / tilemap.tile_height)

        if movement_sign.x < 0:
            collision_id_1 = tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos1.x)]
            collision_id_2 = tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos1.x)]

            if collision_id_1 == 2 or collision_id_2 == 2:
                movement_info.col_lethal = True
                return movement_info
            elif collision_id_1 == 3 or collision_id_2 == 3:
                movement_info.col_finish = True
                return movement_info
            elif collision_id_1 == 1 or collision_id_2 == 1:
                modified_movement.x -= movement_sign.x
                movement_info.col_left = True
                break

        elif movement_sign.x > 0:
            collision_id_1 = tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos2.x)]
            collision_id_2 = tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos2.x)]

            if collision_id_1 == 2 or collision_id_2 == 2:
                movement_info.col_lethal = True
                return movement_info
            elif collision_id_1 == 3 or collision_id_2 == 3:
                movement_info.col_finish = True
                return movement_info
            elif collision_id_1 == 1 or collision_id_2 == 1:
                modified_movement.x -= movement_sign.x
                movement_info.col_right = True
                break

    movement_info.movement = modified_movement
    return movement_info

def tilemap_render(tilemap, camera):
    for x in range(tilemap.map_width):
        for y in range(tilemap.map_height):
            tile_id = tilemap.tile_ids[(y * tilemap.map_width) + x]
            if tile_id == -1: continue
            tile_x = int((tile_id % tilemap.tileset_width) * tilemap.tile_width)
            tile_y = int(math.floor(tile_id / tilemap.tileset_width) * tilemap.tile_width)
            src_rect = [tile_x, tile_y, tilemap.src_rect.w, tilemap.src_rect.h]
            eng.screen.blit(tilemap.source, (x * tilemap.tile_width + camera.x, y * tilemap.tile_height + camera.y), src_rect)