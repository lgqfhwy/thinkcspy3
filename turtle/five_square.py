import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tess!")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)
alex.shape("turtle")

for j in range(4):
    alex.pendown()
    for i in range(4):
        alex.forward(50)
        alex.left(90)
    if j != 3:
        alex.up()
        alex.forward(100)



wn.mainloop()
