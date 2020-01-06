import math
import ../engine as eng
import rect as rect

#TODO add vec2 class

class Tilemap():
    map_width = 0
    map_height = 0
    tile_width = 0
    tile_height = 0
    num_tiles_wide = 0
    num_tiles_high = 0
    source = None
    tile_ids = []
    collision = []

# Returns instantiated tilemap
def tilemap_init(width, height, tile_width, tile_height, num_tiles_wide, num_tiles_wide, tile_ids, collision, src_path):
    new_tilemap = Tilemap()
    new_tilemap.width = width
    new_tilemap.height - height
    new_tilemap.tile_width = tile_width
    new_tilemap.tile_height = tile_height   
    new_tilemap.num_tiles_wide = num_tiles_wide
    new_tilemap.num_tiles_high = num_tiles_high
    #TODO: load tiles/collision from json
    new_tilemap.tile_ids = tile_ids
    new_tilemap.collision = collision
    new_tilemap.source = pygame.image.load(src_path)

def tilemap_collision():
    pass

def tilemap_render(tilemap):
    for x in range(tilemap.width):
        for y in range(tilemap.height):
            tile_id = tilemap.tile_ids[(y * tilemap.map_width) + x]
            tile_x = (int)(tile_id % tilemap.num_tiles_wide) * tilemap.tile_width
            tile_y = (int)floor(tile_id/ tilemap.num_tiles_wide) * tilemap.tile_width
            #TODO: add src and dst to tilemap, include rect
            #eng.screen.blit(tilemap.source, )



                
                
                
                
coords.x = (int)(gid % tileset->number_of_tiles_horizontal) * tileset->tile_width;
coords.y = (int)floor(gid / tileset->number_of_tiles_horizontal) * tileset->tile_width;


    void tilemap_render(const Tilemap *tilemap, const Camera *cam)
{
    for(int x = 0; x < tilemap->map_width; x++)
    {
        for(int y = 0; y < tilemap->map_height; y++)
        {
            Vec2_Int tile = tile_coords_from_gid(tilemap->gid_map[(y * tilemap->map_width) + x], tilemap->tileset);
            tilemap->tileset->src.x = tile.x;
            tilemap->tileset->src.y = tile.y;
            tilemap->tileset->dst.x = x * tilemap->tileset->tile_width + cam->pos.x;
            tilemap->tileset->dst.y = y * tilemap->tileset->tile_height + cam->pos.y;
            SDL_RenderCopy(cam->renderer, tilemap->tileset->tex, &tilemap->tileset->src, &tilemap->tileset->dst);
        }
    }
}