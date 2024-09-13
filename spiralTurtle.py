import random
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tu = (r,g,b)
    return tu

directions = [0, 90, 180, 270]
tim.pensize(1)

def draw_spiral(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


draw_spiral(2)
screen =  t.Screen()
screen.exitonclick()