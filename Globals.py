from PIL import Image
from Misc_Functions import tint_image
from copy import deepcopy


SCREEN_TITLE = "Pymunk Demo VER 1.0"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MID_SCREEN_X = SCREEN_WIDTH / 2
MID_SCREEN_Y = SCREEN_HEIGHT / 2

SCREEN_PERCENTS = (SCREEN_WIDTH / 1080, SCREEN_HEIGHT / 720)
SCREEN_PERCENT = (SCREEN_PERCENTS[0] + SCREEN_PERCENTS[1]) / 2


AREA_WIDTH = 10000
AREA_HEIGHT = 10000

# inputs
DEADZONE = .1

# Player stuff
# forwards driving speeds
PLAYER_MAX_SPEED = 10
PLAYER_ACCELERATION_SPEED = .4

# backwards driving speeds
PLAYER_BACK_MAX_SPEED = PLAYER_MAX_SPEED / 1.2
PLAYER_BACK_ACCELERATION_SPEED = PLAYER_ACCELERATION_SPEED / 1.2

# other speed stuff
PLAYER_DEACCELERATION_SPEED = PLAYER_ACCELERATION_SPEED / 2
PLAYER_DRIFT_SPEED = PLAYER_MAX_SPEED / 1.3

PLAYER_ROTATION_SPEED = .1

# Camera
LEFT_VIEWPORT_MARGIN = int(SCREEN_WIDTH * .3)
RIGHT_VIEWPORT_MARGIN = int(SCREEN_WIDTH * .3)
BOTTOM_VIEWPORT_MARGIN = int(SCREEN_HEIGHT * .3)
TOP_VIEWPORT_MARGIN = int(SCREEN_HEIGHT * .3)

CAMERA_SPEED = .3

# physics
DAMPING = .5
GRAVITY = (0, -1500)

P_FRICTION = .8
P_MOVE_FORCE = 4000

F_FRICTION = 1

# World stuff
GOAL_WIDTH = int(50 * SCREEN_PERCENTS[0])
GOAL_HEIGHT = int(100 * SCREEN_PERCENTS[1])


# particles
PARTICLE_SHAPE = Image.open("Resources/Particles/p_shape_round.png")
RED = "#f80000"
ORANGE = "#f8891d"
YELLOW = "#f8e91d"
GRAY = "#797979"
gray_part = tint_image(deepcopy(PARTICLE_SHAPE), GRAY)
red_part = tint_image(deepcopy(PARTICLE_SHAPE), RED)
orange_part = tint_image(deepcopy(PARTICLE_SHAPE), ORANGE)
yellow_part = tint_image(deepcopy(PARTICLE_SHAPE), ORANGE)


# Helper functions
def resize_screen(width: int, height: int):
    global SCREEN_WIDTH, SCREEN_HEIGHT, MID_SCREEN_X, SCREEN_PERCENTS, SCREEN_PERCENT, PLAYER_MAX_SPEED, \
        PLAYER_BACK_MAX_SPEED, PLAYER_DRIFT_SPEED

    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height

    MID_SCREEN_X = SCREEN_WIDTH / 2

    SCREEN_PERCENTS = (SCREEN_WIDTH / 1080, SCREEN_HEIGHT / 720)
    SCREEN_PERCENT = (SCREEN_PERCENTS[0] + SCREEN_PERCENTS[1]) / 2

    PLAYER_MAX_SPEED = 10 * SCREEN_PERCENT
    PLAYER_BACK_MAX_SPEED = PLAYER_MAX_SPEED / 1.2
    PLAYER_DRIFT_SPEED = PLAYER_MAX_SPEED / 1.3
