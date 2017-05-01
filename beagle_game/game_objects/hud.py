from client.beagle.beagle_api import api as bgl
from client.beagle.assets import assets
from .arena import arena

font_size = 8 # default size for lotext font renderer
hud_width_chars = 24
hud_height_chars = 12

class hud():
    def __init__(self): 
        self.t = 0
        self.render_buffer =  bgl.framebuffer.from_dims( hud_width_chars * font_size, hud_height_chars * font_size )

    def render(self):

        with bgl.context.render_target(self.render_buffer):
            bgl.context.clear(0,0,0,0)
            with bgl.blendmode.alpha_over:
                bgl.lotext.render_text_grid("{0}".format([ arena.score_left, arena.score_right ]), 8,5, [0.0,0.0,0.0] )

        self.render_buffer.render_processed( assets.get("beagle-2d/shader/passthru") )
