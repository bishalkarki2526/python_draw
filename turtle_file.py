import turtle   # importing turtle module
a = turtle.Turtle() #initalize a pen object
win = turtle.Screen() # initalize a screen object
win.title("Double heart draw")
win.bgcolor("black")
a.speed(1) # speed set to slow
a.color('red')
a.begin_fill()
a.color("Blue")
a.setheading(140) # set the head of turtle in which direction you want
a.forward(180)
a.circle(-90,200)
a.setheading(60)
a.circle(-90,200)
a.forward(180)
a.end_fill() # it stops filling the color
a.setheading(180)
a.up()  # it makes pen up
a.forward(200)
a.down()
a.left(40)
a.forward(10)
a.backward(10)
a.right(400) # goes right (angle in degrees)
a.forward(5)
a.backward(5) # moves backward(distance in pixel)
a.setheading(35)

a.forward(500) # takes 500 pixel ahead
a.up()
a.home() #  it puts the turtle to home

a.down() # it slows down the turtle

a.begin_fill() # begin to fill color
a.fillcolor("Red") # which color you like
a.setheading(220)
a.forward(180)  # moves turtle forward
a.circle(90,200)
a.setheading(300)
a.circle(90, 200) # it creates a semi-circle with 90 radius in anti clock wise
a.forward(180)
a.end_fill() #end the filling of color
a.hideturtle() # hides the turtle from the drawing
