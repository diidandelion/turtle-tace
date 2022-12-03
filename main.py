import turtle
from turtle import Turtle, Screen
import random
from typing import List

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles= []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=-100 + i * 40)
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You win! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You lose! The {turtle.pencolor()} turtle is the winner!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()