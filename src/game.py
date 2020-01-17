import pygame
import engine as eng
import rect as rect
import animations as anim
import tilemap as tm
import character as char
import vec2 as vec2
import movement_info as mi

gravity = 1
jump_speed = -8
move_speed = 5
max_move_speed = 8
horizontal_wall_jump_speed = 10
vertical_wall_jump_speed = -10
forced_move_dir = 0
forced_move_counter = 0
forced_move_total_frames = 5

gravity_on_wall = 1
accel_in_air = 2
accel_on_ground = 1
deccel_in_air = 2
deccel_on_ground = 1

# Movement info from last frame
movement_info = None
desired_movement = None

player = None
current_tilemap = None
camera = None

# Replace with actual input system
up = False
down = False
left = False
right = False
jump = False

def game_init():
    global player
    player_rect = rect.init_rect(150, 150, 15, 15)
    player = char.init_character(player_rect, player_rect, anim.Animations(), 20, 20, 20, 20, 20)
    
    global movement_info
    movement_info = mi.Movement_Info()
    global desired_movement
    desired_movement = vec2.Vec2()

    global current_tilemap
    tile_ids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

    current_tilemap = tm.tilemap_init(20, 20, 16, 16, 10, 10, tile_ids, collision,
                                        "../assets/bricks2.png", None)
    current_tilemap.src_rect = rect.init_rect(0, 0, current_tilemap.tile_width, current_tilemap.tile_height)

    global camera
    camera = vec2.Vec2()

def game_update():
    global player
    global movement_info
    global forced_move_dir
    global forced_move_counter

   # if movement_info.col_up == True:
   #     desired_movement.y = 0
   # if (left == True and forced_move_dir != 1) or forced_move_dir == -1:
   #     desired_movement.x += -move_speed
   # elif (right == True and forced_move_dir != -1) or forced_move_dir == 1:
   #     desired_movement.x += move_speed
   # elif movement_info.col_down == True:
   #     desired_movement.x = 0
   # if jump == True and movement_info.col_down == True:
   #     desired_movement.y = jump_speed
   # elif jump == True and movement_info.col_down == False and movement_info.col_left == True:
   #     desired_movement.y = vertical_wall_jump_speed
   #     desired_movement.x = horizontal_wall_jump_speed
   #     forced_move_dir = 1
   #     forced_move_counter = forced_move_total_frames
   # elif jump == True and movement_info.col_down == False and movement_info.col_right == True:
   #     desired_movement.y = vertical_wall_jump_speed
   #     desired_movement.x = -horizontal_wall_jump_speed
   #     forced_move_dir = -1
   #     forced_move_counter = forced_move_total_frames
    # Player Movement
    # In air
    if movement_info.col_down == False:
        # In air touching wall on left side
        if movement_info.col_left == True:
            if left == True:
                desired_movement.y = gravity_on_wall
            else:
                desired_movement.y += gravity
            if jump == True:
                desired_movement.y = vertical_wall_jump_speed
                desired_movement.x = horizontal_wall_jump_speed
            if right == True:
                desired_movement.x += accel_in_air
        # In air touching wall on right side
        elif movement_info.col_right == True:
            if right == True:
                desired_movement.y = gravity_on_wall
            else:
                desired_movement.y += gravity
            if jump == True:
                desired_movement.y = vertical_wall_jump_speed
                desired_movement.x = -horizontal_wall_jump_speed
            if left == True:
                desired_movement.x += -accel_in_air
        # In air not touching wall
        else:            
            # Acceleration
            desired_movement.y += gravity
            if left == True:
                desired_movement.x += -accel_in_air
            elif right == True:
                desired_movement.x += accel_in_air
            # Decceleration
            elif desired_movement.x < 0:
                if desired_movement.x + deccel_in_air >= 0:
                    desired_movement.x = 0
                else:
                    desired_movement.x += deccel_in_air
            elif desired_movement.x > 0:
                if desired_movement.x - deccel_in_air <= 0:
                    desired_movement.x = 0
                else:
                    desired_movement.x -= deccel_in_air
    # On Ground
    else:
        # Acceleration
        desired_movement.y = gravity
        if jump == True:
            desired_movement.y = jump_speed
        elif left == True:
            desired_movement.x += -accel_on_ground
        elif right == True:
            desired_movement.x += accel_on_ground
        # Decceleration
        # Switch to ground accel/deccel
        elif desired_movement.x < 0:
            if desired_movement.x + deccel_in_air >= 0:
                desired_movement.x = 0
            else:
                desired_movement.x += deccel_in_air
        elif desired_movement.x > 0:
            if desired_movement.x - deccel_in_air <= 0:
                desired_movement.x = 0
            else:
                desired_movement.x -= deccel_in_air
        


    desired_movement.x = max(-max_move_speed, min(desired_movement.x, max_move_speed))
    movement_info = tm.tilemap_collision(desired_movement.x, desired_movement.y, player.box_collider, current_tilemap)
    if forced_move_dir != 0:
        forced_move_counter -= 1
        if forced_move_counter <= 0:
            forced_move_dir = 0

    # Move player
    player.box_collider.x += movement_info.movement.x
    player.box_collider.y += movement_info.movement.y
    # Center camera on player
    camera.x = -player.box_collider.x + (eng.screen_width/2)
    camera.y = -player.box_collider.y + (eng.screen_height/2)

def game_render():
    tm.tilemap_render(current_tilemap, camera)
    pygame.draw.rect(eng.screen, [255, 0, 0], [player.box_collider.x + camera.x, player.box_collider.y + camera.y, player.box_collider.w, player.box_collider.h])

