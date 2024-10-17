from turtle import *
from superturtle.animation import animate
from superturtle.movement import fly
from shapes import triangle, rectangle
import settings


bgcolor(settings.BACKGROUND_COLOR)


for frame in animate(loop = True):
    for frame in animate(settings.TOTAL_FRAMES//3, loop=False):
        with frame.translate(start=[-200, 0], stop=[200, 0]):
            with frame.rotate(start=0, stop=360):
                rectangle(settings.RECTANGLE_HEIGHT, settings.RECTANGLE_WIDTH, settings.RECTANGLE_COLOR)

    for frame in animate(settings.TOTAL_FRAMES//3, loop=False):
        with frame.translate(start=[200, 0], stop=[-200, 0]):
            with frame.scale(start=1, stop=2):
                rectangle(settings.RECTANGLE_HEIGHT, settings.RECTANGLE_WIDTH, settings.RECTANGLE_COLOR)

