from client.beagle.beagle_api import api as bgl

from .game_objects.paddle import paddle
from .game_objects.ball import ball
from .game_objects.paddle_controller import paddle_controller
from .game_objects.hud import hud

class game():
    def __init__(self):
        self.tickables = []

    def init(self):
        self.left_paddle = paddle( side = "left", controller = paddle_controller( mode = "human_leftstick")  )
        self.right_paddle = paddle( side = "right", controller = paddle_controller( mode = "human_rightstick" ) )
        self.ball = ball( left_paddle = self.left_paddle, right_paddle = self.right_paddle )
        self.hud = hud()
        self.tickables.extend([ self.left_paddle, self.right_paddle, self.ball ])

    def tick(self):
        for tickable in self.tickables:
            tickable.tick()

    def render(self):
        paddle_batch = []

        bgl.context.clear(0,1,0,1)
        with bgl.blendmode.alpha_over:
            self.left_paddle.render()
            self.right_paddle.render()
            self.ball.render()
            self.hud.render()

    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
