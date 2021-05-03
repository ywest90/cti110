import turtle             # Allows us to use turtles
win = turtle.Screen()   # The area for for turtle move
win.bgcolor("blue")
y = turtle.Turtle()    # Create a turtle, assign to y
w = turtle.Turtle()    # Create a turtle, assign to w

#Display For Turtles

y.pen(pencolor="yellow", pensize=3, speed=3)    
w.pen(pencolor="white", pensize=3, speed=5)
y.shape("turtle") # Changes the shape to a turtle
w.shape("circle") # Changes the shape to a circle

#Begin Drawing First Initial

y.backward(100)
y.left(90)
y.forward(100)
y.backward(100)
y.right(90)
y.forward(100)
y.left(90)
y.forward(100)
y.backward(200)
y.left(90)
y.forward(120)
y.left(30)
y.backward(200)
y.pendown()

#Moving Turtle Position

w.penup()           # Command w to pick up pen
w.forward(50)                              
w.pendown()

#Draw Second Initial

w.left(90)
w.forward(100)
w.backward(200)
w.right(90)
w.forward(100)
w.left(90)
w.forward(100)
w.right(90)
w.right(90)
w.forward(100)
w.left(90)
w.forward(100)
w.left(90)
w.forward(200)


# end commands
win.mainloop()             # Wait for user to close window


