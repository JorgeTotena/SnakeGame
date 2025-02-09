from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle): #INHERIT from the turtle class
    def __init__(self):
        super().__init__() #take all the atributes from the supra class
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.counter = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.scoreboard = self.write(arg=f"Score = {self.counter} High score: {self.high_score}", move=False,
                                     align=ALIGN, font=FONT)

    def increase(self):
        #self.clear() #we clear the screen to delete the previous text so the text won't overlap
        self.counter+=1
        self.update_scoreboard()


    """def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write(arg="Game over", move=False, align=ALIGN, font=FONT)"""
    def reset(self):
        if self.counter >= self.high_score:
            self.high_score = self.counter
            self.counter = 0
            self.update_scoreboard()


