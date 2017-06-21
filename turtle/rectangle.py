import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

size = 0
tangle = 95
for i in range(10):
    for j in range(4):

        tess.right(tangle)
        size = size + 10
        tess.forward(size)

wn.mainloop()