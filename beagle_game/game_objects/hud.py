from client.beagle.beagle_api import api
from client.beagle.assets import assets

font_size = 8 # default size for lotext font renderer
hud_width_chars = 24
hud_height_chars = 12

class hud():
    def __init__(self): 
        self.render_buffer =  api.framebuffer.from_dims( hud_width_chars * font_size, hud_height_chars * font_size );

    def render(self):
        with api.context.render_target(self.render_buffer):
            api.context.clear(0,1,0,1)
            with api.blendmode.alpha_over:
                api.lotext.render_text_pixels(" ~= BEAGLE PONG =~", 0,0, [1.0,0.0,1.0] )
        self.render_buffer.render_processed( assets.get("beagle-2d/shader/passthru") )
