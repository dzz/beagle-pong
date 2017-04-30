from .game_objects.paddle import paddle

class game():
    def __init__(self):
        self.tickables = []

    def init(self):
        self.left_paddle = paddle()
        self.tickables.append(self.left_paddle)

    def tick(self):
        for tickable in self.tickables:
            tickable.tick()

    def render(self):
        self.left_paddle.render()

    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
