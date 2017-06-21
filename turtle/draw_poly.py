def draw_poly(t, n, sz):
    a = (n - 2) * 180.0 / n
    for i in range(n):
        t.forward(sz)
        t.left(180.0 - a)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

draw_poly(tess, 17, 50)

wn.mainloop()