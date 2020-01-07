class Animations():
    animation_index = 0
    animation_frame_index = 0
    # Animation frames (images)
    animations = []
    # Hitbox frames (rects)
    hitboxes = []
    # Hurtbox frames (rects)
    hurtboxes = []

# Returns instantiated animations
def init_animations(animations, hitboxes, hurtboxes):
    new_animations = Animations()
    #TODO: this
    #new_animations[0] = pygame.image.load(os.path.join("../assets/tileset.png))
    return new_animations