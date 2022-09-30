from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.clear()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("red")
        self.generating_food()

    def generating_food(self):
        x_position = random.randint(-160,160)
        y_position = random.randint(-160,160)
        self.goto(x_position,y_position)