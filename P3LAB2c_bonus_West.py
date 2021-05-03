import turtle             # Allows us to use turtles
win = turtle.Screen()      # The area for for turtle move
flakes = turtle.Turtle()    # Create a turtle, assign to snow
win.bgcolor("#011ad5")

#Display for Turtle

flakes.pen(pencolor="white", fillcolor="cyan", pensize=5, speed=3)

# Taking input for the number of side of the snowflake
N = int(input('Enter a number under 20 for the sides of the snowflake:'))

#Snowflakes Begins To Form

for i in range(0,N):
        flakes.forward(100)
        flakes.forward(-40)
        flakes.left(40)
        flakes.forward(30)
        flakes.forward(-30)
        flakes.right(80)
        flakes.forward(30)
        flakes.forward(-30)
        flakes.left(40)
        flakes.forward(-60)

        flakes.right(60)
        flakes.penup()
        flakes.left(45)
        flakes.pendown()
        
        flakes.forward(-100)
        flakes.forward(40)
        flakes.left(-40)
        flakes.forward(-30)
        flakes.forward(30)
        flakes.right(-80)
        flakes.forward(-30)
        flakes.forward(30)
        flakes.left(-40)
        flakes.forward(60)

        flakes.right(-60)


# end commands

win.exitonclick()
        

