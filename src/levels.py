import tilemap as tm
import rect as rect
import copy

class Level():
    tilemap = None
    start_x = 0
    start_y = 0
    name = ""

levels = []
current_level_id = 0
number_of_levels = 2

# "Just throw all the data in the executable"
def load_levels():
    global levels

    # "There is no pythonic way of passing by value", shallow copies don't work and you can't deepcopy pygame surfaces
    # so here we are...
    # Level 1 -----------------------------------------------------------------
    tilemap1 = tm.tilemap_init(0, 0, 16, 16, 50, 50, None, None, 'tileset.png', None)
    tilemap1.src_rect = rect.init_rect(0, 0, tilemap1.tile_width, tilemap1.tile_height)
    new_level1 = Level()
    tilemap1.tile_ids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    tilemap1.collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,
                         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
    tilemap1.map_width = 20
    tilemap1.map_height = 4
    new_level1.tilemap = tilemap1
    new_level1.name = "Wall Jump"
    new_level1.start_x = 18
    new_level1.start_y = 33
    levels.append(new_level1)

    # Level 2 -----------------------------------------------------------------
    tilemap2 = tm.tilemap_init(0, 0, 16, 16, 50, 50, None, None, 'tileset.png', None)
    tilemap2.src_rect = rect.init_rect(0, 0, tilemap2.tile_width, tilemap2.tile_height)
    new_level2 = Level()
    tilemap2.tile_ids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                         1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                         1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                         1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                         1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

    tilemap2.collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                          1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                          1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                          1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                          1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                          1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,
                          1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,]
    tilemap2.map_width = 20
    tilemap2.map_height = 7
    new_level2.tilemap = tilemap2
    new_level2.name = "Wall Jump"
    new_level2.start_x = 18
    new_level2.start_y = 33
    levels.append(new_level2)
    
