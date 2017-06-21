def five_star(t):
    t.right(180)
    for i in range(5):
        t.left(144)
        t.forward(100)
    t.left(180)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.speed(2)


for i in range(5):
    five_star(tess)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()



wn.mainloop()
