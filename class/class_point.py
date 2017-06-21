class Point:
    """ Point class represents and manipulates x, y coords. """

    def __init__(self, x, y):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        """ Return a new point, one which is the reflection of the point about the x-axis."""
        mx = self.x
        my = -self.y
        return Point(mx, my)

    def slope_from_origin(self):
         """ Return the slope of the line joining the origin to the point"""
         return self.y / self.x

    def get_line_to(self, target):
        """ Compute the equation of the straight line joining the two points.
            Return the two coefficients as a tuple of two values."""
        if self.x == target.x:
            return 
        a = (self.y - target.y) / (self.x - target.x)
        b = self.y - a * self.x
        return (a, b)

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my) 


def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


p = Point(3, 4)
q = Point(3, 5)
r = distance(p, q)
# print(r)
# print(Point(3, 5).reflect_x())
t = Point(4, 10)
# print(t.slope_from_origin())
# print(Point(4, 11).get_line_to(Point(4, 15)))


def find_midpoint_of_circle(p1, p2, p3, p4):
    """ Find the midpoint of the circle."""
    x = ((p3.y - p2.y) + (p3.x ** 2 - p1.x ** 2) / (p3.y - p1.y) - 
        (p2.x ** 2 - p1.x ** 2) / (p2.y - p1.y)) * ((p3.x - p1.x) / 
        (p3.y - p1.y) - (p2.x - p1.x) / (p2.y - p1.y)) / 2
    y = ((p2.x - p1.x) / (p1.y - p2.y) * x) + (((p1.y + p2.y) + 
        (p2.x ** 2 - p1.x ** 2) / (p2.y - p1.y)) / 2)
    return (x, y)



class Rectangle(object):
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})" \
                .format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """ Return the area of any instance. """
        return self.width * self.height

    def perimeter(self):
        """ Find the perimeter of any rectangle instance. """
        return self.width * 2 + self.height * 2

    def flip(self):
        """ Swap the width and the height of any rectangle instance. """
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, target):
        dx = target.x - self.corner.x
        dy = target.y - self.corner.y
        if dx >= 0 and dy >= 0 and dx < self.width and dy < self.height:
            return True
        return False

    def collision_detection(self, target):
        dx = target.corner.x - self.corner.x
        dy = target.corner.y - self.corner.y
        if dx >= 0 and dy >= 0:
            if dx < self.width and dy < self.height:
                return True
        elif dx >= 0 and dy < 0:
            if dx < self.width and -dy < target.height:
                return True
        elif dx < 0 and dy >= 0:
            if -dx < target.width and dy < self.height:
                return True
        else:
            if -dx < target.width and -dy < target.height:
                return True
        return False


# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10)
# print("box: ", box)
# print("bomb: ", bomb)
# box.width += 50
# box.height += 100
# print("box: ", box)
# r = Rectangle(Point(10, 5), 100, 50)
# print(r)
# r.grow(25, -10)
# print(r)
# r.move(-10, 10)
# print(r)

# p = Point(4, 2)
# s = Point(4, 2)
# print("== on Points returns", p == s)
# s = p
# print("== on Points returns", p == s)

# a = [2, 3]
# b = [2, 3]
# print("== on lists returns", a == b)

# import copy
# p1 = Point(3, 4)
# p2 = copy.copy(p1)

# b1 = Rectangle(Point(0, 0), 100, 200)
# b2 = copy.deepcopy(b1)
# b1.grow(25, -10)
# print(b1, b2)
# b1.move(-10, 10)
# print(b1, b2)

r = Rectangle(Point(0, 0), 10, 5)
# print(r.area())
# print(r.perimeter())
# print(r)
# r.flip()
# print(r)
# print(r.contains(Point(0, 0)))
# print(r.contains(Point(3, 3)))
# print(not r.contains(Point(3, 7)))
# print(not r.contains(Point(3, 5)))
# print(r.contains(Point(3, 4.99999)))
# print(not r.contains(Point(-3, -3)))
























