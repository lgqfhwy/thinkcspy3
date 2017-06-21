def draw_bar(t, height, xcolor):
    """ 
        Get turtle t to draw one bar, of height.
    """
    t.color("blue", xcolor)
    t.color()
    t.begin_fill()
    t.left(90)
    t.forward(height)
    #t.stamp()
    if height < 0:
        t.penup()
        t.forward(-12)
        t.write("        " + str(height), False, align = "left")
        t.forward(12)
        t.pendown()
    else:
        t.write("        " + str(height), False, align = "left")
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.penup()
    t.end_fill()
    t.forward(10)
    t.pendown()


import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
#tess.color("blue", "red")
tess.pensize(3)


xs = [-48, 117, 200, 240, 160, 260, 220]
#xs = [-48]
for v in xs:
    if v >= 200:
        xcolor = "red"
    elif v >= 100 and v < 200:
        xcolor = "yellow"
    else:
        xcolor = "green"
    draw_bar(tess, v, xcolor)

wn.mainloop()
















