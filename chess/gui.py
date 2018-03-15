import pyglet 

IMAGE_PATH = 'images/{color}-{figure}.png'

FIGURES = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
COLORS = ['black', 'white']


def load_figure_image(color, figure):
    path = IMAGE_PATH.format(color=color, figure=figure)
    return pyglet.resource.image(path)


IMAGES = {
    (color, figure): load_figure_image(color, figure)
    for figure in FIGURES
    for color in COLORS
}

