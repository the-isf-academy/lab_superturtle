from superturtle.animation import animate
from turtle import *
from superturtle.movement import update_position, fly
from shapes import triangle, rectangle

for frame in animate(60, loop=True):
    with frame.translate(start=[-200, 0], stop=[200, 0]):
        with frame.rotate(start=0, stop=360):
                rectangle(20, 20, 'coral')