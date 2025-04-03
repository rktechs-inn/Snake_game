from turtle import Turtle

#creted these constants to change the value easily as per user
SNAKE_STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE = 20

class SnakeMove:
    def __init__(self):
        self.snake_progress = []
        self.create_snake()
        self.head = self.snake_progress[0]
        self.move()

    #Below 3 functions are interconnected to create and add segments into the snake
    def create_snake(self):
        for starting_body in SNAKE_STARTING_POSITION:
            self.add_segment(starting_body)

    def add_segment(self, starting_body):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(starting_body)
        snake.speed("slow")
        self.snake_progress.append(snake)

    def extend(self):
        self.add_segment(self.snake_progress[-1].position())

    def move(self):
        """In below loop, tail(1 out of 3 segments from snake body) of the snake will come in position of 2nd segment, then
            2nd will come at 1st and then 1st will change"""
        for segment_num in range(len(self.snake_progress) - 1, 0, -1):  # tracing list in reverse to perform above typed doc
            new_x = self.snake_progress[segment_num - 1].xcor()
            new_y = self.snake_progress[segment_num - 1].ycor()  # this will store coords of previous segment
            self.snake_progress[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE)
        # snake_progress[0].left(90)

    # def reset_snake(self):
    #     self.snake_progress.clear()
    #     self.create_snake()
    #     self.head = self.snake_progress[0]
    #     self.move()

    #for snake direction
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)    #Up = 90
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)