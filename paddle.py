from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcord, ycord):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(xcord, ycord)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
