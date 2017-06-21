import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling Keypresses")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

size = 3

tess.pensize(size)

def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

def h5():
    tess.fillcolor("Red")

def h6():
    tess.fillcolor("Green")

def h7():
    tess.fillcolor("Blue")

def pen_size_increase():
    global size
    if size > 1 and size < 20:
        size += 1
        print("size = ", sizea)
    tess.pensize(size)

def pen_size_decrease():
    global size
    if size > 1 and size < 20:
        size -= 1
    tess.pensize(size)

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(pen_size_increase, "+")
wn.onkey(pen_size_decrease, "-")

wn.listen()
wn.mainloop()