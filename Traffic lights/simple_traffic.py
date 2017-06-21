# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Handling Keypresses")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()

# def h1():
#     tess.forward(30)

# def h2():
#     tess.left(45)

# def h3():
#     tess.right(45)

# def h4():
#     wn.bye()

# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")

# wn.listen()
# wn.mainloop()


# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Handing mouse clicks!")
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()
# tess.color("purple")
# alex = turtle.Turtle()
# alex.color("blue")
# alex.forward(100)

# def handler_for_tess(x, y):
#     wn.title("Tess clicked at {0}, {1}".format(x, y))
#     tess.left(42)
#     tess.forward(30)


# def handler_for_alex(x, y):
#     wn.title("Alex clicked at {0}, {1}".format(x, y))
#     alex.right(84)
#     alex.forward(50)


# tess.onclick(handler_for_tess)
# alex.onclick(handler_for_alex)

# wn.mainloop()


# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Using a timer")
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()
# tess.color("purple")
# tess.pensize(3)

# def h1():
#     tess.forward(100)
#     tess.left(56)
#     wn.ontimer(h1, 60)

# h1()
# wn.mainloop()


import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()

tess.forward(40)
tess.left(90)
tess.forward(50)

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

wn.onkey(advance_state_machine, "space")

wn.listen()
wn.mainloop()


































