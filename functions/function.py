def area(radius):
    b = 3.14159 * radius ** 2
    return b


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx * dx + dy * dy
    result = dsquared ** 0.5
    return result


def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


def is_divisible(x, y):
    """ Test if x is exactly divisible by y """
    if x % y == 0:
        return True
    else:
        return False


def is_divisible2(x, y):
    return x % y == 0
def absolute_value(n):
    if n < 0:
        return -n;
    return n;


import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FALLED.".format(linenum))
    print(msg)


def turn_clockwise(points):
    if points == "N":
        x = "E"
    elif points == "E":
        x = "S"
    elif points == "S":
        x = "W"
    elif points == "W":
        x = "N"
    else:
        x = None
    return x


def test_suite():
    """
        Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

test_suite()





















