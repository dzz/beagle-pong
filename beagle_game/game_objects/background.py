from client.beagle.beagle_api import api as bgl
from client.beagle.assets import assets

class background():
    speed = 0.003

    def __init__(self, **kwargs ):
        self.primitive = bgl.primitive.unit_uv_square
        self.t = 0
        self.shader = assets.get("pong/shader/background")
        self.motion_blur_shader = assets.get("beagle-2d/shader/passthru_filtered")
        self.ball = kwargs['ball']
        self.input_buffer = kwargs['input_buffer']



    def tick(self):
        self.t += background.speed

    def get_shader_params(self):
        return { 
                "motion_blur_buffer" : self.input_buffer,
                "ball_x" : self.ball.x,
                "ball_english" : self.ball.english * 100
                } 

    def render(self):
        self.primitive.render_shaded( self.shader, self.get_shader_params() )

