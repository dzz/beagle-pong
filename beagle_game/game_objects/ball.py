from client.beagle.beagle_api import api as bgl
from client.beagle.assets import assets

from .arena import arena

class ball():

    base_vel = 0.12
    render_position_smoothing_filter_coef = 0.8

    min_y = -1* arena.height
    max_y = arena.height
    collision_min_x = -1 * arena.width_inner
    collision_max_x = arena.width_inner
    score_min_x = -1 * arena.width_outer
    score_max_x = 1 * arena.width_outer
    english_decay = 1.0 - (2.5/60)

    def __init__(self, **kwargs):

        self.primitive = bgl.primitive.unit_uv_square
        self.shader = assets.get("beagle-2d/shader/beagle-2d")
        self.view = assets.get("beagle-2d/coordsys/16:9")
        self.texture = assets.get("pong/texture/ball")

        self.left_paddle = kwargs["left_paddle"]
        self.right_paddle = kwargs["right_paddle"]

        self.reset()

    def reset(self):
        self.active = True
        self.render_x = 0
        self.render_y = 0
        self.x = 0
        self.y = 0
        self.vx = -1 * ball.base_vel
        self.vy = 1 * ball.base_vel
        self.english = 0
        self.rotation = 0

    def check_collision( self, paddle ):

        bounds = paddle.get_y_collision_bounds()
        if( self.y > bounds[0] ) and ( self.y < bounds[1] ):
            self.english = paddle.get_english()
            self.vx *=-1
            self.x += self.vx
        else:
            self.active = False

    def tick(self):
        self.english *= ball.english_decay
        self.x = self.x + self.vx
        self.y = self.y + self.vy + self.english


        if(self.y > ball.max_y):
            self.english *= -1
            self.vy *= -1
            self.y = ball.max_y + self.vy
        if(self.y < ball.min_y):
            self.english *= -1
            self.vy *= -1
            self.y = ball.min_y + self.vy

        if(self.active):
            if(self.x < ball.collision_min_x ):
                self.check_collision( self.left_paddle )
            if(self.x > ball.collision_max_x ):
                self.check_collision( self.right_paddle )

        if(self.x < ball.score_min_x ):
            self.reset()
        if(self.x > ball.score_max_x ):
            self.reset()

        self.render_x = self.render_x * ( 1 - ball.render_position_smoothing_filter_coef ) + ( self.x * ball.render_position_smoothing_filter_coef )
        self.render_y = self.render_y * ( 1 - ball.render_position_smoothing_filter_coef ) + ( self.y * ball.render_position_smoothing_filter_coef )

    def get_shader_params(self):
        return {
            "texBuffer"            : self.texture,
            "translation_local"    : [ 0.0,0.0],
            "scale_local"          : [ 0.25, 0.25 ],
            "translation_world"    : [ self.render_x, self.render_y ],
            "scale_world"          : [ 1, 1],
            "view"                 : self.view,
            "rotation_local"       : self.english,
            "filter_color"         : [ 1.0, 1.0, 1.0, 1.0],
            "uv_translate"         : [ 0,0 ] }

    def render(self):
        self.primitive.render_shaded( self.shader, self.get_shader_params() )


