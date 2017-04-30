from client.beagle.beagle_api import api as bgl
from client.beagle.assets import assets

class paddle():

    base_x = 7
    min_y = -3
    max_y = 3
    collision_height = 1.2

    def __init__(self, **kwargs):
        self.primitive = bgl.primitive.unit_uv_square
        self.shader = assets.get("beagle-2d/shader/beagle-2d")
        self.view = assets.get("beagle-2d/coordsys/16:9")
        self.texture = assets.get("pong/texture/paddle")

        if(kwargs['side'] == 'left'):
            self.x = -1 * paddle.base_x
        if(kwargs['side'] == 'right'):
            self.x = paddle.base_x

        self.controller = kwargs['controller']
        self.y = 0

    def apply_motion(self, y):
        new_y = self.y + y
        new_y = max( min( new_y, paddle.max_y ), paddle.min_y )
        #IIR filter for smoothiness
        self.y = self.y*0.7 + new_y*0.3
    def tick(self):
        self.controller.control(self)
        pass

    def get_y_collision_bounds(self):
        return [ self.y - paddle.collision_height, self.y + paddle.collision_height ]

    def get_shader_params(self):
        return {
            "texBuffer"            : self.texture,
            "translation_local"    : [ 0.0,0.0],
            "scale_local"          : [ 0.5, 1.2 ],
            "translation_world"    : [ self.x, self.y ],
            "scale_world"          : [ 1, 1],
            "view"                 : self.view,
            "rotation_local"       : 0.0 ,
            "filter_color"         : [ 1.0, 1.0, 1.0, 1.0],
            "uv_translate"         : [ 0,0 ] }

    def render(self):
        self.primitive.render_shaded( self.shader, self.get_shader_params() )
