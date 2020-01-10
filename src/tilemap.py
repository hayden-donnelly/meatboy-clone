import math
import pygame
import engine as eng
import rect as rect
import vec2 as vec2

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
                collision, src_path, src_rect):
    new_tilemap = Tilemap()
    new_tilemap.map_width = map_width
    new_tilemap.map_height = map_height
    new_tilemap.tile_width = tile_width
    new_tilemap.tile_height = tile_height   
    new_tilemap.tileset_width = tileset_width
    new_tilemap.tileset_height = tileset_height
    new_tilemap.tile_ids = tile_ids
    new_tilemap.collision = collision
    new_tilemap.source = pygame.image.load(src_path)
    new_tilemap.src_rect = src_rect
    return new_tilemap

def tilemap_collision(movement_x, movement_y, collider, tilemap):

    movement_sign = vec2.Vec2()
    movement_sign.x = int(math.copysign(1, movement_x))
    movement_sign.y = int(math.copysign(1, movement_y))

    collider_grid_pos1 = vec2.Vec2() # Top left corner
    collider_grid_pos2 = vec2.Vec2() # Bottom right corner
    modified_movement = vec2.Vec2()

    # Y Collision
    while modified_movement.y != movement_y and movement_y != 0:
        modified_movement.y += movement_sign.y

        # Update collider grid positions
        collider_grid_pos1.x = (collider.x + modified_movement.x) / tilemap.tile_width
        collider_grid_pos2.x = (collider.x + modified_movement.x + collider.w) / tilemap.tile_width
        collider_grid_pos1.y = (collider.y + modified_movement.y) / tilemap.tile_width
        collider_grid_pos2.y = (collider.y + modified_movement.y + collider.h) / tilemap.tile_width

        print(int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos2.x))

        if (movement_sign.y < 0 
        and (tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos1.x)] != 0
        or tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos2.x)] != 0)):
            modified_movement.y -= movement_sign.y
            break
        elif (movement_sign.y > 0 
        and (tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos1.x)] != 0
        or tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos2.x)] != 0)):
            modified_movement.y -= movement_sign.y
            break

    # X Collision
    while modified_movement.x != movement_x and movement_x != 0:
        modified_movement.x += movement_sign.x

        # Update collider grid positions
        collider_grid_pos1.x = (collider.x + modified_movement.x) / tilemap.tile_width
        collider_grid_pos2.x = (collider.x + modified_movement.x + collider.w) / tilemap.tile_width
        collider_grid_pos1.y = (collider.y + modified_movement.y) / tilemap.tile_width
        collider_grid_pos2.y = (collider.y + modified_movement.y + collider.h) / tilemap.tile_width

        if (movement_sign.x < 0
        and (tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos1.x)] != 0
        or tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos1.x)] != 0)):
            modified_movement.x -= movement_sign.x
            break
        elif (movement_sign.x > 0
        and (tilemap.collision[int(collider_grid_pos1.y * tilemap.map_width + collider_grid_pos2.x)] != 0
        or tilemap.collision[int(collider_grid_pos2.y * tilemap.map_width + collider_grid_pos2.x)] != 0)):
            modified_movement.x -= movement_sign.x
            break

    return modified_movement

def tilemap_render(tilemap):
    for x in range(tilemap.map_width):
        for y in range(tilemap.map_height):
            tile_id = tilemap.tile_ids[(y * tilemap.map_width) + x]
            if tile_id == -1: continue
            tile_x = int((tile_id % tilemap.tileset_width) * tilemap.tile_width)
            tile_y = int(math.floor(tile_id / tilemap.tileset_width) * tilemap.tile_width)
            src_rect = [tile_x, tile_y, tilemap.src_rect.w, tilemap.src_rect.h]
            eng.screen.blit(tilemap.source, (x * tilemap.tile_width, y * tilemap.tile_height), src_rect)