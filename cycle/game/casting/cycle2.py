import constants
from game.casting.cycle import Cycle
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

class Cycle2(Cycle):
    """
    A cycle that will continuously grow in length throughout the game.
     
    The responsibility of Cycle is to move itself.

    Attributes:
        _prepare_body: This will create the body of the second cycle
    """

    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 4)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.GREEN if i == 0 else constants.GREEN

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment) 