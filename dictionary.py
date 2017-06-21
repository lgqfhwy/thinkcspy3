import os

def exists(filename):
    try:
        f = open(filename)
        f.close()
        return True
    except:
        return False

def exists1(filename):
    """This is the preferred way to check if a file exists."""
    if os.path.isfile(filename):
        return True
    return False

def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")

#recursion_depth(0)

import turtle
import time

def show_poly():
    try:
        win = turtle.Screen()   #Grab/create a resource ,e.g. a window
        tess = turtle.Turtle()

        # This dialog could be cancelled,
        # or the conversion to int might fail, or n might be zero.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):  # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)   # Make program wait a few seconds
    finally:
        win.bye()   #Close the turtle's window

# show_poly()
# show_poly()
# show_poly()

def readposint():
    try:
        num = input("Please input an positive integer:")
        f = int(num)
        if f <= 0:
            raise ValueError
        print("Hello!")

    except TypeError:
        print("Please input an integer.")
    except ValueError:
        print("Please don't input an invalid literal.")
    except:
        print("Error")

#readposint()


# eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
# for k in eng2sp.keys():
#     print("Got key", k, "which maps to value", eng2sp[k])

# ks = list(eng2sp.keys())
# print(ks)

# for k in eng2sp:
#     print("Got key", k)

alreadyknown = {0 : 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n - 1) + fib(n - 2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

#print(fib(40))


def count_letters_form_tables(string):
    letter_counts = {}
    for letter in string:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

#print(count_letters_form_tables("Mississippi"))

def count_letters_occurs_in_alphabet(string):
    letter_counts = {}
    string_lower = string.lower()
    for letter in string_lower:
        if letter == ' ':
            continue
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    letter_items = list(letter_counts.items())
    letter_items.sort()
    for (k, v) in letter_items:
        print(k, v)


# string = "ThiS is String with Upper and lower case Letters"
# count_letters_occurs_in_alphabet(string)



def add_fruit(inventory, fruit, quantity = 0):
     inventory[fruit] = quantity
     return inventory

# new_inventory = {}
# add_fruit(new_inventory, "strawberries", 10)
# print("strawberries" in new_inventory) 
import string
def text_to_words(the_text):
    """ 
        Return a list of words with all punctuation removed,
        and all in lowercase.
    """
    cleaned_text = the_text.replace(string.punctuation, " ")
    # Translate the text now.
    #cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds




def count_letters_occurs_in_alphabet_in_file(text):
    myfile = open(text, "r", encoding = 'utf-8')
    xs = myfile.read()
    myfile.close()
    words = text_to_words(xs)
    letter_counts = {}
    for letter in words:
        letter = letter.lower()
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    letter_items = list(letter_counts.items())
    letter_items.sort()
    endfile = open("alice_words.txt", "w", encoding = "utf-8")
    endfile.write("Word" + " " * 20 + "Count")
    endfile.write("\n")
    endfile.write("=" * 29)
    endfile.write("\n")
    for (k, v) in letter_items:
        endfile.writelines(str(k) + "\t\t\t" + str(v) + "\n")
        # endfile.write("\t\t\t")
        # endfile.write(str(v))
        # endfile.write("\n")
    endfile.close()

text = "alice.txt"
count_letters_occurs_in_alphabet_in_file(text)
































