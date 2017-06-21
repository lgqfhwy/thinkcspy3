import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

size = 0
for i in range(5):
    tess.pendown()
    size = size + 20
    for j in range(4):
        tess.forward(size)
        tess.left(90)
    tess.penup()
    tess.right(90)
    tess.forward(10)
    tess.right(90)
    tess.forward(10)
    tess.right(180)



wn.mainloop()
