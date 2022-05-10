# Import Libraries
import math
import random
import os
import time
import turtle

# Settings 
speed = 20
delay = 0.1
lspeed = 40
espeed = 15

colors = ['red', 'orange', 'yellow', 'lawn green', 'turquoise', 'violet']

col = 1

state = True

b = True

# Create A Window
wn = turtle.Screen()
wn.bgcolor('sky blue')
wn.title('Snake Game')
wn.setup(620, 620)
wn.tracer(0) # Helps With Animation

# Create The Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.pensize(6)
border_pen.penup()
border_pen.setposition(-310, -310)
border_pen.pendown()
for a in range(4):
    border_pen.forward(620)
    border_pen.left(90)
border_pen.hideturtle()

# Create A Scoreboard
score = 0

scorepen = turtle.Turtle()
scorepen.speed(0)
scorepen.color("black")
scorepen.penup()
scorepen.setposition(-280, 270)
scorestring = "Score: %s" %score
scorepen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
scorepen.hideturtle()

# Record High Score
highscore = 0

scorepen2 = turtle.Turtle()
scorepen2.speed(0)
scorepen2.color("black")
scorepen2.penup()
scorepen2.setposition(-280, 250)
scorestring2 = "High Score: %s" %score
scorepen2.write(scorestring2, False, align = "left", font = ("Arial", 10, "normal"))
scorepen2.hideturtle()

# Create The Snake's Head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('red')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

neck = turtle.Turtle()
neck.speed(0)
neck.shape('square')
neck.shapesize(0.5, 1)
neck.color('red')
neck.penup()
neck.goto(0, -5)
neck.hideturtle()

laser = turtle.Turtle()
laser.speed(0)
laser.shape('square')
laser.shapesize(0.2, 0.7)
laser.penup()
laser.hideturtle()
laser.direction = 'stop'

eye1 = turtle.Turtle()
eye1.speed(0)
eye1.shape('circle')
eye1.shapesize(0.2, 0.2)
eye1.penup()
eye1.goto(-3, 3)

eye2 = turtle.Turtle()
eye2.speed(0)
eye2.shape('circle')
eye2.shapesize(0.2, 0.2)
eye2.penup()
eye2.goto(3, 3)

# Create Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
x = random.randint(-280, 280)
y = random.randint(-280, 280)
food.goto(x, y)

stem = turtle.Turtle()
stem.speed(0)
stem.shape('square')
stem.shapesize(0.5, 0.1)
stem.penup()
stem.goto(x, y + 10)

stem2 = turtle.Turtle()
stem2.speed(0)
stem2.shape('square')
stem2.shapesize(0.1, 0.3)
stem2.penup()
stem2.goto(x, y + 5)

enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape('circle')
enemy.penup()
x = random.randint(-280, 280)
y = random.randint(-280, 280)
enemy.goto(x, y)
enemy.direction = 'stop'

brow1 = turtle.Turtle()
brow1.speed(0)
brow1.shape('square')
brow1.shapesize(0.5, 0.1)
brow1.color('orange')
brow1.setheading(45)
brow1.penup()
brow1.goto(x - 5, y + 6)

brow2 = turtle.Turtle()
brow2.speed(0)
brow2.shape('square')
brow2.shapesize(0.5, 0.1)
brow2.color('orange')
brow2.setheading(135)
brow2.penup()
brow2.goto(x + 5, y + 6)

eye3 = turtle.Turtle()
eye3.speed(0)
eye3.shape('circle')
eye3.shapesize(0.2, 0.2)
eye3.color('red')
eye3.penup()
eye3.goto(x - 4, y)

eye4 = turtle.Turtle()
eye4.speed(0)
eye4.shape('circle')
eye4.shapesize(0.2, 0.2)
eye4.color('red')
eye4.penup()
eye4.goto(x + 4, y)

mouth = turtle.Turtle()
mouth.speed(0)
mouth.shape('square')
mouth.shapesize(0.05, 0.5)
mouth.color('white')
mouth.penup()
mouth.goto(x, y - 5)

# Make A List To Store The Snake Segments
snake = []
segments = 0


# Move The Snake
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + speed)
    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - speed)
    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + speed)
    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - speed)


# Create Functions To Use In Keyboard Binding
def move_up():
    if head.direction == 'down':
        head.direction = 'down'
    else:
        head.direction = 'up'


def move_down():
    if head.direction == 'up':
        head.direction = 'up'
    else:
        head.direction = 'down'


def move_right():
    if head.direction == 'left':
        head.direction = 'left'
    else:
        head.direction = 'right'


def move_left():
    if head.direction == 'right':
        head.direction = 'right'
    else:
        head.direction = 'left'


def I_AM_SPEED():
    global speed
    speed = 40


def slow_down():
    global speed
    speed = 20


def hack():
    x = food.xcor()
    y = food.ycor()
    head.goto(x, y)


def shoot():
    global state
    if state:
        x = head.xcor()
        y = head.ycor()
        laser.goto(x, y)
        laser.showturtle()
        if head.direction == 'up':
            laser.setheading(90)
            laser.direction = 'up'
        elif head.direction == 'down':
            laser.setheading(90)
            laser.direction = 'down'
        elif head.direction == 'right':
            laser.setheading(0)
            laser.direction = 'right'
        elif head.direction == 'left':
            laser.setheading(0)
            laser.direction = 'left'
        state = False


def move_enemy():
    if ran == 1:
        enemy.direction = 'right'
    elif ran == 2:
        enemy.direction = 'left'
    elif ran == 3:
        enemy.direction = 'up'
    elif ran == 4:
        enemy.direction = 'down'


# Funtion To Check Distance Between Objects
def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance


# Keyboard Bindings
wn.listen()
wn.onkeypress(move_up, 'w')
wn.onkeypress(move_down, 's')
wn.onkeypress(move_right, 'd')
wn.onkeypress(move_left, 'a')
wn.onkeypress(move_up, 'Up')
wn.onkeypress(move_down, 'Down')
wn.onkeypress(move_right, 'Right')
wn.onkeypress(move_left, 'Left')
wn.onkeypress(I_AM_SPEED, 'j')
wn.onkeypress(slow_down, 'k')
wn.onkeypress(hack, 'l')
wn.onkeypress(shoot, 'space')


# Main Game Loop
while True:
    wn.update()

    # Move Each Part In Snake In Reverse Order
    for index in range(len(snake) - 1, 0, -1):
        x = snake[index - 1].xcor()
        y = snake[index - 1].ycor()
        snake[index].goto(x, y)
        new_segment.showturtle()

    # Move The First Segment
    if len(snake) > 0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x, y)
        new_segment.showturtle()

    # Let Snake Eat Food And Append A Segment
    if iscollision(head, food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        stem.goto(x, y + 10)
        stem2.goto(x, y + 5)

        new_segment = turtle.Turtle()
        new_segment.hideturtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color(colors[col])
        new_segment.penup()
        snake.append(new_segment)

        col += 1

        if col > len(colors) - 1:
            col = 0

        if len(snake) == 1:
            neck.showturtle()

        snake[-1].shape('circle')

        if len(snake) > 1:
            snake[-2].shape('square')

        score += 10
        scorestring = "Score: %s" % score
        scorepen.clear()
        scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    if score > highscore:
        highscore = score
        scorestring2 = "High Score: %s" % score
        scorepen2.clear()
        scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))

    if iscollision(laser, enemy) < 21:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        enemy.goto(x, y)

        laser.hideturtle()
        state = True

        score += 50
        scorestring = "Score: %s" % score
        scorepen.clear()
        scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    if laser.xcor() > 290 or laser.xcor() < -290 or laser.ycor() > 290 or laser.ycor() < -290:
        laser.hideturtle()
        state = True

    # Check For Border Collisions
    if head.ycor() > 290 or head.ycor() < -290 or head.xcor() > 290 or head.xcor() < -290:
        scorepen.clear()
        scorepen2.clear()
        scorepen.goto(0, 0)
        scorepen.write('Game Over', False, align="center", font=("Arial", 36, "normal"))
        scorepen.goto(-280, 270)
        time.sleep(3)
        scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
        head.direction = 'stop'
        head.goto(0, 0)
        eye1.goto(3, 3)
        eye2.goto(-3, 3)
        neck.hideturtle()
        col = 1
        for c in snake:
            c.goto(2000, 2000)
        snake.clear()
        if score > highscore:
            highscore = score
            scorestring2 = "High Score: %s" % score
            scorepen2.clear()
            scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
        score = 0
        scorestring = "Score: %s" % score
        scorepen.clear()
        scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    if iscollision(enemy, head) < 20:
        scorepen.clear()
        scorepen2.clear()
        scorepen.goto(0, 0)
        scorepen.write('Game Over', False, align="center", font=("Arial", 36, "normal"))
        scorepen.goto(-280, 270)
        time.sleep(3)
        scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
        head.direction = 'stop'
        head.goto(0, 0)
        eye1.goto(3, 3)
        eye2.goto(-3, 3)
        neck.hideturtle()
        col = 1
        for c in snake:
            c.goto(2000, 2000)
        snake.clear()
        if score > highscore:
            highscore = score
            scorestring2 = "High Score: %s" % score
            scorepen2.clear()
            scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
        score = 0
        scorestring = "Score: %s" % score
        scorepen.clear()
        scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    for f in snake:
        if iscollision(enemy, f) < 20:
            scorepen.clear()
            scorepen2.clear()
            scorepen.goto(0, 0)
            scorepen.write('Game Over', False, align="center", font=("Arial", 36, "normal"))
            scorepen.goto(-280, 270)
            time.sleep(3)
            scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
            head.direction = 'stop'
            head.goto(0, 0)
            eye1.goto(3, 3)
            eye2.goto(-3, 3)
            neck.hideturtle()
            col = 1
            for c in snake:
                c.goto(2000, 2000)
            snake.clear()
            if score > highscore:
                highscore = score
                scorestring2 = "High Score: %s" % score
                scorepen2.clear()
                scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
            score = 0
            scorestring = "Score: %s" % score
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    if b:
        ran = random.randint(1, 4)
        b = False
    if enemy.xcor() > -280 and enemy.xcor() < 280 and enemy.ycor() > -280 and enemy.ycor() < 280:
        ran2 = random.randint(1, 10)
        if ran2 == 5:
            ran = random.randint(1, 4)

    if enemy.ycor() > 285:
        ran3 = random.randint(1, 3)
        if ran3 == 1:
            ran = 1
        elif ran3 == 2:
            ran = 2
        elif ran3 == 3:
            ran = 4
    
    if enemy.ycor() < -285:
        ran3 = random.randint(1, 3)
        if ran3 == 1:
            ran = 1
        elif ran3 == 2:
            ran = 2
        elif ran3 == 3:
            ran = 3

    if enemy.xcor() > 285:
        ran3 = random.randint(1, 3)
        if ran3 == 1:
            ran = 3
        elif ran3 == 2:
            ran = 2
        elif ran3 == 3:
            ran = 4

    if enemy.xcor() < -285:
        ran3 = random.randint(1, 3)
        if ran3 == 1:
            ran = 1
        elif ran3 == 2:
            ran = 3
        elif ran3 == 3:
            ran = 4

    # Move Snake
    move()

    move_enemy()

    if head.direction == 'up':
        x = head.xcor()
        y = head.ycor()
        eye1.goto(x - 3, y + 3)
        eye2.goto(x + 3, y + 3)
        neck.setheading(0)
        neck.goto(x, y - 5)

    if head.direction == 'down':
        x = head.xcor()
        y = head.ycor()
        eye1.goto(x - 3, y - 3)
        eye2.goto(x + 3, y - 3)
        neck.setheading(0)
        neck.goto(x, y + 5)

    if head.direction == 'right':
        x = head.xcor()
        y = head.ycor()
        eye1.goto(x + 3, y - 3)
        eye2.goto(x + 3, y + 3)
        neck.setheading(90)
        neck.goto(x - 5, y)

    if head.direction == 'left':
        x = head.xcor()
        y = head.ycor()
        eye1.goto(x - 3, y - 3)
        eye2.goto(x - 3, y + 3)
        neck.setheading(90)
        neck.goto(x + 5, y)

    if laser.direction == 'up':
        y = laser.ycor()
        y += lspeed
        laser.sety(y)
    
    if laser.direction == 'down':
        y = laser.ycor()
        y -= lspeed
        laser.sety(y)

    if laser.direction == 'right':
        x = laser.xcor()
        x += lspeed
        laser.setx(x)

    if laser.direction == 'left':
        x = laser.xcor()
        x -= lspeed
        laser.setx(x)

    if enemy.direction == 'up':
        y = enemy.ycor()
        y += espeed
        enemy.sety(y)
    
    if enemy.direction == 'down':
        y = enemy.ycor()
        y -= espeed
        enemy.sety(y)

    if enemy.direction == 'right':
        x = enemy.xcor()
        x += espeed
        enemy.setx(x)

    if enemy.direction == 'left':
        x = enemy.xcor()
        x -= espeed
        enemy.setx(x)

    x = enemy.xcor()
    y = enemy.ycor()

    brow1.goto(x - 4, y + 6)
    brow2.goto(x + 4, y + 6)
    eye3.goto(x - 4, y)
    eye4.goto(x + 4, y)
    mouth.goto(x, y - 5)

    # Check If Snake Has Hit Itself
    for d in snake:
        if d.distance(head) < 19:
            scorepen.clear()
            scorepen2.clear()
            scorepen.goto(0, 0)
            scorepen.write('Game Over', False, align="center", font=("Arial", 36, "normal"))
            scorepen.goto(-280, 270)
            time.sleep(3)
            scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
            head.direction = 'stop'
            head.goto(0, 0)
            eye1.goto(3, 3)
            eye2.goto(-3, 3)
            neck.hideturtle()
            col = 1
            for c in snake:
                c.goto(2000, 2000)
            snake.clear()
            if score > highscore:
                highscore = score
                scorestring2 = "High Score: %s" % score
                scorepen2.clear()
                scorepen2.write(scorestring2, False, align="left", font=("Arial", 10, "normal"))
            score = 0
            scorestring = "Score: %s" % score
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    # Delay
    time.sleep(delay)
