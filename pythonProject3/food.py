from turtle import Turtle
import random

class Food(Turtle): #INHERIT from the turtle class
    def __init__(self):
        super().__init__() #take all the atributes from the supra class
        self.shape("circle")
        self.penup()
        self.color("lightblue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #change the dimension of the shape by percentage
        self.speed("fastest")
        self.random_x = random.randint(-280,280)
        self.random_y = random.randint(-280, 255)
        self.goto(self.random_x, self.random_y)
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)






