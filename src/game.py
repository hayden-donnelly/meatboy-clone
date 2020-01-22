import pygame
import engine as eng
import rect as rect
import animations as anim
import tilemap as tm
import character as char
import vec2 as vec2
import movement_info as mi
import levels as lv

# 0 = main menu, 1 = in game, 2 = game complete
game_state = 0

# Movement variables
gravity = 1
jump_speed = -8
move_speed = 5
max_move_speed = 10
horizontal_wall_jump_speed = 10
vertical_wall_jump_speed = -10
gravity_on_wall = 1
accel_in_air = 3
accel_on_ground = 4
deccel_in_air = 1
deccel_on_ground = 3

# Movement info from last frame
movement_info = None
desired_movement = None

player = None
camera = None

start_x = 150
start_y = 150

# TODO: replace with actual input system
up = False
down = False
left = False
right = False
jump = False
jump_key_released = False

def game_init():
    global player
    player_rect = rect.init_rect(150, 150, 15, 15)
    player = char.init_character(player_rect, player_rect, anim.Animations(), 20, 20, 20, 20, 20)
    
    global movement_info
    movement_info = mi.Movement_Info()
    global desired_movement
    desired_movement = vec2.Vec2()

    global camera
    camera = vec2.Vec2()

    # Loads all levels into array
    lv.load_levels()

def game_update():
    global game_state
    if game_state == 1:   # In Game
        global player
        global movement_info
        global desired_movement

        # Player Movement
        # In air
        if movement_info.col_down == False:
            # In air touching wall on left side
            if movement_info.col_left == True:
                #if left == True:
                desired_movement.y = gravity_on_wall
                #else:
                    #desired_movement.y += gravity
                if jump == True:
                    desired_movement.y = vertical_wall_jump_speed
                    desired_movement.x = horizontal_wall_jump_speed
                if right == True:
                    desired_movement.x += accel_in_air
            # In air touching wall on right side
            elif movement_info.col_right == True:
                #if right == True:
                desired_movement.y = gravity_on_wall
                #else:
                #    desired_movement.y += gravity
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
            if movement_info.col_up == True:
                desired_movement.y = 0
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
        movement_info = tm.tilemap_collision(desired_movement.x, desired_movement.y, player.box_collider, lv.levels[lv.current_level_id].tilemap)
        
        # Finished level
        if movement_info.col_finish == True:
            if lv.current_level_id + 1 < len(lv.levels):
                lv.current_level_id += 1
                player.box_collider.x = lv.levels[lv.current_level_id].start_x
                player.box_collider.y = lv.levels[lv.current_level_id].start_y
            else:
                game_state = 2  # Game Complete
        # PLayer collided with lethal object and was killed
        elif movement_info.col_lethal == True:
            desired_movement = vec2.Vec2()
            player.box_collider.x = lv.levels[lv.current_level_id].start_x
            player.box_collider.y = lv.levels[lv.current_level_id].start_y

        # Move player
        player.box_collider.x += movement_info.movement.x
        player.box_collider.y += movement_info.movement.y
        # Center camera on player
        camera.x = -player.box_collider.x + (eng.screen_width/2)
        camera.y = -player.box_collider.y + (eng.screen_height/2)
    elif game_state == 0:   # Main Menu
        if jump == True:
            game_state = 1
            lv.current_level_id = 0
            player.box_collider.x = lv.levels[lv.current_level_id].start_x
            player.box_collider.y = lv.levels[lv.current_level_id].start_y
    elif game_state == 2:   # Game Complete
        if jump == True:
            game_state = 0

def game_render():
    if game_state == 1:
        # Draw tilemap
        tm.tilemap_render(lv.levels[lv.current_level_id].tilemap, camera)
        # Draw player
        pygame.draw.rect(eng.screen, [255, 0, 0], [player.box_collider.x + camera.x, player.box_collider.y + camera.y, player.box_collider.w, player.box_collider.h])
    elif game_state == 0:
        pass
    elif game_state == 2:
        pass

