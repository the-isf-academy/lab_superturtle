from superturtle.animation import animate
from turtle import *
from  superturtle.easing import easeOutSine, easeInSine, easeOutExpo, easeInExpo
from superturtle.movement import update_position, fly
from shapes import triangle


for frame in animate(frames=100, loop=True):
    with frame.translate(start=[-200, 0], stop=[200, 0],easing=easeInExpo):
        triangle(100,'pink')


# what does translate mean?
# changes the numbers to make the triangle move diagonly from the top left to the bottom right
         # what did you change? 

