from turtle import Turtle

INITIAL_POSITIONS = ((0,0),(-20,0),(-40,0))

class Snake():
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(position[0],position[1])
            self.parts.append(snake)

    def move(self):
        for num in range(len(self.parts)-1,-1,-1):
            if num == 0:
                self.head.forward(20)
            else:
                self.parts[num].goto(self.parts[num-1].xcor(),self.parts[num-1].ycor())

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def grow(self):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.setx(self.parts[-1].xcor())
        snake.sety(self.parts[-1].ycor())
        self.parts.append(snake)