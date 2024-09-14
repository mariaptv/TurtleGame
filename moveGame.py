from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_foward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_counter_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_counter():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.home()

screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_counter)
screen.onkey(key="c", fun=clear)

screen.exitonclick()