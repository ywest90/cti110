import turtle             # Allows us to use turtles
win = turtle.Screen()      # The area for for turtle move
win.bgcolor("yellow")
joe = turtle.Turtle()    # Create a turtle, assign to joe
tim = turtle.Turtle()    # Create a turtle, assign to tim


#Display For Turtles

joe.shape("circle")           # Changes the shape to a circle
tim.shape("square")           # Changes the shape to a circle

                            # Changes the pen color, fill color, pen size, and speed
joe.pen(pencolor="purple", fillcolor="purple", pensize=5, speed=5)    
tim.pen(pencolor="red", fillcolor="red", pensize=10, speed=2)    


#Begin Drawing Square

for i in range(4):
    joe.forward(150)
    joe.right(90)
    
#Moving Turtle Position

tim.penup()
tim.backward(150)      # Command joe to pick up off the screen                        
tim.pendown()             


#Begin Drawing Triangle

for i in range(4):
    tim.forward(100)
    tim.right(120) 


# end commands
win.mainloop()             # Wait for user to close window
