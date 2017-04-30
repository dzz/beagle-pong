from .game_objects.paddle import paddle
from .game_objects.hud import hud

class game():
    def __init__(self):
        self.tickables = []

    def init(self):
        self.left_paddle = paddle()
        self.hud = hud()
        self.tickables.append(self.left_paddle)

    def tick(self):
        for tickable in self.tickables:
            tickable.tick()

    def render(self):
        #self.left_paddle.render()
        self.hud.render()

    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
