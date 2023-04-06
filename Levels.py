import arcade as arc
from arcade.pymunk_physics_engine import PymunkPhysicsEngine
import Globals
from Player import BasicPlayer


def new_area(game):
    area_pymunk(game)


def area_one(game):
    game.scene = arc.Scene()
    game.scene.add_sprite_list("player")

    game.player = BasicPlayer()
    game.scene.add_sprite("player", game.player)

    game.camera = arc.Camera(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
    game.gui_camera = arc.Camera(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
    game.physics_engine = arc.PhysicsEngineSimple(game.player, [])


def area_pymunk(game):
    game.camera = arc.Camera(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
    game.gui_camera = arc.Camera(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
    game.physics_engine = arc.PymunkPhysicsEngine(damping=Globals.DAMPING, gravity=Globals.GRAVITY)

    game.scene = arc.Scene()
    game.scene.add_sprite_list("player")
    game.scene.add_sprite_list_after("ball", "player")
    game.scene.add_sprite_list_after("world", "ball")

    # Player Spanws
    game.player = BasicPlayer()
    game.player.center_y = 50
    game.player.center_x = 50
    game.scene.add_sprite("player", game.player)
    game.physics_engine.add_sprite(game.player, friction=Globals.P_FRICTION,
                                   moment_of_inertia=PymunkPhysicsEngine.MOMENT_INF,
                                   damping=0.01, collision_type="player", max_velocity=400)
    game.player.pymunk_phys = game.physics_engine.get_physics_object(game.player)

    # World Gen
    floor = arc.SpriteSolidColor(Globals.SCREEN_WIDTH, 25, arc.color.GREEN)
    floor.center_x = Globals.SCREEN_WIDTH / 2
    game.scene.add_sprite("world", floor)
    game.physics_engine.add_sprite(floor, body_type=1, friction=Globals.F_FRICTION)

    # generate first goal
    # goal post
    goal1a = arc.SpriteSolidColor(int(Globals.GOAL_WIDTH/5), Globals.GOAL_HEIGHT, color=arc.color.BLUE)
    goal1a.center_x = goal1a.width / 2
    goal1a.center_y = (goal1a.height / 2) + ((floor.height / 2) + floor.center_y)
    # goal crossbar
    goal1b = arc.SpriteSolidColor(Globals.GOAL_WIDTH, int(Globals.GOAL_HEIGHT/5), color=arc.color.BLUE)
    goal1b.center_x = goal1b.width / 2
    goal1b.center_y = goal1a.center_y + (goal1a.height / 2)

    # generate second goal
    # goal post
    goal2a = arc.SpriteSolidColor(int(Globals.GOAL_WIDTH/5), Globals.GOAL_HEIGHT, color=arc.color.RED)
    goal2a.center_x = Globals.SCREEN_WIDTH - goal2a.width / 2
    goal2a.center_y = (goal1a.height / 2) + ((floor.height / 2) + floor.center_y)
    # goal crossbar
    goal2b = arc.SpriteSolidColor(Globals.GOAL_WIDTH, int(Globals.GOAL_HEIGHT/5), color=arc.color.RED)
    goal2b.center_x = Globals.SCREEN_WIDTH - goal2b.width / 2
    goal2b.center_y = goal2a.center_y + (goal2a.height / 2)

    game.scene.add_sprite("world", goal1a)
    game.scene.add_sprite("world", goal1b)
    game.scene.add_sprite("world", goal2a)
    game.scene.add_sprite("world", goal2b)

