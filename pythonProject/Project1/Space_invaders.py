# Space invaders
# setup the screen

import turtle
import os

#set up the screen
window =turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

#draw a Border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()   # levanta el pincel
border_pen.setposition(-300,-300)
border_pen.pendown()  # Pon el pincel en el suelo para que pinte
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600) # pinta 600 px hacia adelante
    border_pen.left(90)     #gira 90 grados a la izquierda
border_pen.hideturtle()     # Desaparece el pincel

# Create a player turtle
player =turtle.Turtle() # Create a turtle object
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


playerspeed=15

#Move the player left and right
def move_left():
    x =player.xcor()
    x -= playerspeed
    if x < -280:
       x = -280
    player.setx(x)

def move_right():
    x =player.xcor()
    x +=playerspeed
    if  x > 280:
       x = 280
    player.setx(x)



#Create a Keyboard   binding
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")














# Es una mejora que aparece en los comentarios
window.mainloop()


