from turtle import Screen
from snake import Snake
from food import Food
from scorebar import ScoreBar
import time


screen = Screen()
screen.setup(width=400,height=400)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBar()

is_continue = True

screen.listen()
screen.onkey(fun=snake.Down, key='Down')
screen.onkey(fun=snake.Up, key='Up')
screen.onkey(fun=snake.Left, key='Left')
screen.onkey(fun=snake.Right, key='Right')

while is_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.generating_food()
        snake.grow()
        score.increase()

    if snake.head.xcor() > 200 or snake.head.xcor() < -200 or snake.head.ycor() < -200 or snake.head.ycor() > 200:
        score.game_over()
        is_continue = False

    for part in snake.parts[1:]:
        if snake.head.distance(part) < 5:
            score.game_over()
            is_continue = False
            break

screen.exitonclick()