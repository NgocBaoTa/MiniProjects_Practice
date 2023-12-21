# There are some turles on the race track with the random speed. 
# You can bet on one of them. 
# The turtle that reaches the finish line first wins. 
# If your turtle wins, you get double your bet back. 
# If you bet on the wrong turtle, you lose your bet. 


from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turle will win the race? Enter a color: ")

colors=["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70 + turle_index * 30)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()