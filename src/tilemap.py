import math
import pygame
import engine as eng
import rect as rect

#TODO add vec2 class

class Tilemap():
    map_width = 0
    map_height = 0
    tile_width = 0
    tile_height = 0
    tileset_width = 0
    tileset_height = 0
    # Tileset source
    source = None
    # Rects for drawing
    src_rect = None
    dst_rect = None
    # IDs for drawing
    tile_ids = []
    # IDs for collision
    collision = []

# Returns instantiated tilemap
def tilemap_init(map_width, map_height, tile_width, tile_height, 
                tileset_width, tileset_height, tile_ids, 
                collision, src_path, src_rect, dst_rect):
    new_tilemap = Tilemap()
    new_tilemap.map_width = map_width
    new_tilemap.map_height = map_height
    new_tilemap.tile_width = tile_width
    new_tilemap.tile_height = tile_height   
    new_tilemap.tileset_width = tileset_width
    new_tilemap.tileset_height = tileset_height
    #TODO: load tiles/collision from json
    new_tilemap.tile_ids = tile_ids
    new_tilemap.collision = collision
    new_tilemap.source = pygame.image.load(src_path)
    new_tilemap.src_rect = src_rect
    new_tilemap.dst_rect = dst_rect
    return new_tilemap

def tilemap_collision():
    pass

def tilemap_render(tilemap):
    for x in range(tilemap.map_width):
        for y in range(tilemap.map_height):
            tile_id = tilemap.tile_ids[(y * tilemap.map_width) + x]
            tile_x = (int)((tile_id % tilemap.tileset_width) * tilemap.tile_width)
            tile_y = int(math.floor(tile_id / tilemap.tileset_width) * tilemap.tile_width)
            src_rect = [tile_x, tile_y, tilemap.src_rect.w, tilemap.src_rect.h]
            dst_rect = [x * tilemap.tile_width, y * tilemap.tile_height, tilemap.dst_rect.w, tilemap.dst_rect.h]
            eng.screen.blit(tilemap.source, (x * tilemap.tile_width, y * tilemap.tile_height), src_rect)