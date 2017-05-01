from client.beagle.beagle_api import api as bgl
from client.beagle.assets import assets

from .game_objects.paddle import paddle
from .game_objects.ball import ball
from .game_objects.paddle_controller import paddle_controller
from .game_objects.hud import hud
from .game_objects.background import background

class game():
    def __init__(self):
        self.tickables = []

    def new_tickable( self, tickable ):
        self.tickables.append( tickable )
        return tickable

    def init(self):
        self.last_frame = bgl.framebuffer.from_screen()
        self.current_frame = bgl.framebuffer.from_screen()
        self.left_paddle = self.new_tickable( paddle( side = "left", controller = paddle_controller( mode = "human_leftstick")  ) )
        self.right_paddle =self.new_tickable( paddle( side = "right", controller = paddle_controller( mode = "human_rightstick" ) ) )
        self.ball = self.new_tickable( ball( left_paddle = self.left_paddle, right_paddle = self.right_paddle ) )

        self.background = self.new_tickable( background( ball = self.ball, input_buffer = self.last_frame ) )


        self.hud = hud()


    def tick(self):
        for tickable in self.tickables:
            tickable.tick()

    def render(self):

        ##copy the curent frame to last frame for use in
        ##feedback effects

        with bgl.context.render_target(self.last_frame):
            self.current_frame.render_processed( assets.get("beagle-2d/shader/passthru") )

        with bgl.context.render_target(self.current_frame):
            bgl.context.clear(1,1,1,0)
            with bgl.blendmode.alpha_over:
                self.background.render()
                self.left_paddle.render()
                self.right_paddle.render()
                self.ball.render()

        self.current_frame.render_processed( assets.get("beagle-2d/shader/passthru") )

        with bgl.blendmode.alpha_over:
            self.hud.render()


    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
