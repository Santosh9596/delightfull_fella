
import turtle
import time
import random

#screen for turtle....
#sc = turtle.Screen()

#turtle name....
btn = turtle.Turtle()
btn_1 = turtle.Turtle()
btn_2 = turtle.Turtle()
btn_3 = turtle.Turtle()

#shape change of btn turtle
btn.shape('square')
btn_1.shape('square')
btn_2.shape('square')
btn_3.shape('square')

#turtle shape change....

btn.turtlesize(stretch_wid = 1)
btn_1.turtlesize(stretch_wid = 3)
btn_2.turtlesize(stretch_wid = 5)
btn_3.turtlesize(stretch_wid = 8)

btn_3.penup()

i = 0
while i <= 360:
#physics for squares...
    
    btn_3.forward(300)
    btn_3.backward(300)
    btn_3.backward(300)
    btn_3.forward(300)

    btn_2.color('white')
    btn_2.circle(0,-45)
    btn_1.color('black')
    btn_1.circle(0,45)
    btn.color('white')
    btn.circle(0,-45)
    time.sleep(1)
    
    i+=1
