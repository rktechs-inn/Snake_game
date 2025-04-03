from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.current_score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.current_score}", False, "center", ("Courier", 20, "normal"))
        self.high_score = 0
        # self.write(f"High Score: {self.current_score}", False, "right", ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, "center", ("Courier", 20, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"High Score: {self.current_score}", False, "right", ("Courier", 20, "normal"))

    # TODO: Create high score
    # def reset_score(self):
    #     if self.current_score > self.high_score:
    #         self.high_score = self.current_score
    #     self.current_score = 0
    #     self.increase_score()

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score: {self.current_score}", False, "center",
                   ("Courier", 20, "normal"))       #add  High Score: {self.high_score} in print
