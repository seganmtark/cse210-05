import constants

from game.casting.cast import Cast
#from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.casting.cycle2 import Cycle2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    #cast.add_actor("foods", Food())
    cast.add_actor("snake1", Cycle())
    cast.add_actor("snake2", Cycle2())
    score1 = Score()
    score1.set_position(Point(0, 0))
    cast.add_actor("scores1", score1)
    score2 = Score()
    score2.set_position(Point(round(constants.MAX_X-100), 0))
    cast.add_actor("scores2", score2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
