import turtle
a = turtle.Pen() #initalize a pen object
win = turtle.Screen() # initalize a screen object
win.title("Double heart draw")
win.bgcolor("black")
a.speed(1) # speed set to slow
a.color('red')
a.begin_fill()
a.color("Blue")
a.setheading(140)
a.forward(180)
a.circle(-90,200)
a.setheading(60)
a.circle(-90,200)
a.forward(180)
a.end_fill()
a.setheading(180)
a.up()  # it makes pen up
a.forward(200)
a.down()
a.left(40)
a.forward(10)
a.backward(10)
a.right(400)
a.forward(5)
a.backward(5)
a.setheading(35)

a.forward(500)
a.up()
a.home()
a.down()

a.begin_fill()
a.fillcolor("Red")
a.setheading(220)
a.forward(180)  # moves turtle forward
a.circle(90,200)
a.setheading(300)
a.circle(90, 200)# it creates a semi-circle with 90 radius in anti clock wise
a.forward(180)
a.end_fill()
a.hideturtle() # hides the turtle from the drawing
