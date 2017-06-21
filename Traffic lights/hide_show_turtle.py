#think python P143 3
#Using hideturtle and showturtle to implement the traffic lights program
import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Traffic light 2")
wn.bgcolor("lightgreen")

tess1 = turtle.Turtle()
tess2 = turtle.Turtle()
tess3 = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess1.pensize(3)
    tess1.color("black", "darkgrey")
    tess1.begin_fill()
    tess1.forward(80)
    tess1.left(90)
    tess1.forward(200)
    tess1.circle(40, 180)
    tess1.forward(200)
    tess1.left(90)
    tess1.end_fill()

draw_housing()

tess1.penup()

tess1.forward(40)
tess1.left(90)
tess1.forward(50)

tess1.shape("circle")
tess1.shapesize(3)
tess1.fillcolor("green")


tess2.penup()

tess2.forward(40)
tess2.left(90)
tess2.forward(120)

tess2.shape("circle")
tess2.shapesize(3)
tess2.fillcolor("orange")

tess3.penup()

tess3.forward(40)
tess3.left  (90)
tess3.forward(190)

tess3.shape("circle")
tess3.shapesize(3)
tess3.fillcolor("red")

tess2.hideturtle()
tess3.hideturtle()

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:
        tess1.hideturtle()
        tess2.showturtle()
        state_num = 1
    elif state_num == 1:
        print(456)
        tess2.hideturtle()
        tess3.showturtle()
        print(3)
        state_num = 2
    else:
        tess1.showturtle()
        tess3.hideturtle()
        state_num = 0

wn.onkey(advance_state_machine, "space")

wn.listen()
wn.mainloop()













