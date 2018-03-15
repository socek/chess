import pyglet 
from itertools import product
import os

DIRPATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FIGURE_IMAGE_PATH = os.path.join('images', '{color}-{figure}.png')

FIGURES = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
COLORS = ['black', 'white']
IMAGE_SIZE = 64


class Gui(object):
    WIDTH = 8
    HEIGHT = 8

    figure_images = None

    def __init__(self, board):
        self.board = board

    def load_images(self):
        self.figure_images = {
            (color, figure): self.load_figure_image(color, figure)
            for figure in FIGURES
            for color in COLORS
        }

        self.cell_images = [
           pyglet.resource.image('images/black-cell.png'),
           pyglet.resource.image('images/white-cell.png') 
        ]

    def load_figure_image(self, color, figure):
        path = FIGURE_IMAGE_PATH.format(color=color, figure=figure)
        return pyglet.resource.image(path)

    def get_figure_image(self, figure):
        figure_name = figure.name
        color = figure.player.color

        return self.figure_images[color, figure_name]

    def run(self):
        width = self.WIDTH * IMAGE_SIZE
        height = self.HEIGHT * IMAGE_SIZE
        window = pyglet.window.Window(width=width, height=height)

        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        @window.event()
        def on_draw():
            window.clear()
            self.on_draw(window)

        pyglet.app.run()
            
    def on_draw(self, window):
        widths = range(self.WIDTH)
        heights = range(self.HEIGHT)
        cords = product(widths, heights)
        for x, y in cords:
            xx = x * IMAGE_SIZE
            yy = y * IMAGE_SIZE

            cell_image = self.cell_images[(x + y) % 2]
            cell_image.blit(yy, xx)

            figure = self.board.get_figure(x, y)
            if figure is None:
                continue
            image = self.get_figure_image(figure)
            image.blit(yy, xx)

