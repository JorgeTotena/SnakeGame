import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Si desactivas las actualizaciones automáticas con screen.tracer(0), puedes usar screen.update() para decidir cuándo se reflejan los cambios en la pantalla
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# x_coordinates = [(0, 0),(-20, 0),(-40, 0)]
#segments = [] # store the variables generated in the for loop here
game_status = True
#tim = Turtle("square")
#tim.color("white")

while game_status:
    screen.update() #En Python, screen.update() se utiliza principalmente en el módulo turtle para controlar cuándo se actualiza la visualización gráfica. Es especialmente útil cuando se trabaja con animaciones o dibujos complejos para optimizar el rendimiento y evitar parpadeos.
    time.sleep(0.15)# 1 sec delay when the whole snake moves, this function is used to control de delay of how the screen moves
    snake.move()
    # DETECT COLISSION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()
    #DETECT COLISSION WITH WALL
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 290 or snake.head.ycor() <= -300:
        #game_status = False
        scoreboard.reset()
        snake.reset()
    #DETECT COLISSION WITH TAIL

    for segment in snake.segments[1:]: #accesing everything in the list from start to end, avoiding position 0
        if snake.head.distance(segment) < 10: #distance between the head and the segments
            #game_status = False
            scoreboard.reset()
            snake.reset()







"""

for coordinate in x_coordinates:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(coordinate)
    segments.append(new_segment)

while game_status:
    screen.update() #En Python, screen.update() se utiliza principalmente en el módulo turtle para controlar cuándo se actualiza la visualización gráfica. Es especialmente útil cuando se trabaja con animaciones o dibujos complejos para optimizar el rendimiento y evitar parpadeos.
    time.sleep(0.1)# 1 sec delay when the whole snake moves, this function is used to control de delay of how the screen moves
    #for segment in segments: just moves one of the segments
        #segment.forward(20)
    #for seg_num in range(start=2, stop=0, step=-1):
    #THESE ARE THE CONCEPTS TO MOVE FREELY THE SNAKE, CAN BE USEFUL IN OTHER CODES
    for seg_num in range(len(segments) -1,0,-1): #the range is being iterated backwards
        new_x = segments[seg_num -1].xcor() #chaning the second to last coordinate
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20) """









screen.exitonclick()
