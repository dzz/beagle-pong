from client.beagle.beagle_api import api as bgl
class paddle_controller():
    def __init__(self, **kwargs):
        self.mode = kwargs['mode']

    def control(self, paddle):
        if( self.mode == 'human_leftstick' ):
            paddle.apply_motion( bgl.gamepads.find_primary().left_stick[1] )
        if( self.mode == 'human_rightstick' ):
            paddle.apply_motion( bgl.gamepads.find_primary().right_stick[1] )
