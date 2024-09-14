import random
from datetime import timedelta
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
position = -100
is_race_on = False

for turtle_index in range(0,6):
    tim = Turtle(shape= "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=position)
    position += 40
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You ve won! {winning_color}")
            else:
                print(f"You ve lost! {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

