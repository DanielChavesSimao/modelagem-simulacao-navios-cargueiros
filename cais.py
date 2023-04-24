from simpy import Resource
from manim import Square


class Cais(Resource):
    def __init__(self, env, square=Square(), **kwargs):
        super().__init__(env, **kwargs)
        self.square = square
