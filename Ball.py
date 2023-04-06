import arcade as arc
from math import sin, cos, degrees


class Ball(arc.SpriteCircle):
    def __init__(self):
        super().__init__(25, arc.color.RED)
        self.parent = None
        self.pymunk_phys = None

    def on_update(self, delta_time: float = 1 / 60):
        # update pymunk physics and usual variables with pymunk ones
        if self.pymunk_phys:
            self.angle += degrees(self.change_angle)
            self.pymunk_phys.body.angle += self.change_angle
            print(self.angle, self.pymunk_phys.body.angle)

            # prevent player from going outside area
            self.pymunk_phys.body._set_position((self.center_x, self.center_y))
