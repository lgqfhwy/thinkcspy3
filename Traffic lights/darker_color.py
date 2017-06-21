#think python P143 5
#Using darker color
import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Traffic light3")
wn.bgcolor("lightgreen")

tess1 = turtle.Turtle()
tess2 = turtle.Turtle()
tess3 = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights"""
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

def circle_turtle_color(tess, forward1, leftangle, forward2, color):
    tess.penup()

    tess.forward(forward1)
    tess.left(leftangle)
    tess.forward(forward2)

    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor(color)

circle_turtle_color(tess1, 40, 90, 50, "green")
circle_turtle_color(tess2, 40, 90, 120, "orange")
circle_turtle_color(tess3, 40, 90, 190, "red")


state_num = 0
tess2.fillcolor("darkgrey")
tess3.fillcolor("darkgrey")


def advance_state_machine():
    global state_num
    if state_num == 0:
        tess2.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess1.fillcolor("darkgrey")
        state_num = 2
    elif state_num == 2:
        tess2.fillcolor("darkgrey")
        tess3.fillcolor("red")
        state_num = 3
    else:
        tess1.fillcolor("green")
        tess3.fillcolor("darkgrey")
        state_num = 0 

#wn.onkey(advance_state_machine, "space")
t = 0
def control_time():
    global t
    global state_num
    t += 1
    if state_num == 0 and t == 3:
        #green -> Green + Orange
        advance_state_machine()
    if state_num == 1 and t == 4:
        # Green + Orange -> Orange
        advance_state_machine()
    if state_num == 2 and t == 5:
        #Orange -> Red
        advance_state_machine()
    if state_num == 3 and t == 7:
        advance_state_machine()
        t = 0
    wn.ontimer(control_time, 1000)





wn.ontimer(control_time, 1000)

wn.listen()
wn.mainloop(  )
















