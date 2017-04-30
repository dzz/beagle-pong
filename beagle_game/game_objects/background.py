from client.beagle.beagle_api import api as bgl
from client.beagle.assets import assets

class background():
    speed = 0.1

    def __init__(self):
        self.primitive = bgl.primitive.unit_uv_square
        self.t = 0
        self.shader = assets.get("pong/shader/background")

    def tick(self):
        self.t += background.speed

    def get_shader_params(self):
        return { "t" : self. t } 

    def render(self):
        self.primitive.render_shaded( self.shader, self.get_shader_params() )

