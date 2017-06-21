def koch(t, order, size):
    """
        Make turtle t draw a Koch fractical of 'order' and 'size'.
        Leave the turtle facing the same direction.
    """
    if order == 0:      # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)
        t.right(120)
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)

def koch1(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for i in range(3):
        koch1(t, order, size)
        t.right(120)

def cesaro_torn_line(t, order, size, angle):
    m = angle - 180
    n = -m // 2
    if order == 0:
        t.forward(size)
    else:
        for i in [n, m, n, 0]:
            cesaro_torn_line(t, order - 1, size / 2, angle)
            t.right(i)

def cesaro_torn_line_not_larger(t, order, size, angle):
    print(size)
    import math
    m = angle - 180
    n = -m // 2
    x = math.cos(math.radians(n))
    print("n = ", n)
    print("x = ", x)
    real_size = size / (2 + 2 * x)
    if order == 0:
        t.forward(size)
    else:
        for i in [n, m, n, 0]:
            cesaro_torn_line_not_larger(t, order - 1, real_size, angle)
            t.right(i)



def cesaro_squares(t, order, size, angle):
    for i in range(4):
        cesaro_torn_line(t, order, size, angle)
        t.right(90)

def cesaro_squares_not_larger(t, order, size, angle):
    for i in range(4):
        cesaro_torn_line_not_larger(t, order, size, angle)
        t.right(90)


def sierpinski_triangle(t, order, size):
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski_triangle(t, order - 1, size / 2)
        t.forward(size / 2)
        sierpinski_triangle(t, order - 1, size / 2)
        t.left(120)
        t.forward(size / 2)
        t.right(120)
        sierpinski_triangle(t, order - 1, size / 2)
        t.right(120)
        t.forward(size / 2)
        t.left(120)


def sierpinski_triangle_color(t, order, size):

    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski_triangle_color(t, order - 1, size / 2)
        t.forward(size / 2)
        sierpinski_triangle_color(t, order - 1, size / 2)
        t.left(120)
        t.forward(size / 2)
        t.right(120)
        sierpinski_triangle_color(t, order - 1, size / 2)
        t.right(120)
        t.forward(size / 2)
        t.left(120)


def sierpinski_triangle_color_change_depth_0(t, order, size, colorChangeDepth = -1):
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        colorChangeDepth += 1
        if colorChangeDepth == 0:
            t.color("red")
        sierpinski_triangle_color_change_depth_0(t, order - 1, size / 2, colorChangeDepth)
        t.penup()
        t.forward(size / 2)
        t.pendown()
        if colorChangeDepth == 0:
            t.color("blue")
        sierpinski_triangle_color_change_depth_0(t, order - 1, size / 2, colorChangeDepth)
        t.penup()
        t.left(120)
        t.forward(size / 2)
        t.right(120)
        t.pendown()
        if colorChangeDepth == 0:
            t.color("magenta")
        sierpinski_triangle_color_change_depth_0(t, order - 1, size / 2, colorChangeDepth)
        t.penup()
        t.right(120)
        t.forward(size / 2)
        t.left(120)
        t.pendown()


def sierpinski_triangle_color_change_depth_2(t, order, size, colorChangeDepth = -1):
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        colorChangeDepth += 1
        if colorChangeDepth == 2:
            t.color("red")
        sierpinski_triangle_color_change_depth_2(t, order - 1, size / 2, colorChangeDepth)
        t.penup()
        t.forward(size / 2)
        t.pendown()
        if colorChangeDepth == 2:
            t.color("blue")
        sierpinski_triangle_color_change_depth_2(t, order - 1, size / 2, colorChangeDepth)
        t.penup()
        t.left(120)
        t.forward(size / 2)
        t.right(120)
        t.pendown()
        if colorChangeDepth == 2:
            t.color("magenta")
        sierpinski_triangle_color_change_depth_2(t, order - 1, size / 2, colorChangeDepth)
        t.penup()
        t.right(120)
        t.forward(size / 2)
        t.left(120)
        t.pendown()



def sierpinski_triangle_color_change_depth(t, order, size, changedepth, colorChangeDepth = -1):
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        colorChangeDepth += 1
        if colorChangeDepth == changedepth:
            t.color("red")
        sierpinski_triangle_color_change_depth(t, order - 1, size / 2, changedepth, colorChangeDepth)
        t.penup()
        t.forward(size / 2)
        t.pendown()
        if colorChangeDepth == changedepth:
            t.color("blue")
        sierpinski_triangle_color_change_depth(t, order - 1, size / 2, changedepth, colorChangeDepth)
        t.penup()
        t.left(120)
        t.forward(size / 2)
        t.right(120)
        t.pendown()
        if colorChangeDepth == changedepth:
            t.color("magenta")
        sierpinski_triangle_color_change_depth(t, order - 1, size / 2, changedepth, colorChangeDepth)
        t.penup()
        t.right(120)
        t.forward(size / 2)
        t.left(120)
        t.pendown()



# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()

# tess.pensize(3)
# tess.pen(speed = 0)
# wn.mainloop()





def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot


def r_max(nxs):
    """
        Find the maximum in a recursive structure of lists
        within other lists.
        Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True 
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

#print(r_max([2, 9, [1, 13], 8, 6]))
def recursion_depth(number):
    if number > 10:
        return
    print("{0}, ".format(number), end = "")
    recursion_depth(number + 1)

#recursion_depth(0)
def fib(n):
    if n <= 1:
        return n
    t = fib(n - 1) + fib(n - 2)
    return t

import os

def get_dirlist(path):
    """
        Return a sorted list of all entries in path.
        This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":    # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")



def recursive_min(nxs):
    """
        Find the minimum in a recursive structure of lists
        within other lists.
        Precondition: No lists or sublists are empty.
    """
    minimum = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < minimum:
            minimum = val
            first_time = False
    return minimum

# print(recursive_min([2, 9, [1, 13], 8, 6]))
# print(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]))
# print(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]))
# print(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]))

def count(target, nxs):
    """ Return the number of occurrences of target in a nested list."""
    countnum = 0
    for e in nxs:
        if type(e) == type([]):
            countnum += count(target, e)
        else:
            if e == target:
                countnum += 1
    return countnum

# print(count(2, []))
# print(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]))
# print(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]))
# print(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]))
# print(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]))
# print(count("a", [["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]))

def flatten(nxs):
    """ Return a simple list containing all the values in a nested list."""
    result = []
    for e in nxs:
        if type(e) == type([]):
            result.extend(flatten(e))
        else:
            result.append(e)
    return result

# print(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]))
# print(flatten([9, [7, 1, 13, 2], 8, [7, 6]]))

def fib_not_recursion(n):
    a1 = 0
    a2 = 1
    i = 2
    if n <= 1:
        return n
    while i <= n:
        an = a1 + a2
        a1 = a2
        a2 = an
        i += 1
    return an

#print(fib(200))
#print(fib_not_recursion(200))


import os
def get_dirlist(path):
    """
        Return a sorted list of all entries in path.
        This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def files_in_directory_or_subdirectories(path):
    """ Walk a directory, return a list of all the full paths of files in 
        the directory or the subdirectories.
    """

    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if not os.path.isdir(fullname):
            print(fullname)
        else:
            files_in_directory_or_subdirectories(fullname)


# files_in_directory_or_subdirectories("/Users/lgq/Desktop")


#litter.py
#os.chdir(path)  change the current working directory to path
#os.getcwd()  return a string representing the current working directory
#os.remove(path)  remove(delete) the file path.If path is a directory, 
#OSError is raised.Use rmdir() to remove directories
#os.rmdir(path)  remove (delete) the directory path.Only works when the directory 
# is empty, otherwise, OSError is raised.
#os.mknod("test.txt") create an empty file
def create_empty_file_in_subdirectory(path = ""):
    if path == "":
        path = os.getcwd()
    dirlist = get_dirlist(path)
    txt = "trash.txt"
    fullname = os.path.join(path, txt)
    open(fullname, 'a').close()
    for f in dirlist:
        fullname = os.path.join(path, f)
        print(fullname)
        if os.path.isdir(fullname):
            create_empty_file_in_subdirectory(fullname)

path = "/Users/lgq/Desktop/123"   
#create_empty_file_in_subdirectory(path)
#cleanup.py
def clean_up_file_in_subdirectory(txt, path = ""):
    if path == "":
        path = os.getcwd()
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if f == txt:
            os.remove(fullname)
        if os.path.isdir(fullname):
            clean_up_file_in_subdirectory(txt, fullname)
                

txt = "trash.txt"
path = "/Users/lgq/Desktop/123"
clean_up_file_in_subdirectory(txt, path)































































