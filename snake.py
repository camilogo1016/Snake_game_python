import turtle
import time #it will delay every move of the game
import random

delay = 0.1

#Markers
score = 0
high_score = 0

#Window setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black") #background
window.setup(width=600, height=600) #size of window
window.tracer(0)

#Snake head
head = turtle.Turtle() #we create the snake
head.speed(0)   #initialize it
head.shape("square")
head.color("white")
head.penup() #without trace when it advances
head.goto(0,0) #starts at the center
head.direction = "stop" #it starts still

#Food
food = turtle.Turtle() #we create the snake
food.speed(0)   #initialize it
food.shape("circle")
food.color("red")
food.penup() #without trace when it advances
food.goto(0,100) #starts at the center

#Texto
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0    High Score:0", align="center", font=("Courier", 15, "normal"))

#Snake Body
body = []

#Functions
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

def mov():
    if head.direction == "up" :
        y = head.ycor() #it gets the 'y' position
        head.sety(y + 20) #It moves 20 pixels every move
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left" :
        x = head.xcor() #it gets the 'x' position
        head.setx(x - 20) #It moves 20 pixels every move
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 20)

def body_add():
    new_body = turtle.Turtle() #we create the snake
    new_body.speed(0)   #initialize it
    new_body.shape("square")
    new_body.color("grey")
    new_body.penup() #without trace when it advances
    
    body.append(new_body) #We append the new body
    
#Keyboard
window.listen()
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")

while True:
    window.update()

    #Collisions 
    if head.xcor() > 280 or head.xcor()<-280 or head.ycor() > 280 or head.ycor()<-280:
        time.sleep(1)
        score = 0   #Reset the marker
        text.clear()
        text.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 15, "normal"))
        
        head.goto(0,0)
        head.direction= "stop"
        
        [i.hideturtle() for i in body]
        body.clear() #Remove the body

        x = random.randint(-280,280)        
        y = random.randint(-280,280)        
        food.goto(x,y)

    #Food    
    if head.distance(food)<20: #the snake and the food at the same position
        x = random.randint(-280,280)        
        y = random.randint(-280,280)        
        food.goto(x,y)
        
        body_add()

        #score
        score += 10
        if score > high_score:
            high_score = score
        text.clear()
        text.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 15, "normal"))

    #Move the body
                
                ##for this the 'n' segment follows the 'n-1' until the first one
    len_body=len(body)
    for i in range(len_body - 1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    
    
    #Moves the first part of the body
    if len_body>0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    mov()

    #Body Collision
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)
            score = 0   #Reset the marker
            text.clear()
            text.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 15, "normal"))
            
            head.goto(0,0)
            head.direction= "stop"
            
            [i.hideturtle() for i in body]
            body.clear() #Remove the body
            x = random.randint(-280,280)        
            y = random.randint(-280,280)        
            food.goto(x,y)
        
    time.sleep(delay)
#window.exitonclick()