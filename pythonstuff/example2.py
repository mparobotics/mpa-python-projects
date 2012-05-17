from visual import *
import math

examplesphere = sphere(pos=(0,0,0), radius=0.5)

scene.ambient = 0.7
scene.background = (0,0.5,0.5) # blue-green background
red = 0.3333
green = 0.66666
blue = 0

while 1:
    blue = (blue + 0.01) % 1.0
    red = (red + 0.01) % 1.0
    green = (green + 0.01) % 1.0
    examplesphere.color = (red,green,blue)
    rate(10)
