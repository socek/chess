import pyglet
import gui


def run():
    window = pyglet.window.Window()

    @window.event
    def on_draw():
        window.clear()
        # yolo
