class MyTime:

    def __init__(self, hrs = 0, mins = 0, secs = 0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized. """
        # Calculate total seconds to represent
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60


    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours, self.minutes, self.seconds)



    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        while self.minutes < 0:
            self.minutes += 60
            self.hours -= 1
        return self

    def increment_short(self, seconds):
        sec = self.to_seconds()
        sec += seconds
        return MyTime(0, 0, sec)


    def to_seconds(self):
        """ Return the number of seconds represented by this instance """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __gt__(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()


    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def between(self, other):
        """ 
            Return True if the invoking object falls between the
            two times. Assume self <= other
        """
        sec1 = self.to_seconds()
        sec2 = self.to_seconds()
        if sec1 <= sec2:
            return True
        return False


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)


def increment(t, secs):
    t.seconds += secs

    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 1

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1

# t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# t3 = t1 + t2
# print(t3)


class Point:
    """ Point class represents and manipulates x, y coords. """
    def __init__(self, x = 0, y = 0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

# p1 = Point(3, 4)
# p2 = Point(5, 7)
# print(p1 * p2)
# print(2 * p2)
#print(p2 * 2)

def multadd(x, y, z):
    return x * y + z

# print(multadd(3, 2, 1))
# p1 = Point(3, 4)
# p2 = Point(5, 7)
# print(multadd(2, p1, p2))
# print(multadd(p1, p2, 1))


def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front), str(back))

# my_list = [1, 2, 3, 4]
# front_and_back(my_list)
# p = Point(3, 4)
# front_and_back(p)
def between(t1, t2):
    """ Returns True if the invoking object falls between
        the two times. Assume t1 <= t2. """
    sec1 = t1.to_seconds()
    sec2 = t1.to_seconds()
    if sec1 <= sec2:
        return True
    return False

t1 = MyTime(0, 1, 3)
t2 = MyTime(2, 3, 4)
# print(between(t1, t2))
# print(t1.between(t2))
# print(t1.after(t2))
# print(t1 > t2)
# print(t1.increment(-50))
# t1 = MyTime(0, 1, 3)
# print(t1.increment_short(-50))


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit = 0, rank = 0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0

    def cmp_diff(self, other):
        if self.suit > self.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank < self.rank: return 1
        if self.rank > self.rank: return -1

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


# card2 = Card(1, 3)
# print(card2)
# print(card2.suits[2])
# card1 = Card(1, 11)
# card2 = Card(1, 3)
# card3 = Card(1, 11)
# print(card1 == card3)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle_origin(self):
        import random
        rng = random.Random()   # Create a random generator
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i, num_cards)
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards = 999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)



red_deck = Deck()
# blue_deck = Deck()

#red_deck.print_deck()


class Hand(Deck):
    def __init__(self, name = ""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)


# deck = Deck()
# deck.shuffle()
# hand = Hand("frank")
# deck.deal([hand], 5)
# print(hand)

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()



class OldMailHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}"
                        .format(self.name, card, match))
                count += 1
        return count



# game = CardGame()
# hand = OldMailHand("frank")
# game.deck.deal([hand], 13)
# print(hand)
# hand.remove_matches()
# print(hand)                                                                                                              


class OldMaidGame(CardGame):

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def play(self, names):
        # Remove Queen of clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMailHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt.")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor


# game = OldMaidGame()
# game.play(["Allen", "Jeff", "Chris"])

import turtle
class TurtleGTX(turtle.Turtle):

    def __init__(self):
        self.screen = turtle.Screen()
        self.odometer = 0
        self.turtle = turtle.Turtle()
        self.tyre_break = 150



    def print_odometer(self):
        print("Odometer = ", self.odometer)

    def jump_forward(self, distance):
        self.turtle.penup()
        self.turtle.forward(distance)
        self.turtle.pendown()
        dis = distance
        if dis < 0:
            dis = -dis
        self.odometer += dis

    def forward(self, distance):
        if self.odometer >= self.tyre_break:
            print("Error")
            raise ValueError("The turtle break down with a flat tyre,you should change tyre.")
        else:
            self.turtle.forward(distance)
            dis = distance
            if dis < 0:
                dis = -dis
            self.odometer += dis

    def change_tyre(self, tyre_top = 150):
        self.tyre_break += tyre_top



# tess = TurtleGTX()
# tess.print_odometer()
# tess.jump_forward(50)
# tess.print_odometer()
# tess.jump_forward(-50)
# tess.print_odometer()
# tess.forward(49)
# tess.forward(50)
# tess.change_tyre()
# tess.forward(13)
# tess.print_odometer()
# tess.screen.mainloop()


class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    # def print_backward(self):
    #     if self.next is not None:
    #         tail = self.next
    #         tail.print_backward()
    #     print(self.cargo, end = " ")

def remove_second(list):
    if list is None: return
    if list.next is None: return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

def print_list(node):
    print("[", end = "")
    while node is not None:
        print("{0}".format(node), end = "")
        node = node.next
        if node is not None:
            print(",", end = " ")
    print("]")

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end = " ")



# node = Node("test")
# print(node)
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3
# print_list(node1)
# print_backward(node1)
# print_list(node1)
# removed = remove_second(node1)
# print_list(removed)
# print_list(node1)
def print_backward_nicely(list):
    print("[", end = " ")
    print_backward(list)
    print("]")





class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end = " ")
        if self.head is not None:
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1


# node = LinkedList()
# node.print_backward()


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ("{0}".format(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


# Evaluating posfix
def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    #print(token_list)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()


# print(eval_postfix("56 47 + 2 *"))
# print(eval_postfix("1 2 + 3 *"))
#print(eval_postfix("1 2 3 * +"))


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        print("self.head.cargo = ", self.head.cargo)
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

# a = Queue()
# a.insert(3)
# print(a.remove())



class Queue_list:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, cargo):
        self.items.append(cargo)

    def remove(self):
        if self.is_empty():
            return
        return self.items.pop(0)


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node

        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


class PriorityQueue_linkedlist:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node

        self.length += 1

    def remove(self):
        re_maxi = self.head
        refer = self.head
        maxi = self.head
        while refer:
            if refer.cargo > maxi.cargo:
                re_maxi = refer_re
                maxi = refer
            refer_re = refer
            refer = refer.next
        re_maxi.next = maxi.next
        maxi.next = None
        self.length -= 1
        return maxi.cargo


# q = PriorityQueue_linkedlist()
# q.insert(3)
# while not q.is_empty():
#     print(q.remove())










# q = PriorityQueue()
# for num in [11, 12, 14, 13]:
#     q.insert(num)

# while not q.is_empty():
#     print(q.remove())


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score

# tiger = Golfer("Tiger Woods", 61)
# phil = Golfer("Phil Mickelson", 72)
# hal = Golfer("Hal Sutton", 69)

# pq = PriorityQueue()
# for g in [tiger, phil, hal]:
#     pq.insert(g)

# while not pq.is_empty():
#     print(pq.remove())


# import time
# t0 = time.clock()
# q = PriorityQueue()
# for num in range(1000, 0, -1):
#     q.insert(num)

# while not q.is_empty():
#     q.remove()

# t1 = time.clock()
# print("The first took {0:.4f} seconds.".format(t1 - t0))



# t2 = time.clock()
# p = PriorityQueue_linkedlist()
# for num in range(1000, 0, -1):
#     p.insert(num)

# while not p.is_empty():
#     p.remove()

# t3 = time.clock()
# print("The Second took {0:.4f} seconds.".format(t3 - t2))


class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def print_tree_preorder(tree):
    if tree is None: return 
    #print(tree.cargo, end = " ")
    print(tree.cargo)
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)

def print_tree_postorder(tree):
    if tree is None: return 
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end = " ")

def print_tree_inorder(tree):
    if tree is None: return 
    print_tree_inorder(tree.left)
    print(tree.cargo, end = " ")
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level = 0):
    if tree is None: return
    print_tree_indented(tree.right, level + 1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level + 1)

def print_tree_inorder_indented(tree):
    if tree is None: return
    if tree.left:
        print("(", end = " ")
    print_tree_inorder_indented(tree.left)
    print(tree.cargo, end = " ")
    print_tree_inorder_indented(tree.right)
    if tree.right:
        print(")", end = " ")

def is_digit(token):
    if token.isdigit():
        return int(token)
    try:
        result = float(token)
        isFloat = True
    except:
        isFloat = False
    if isFloat:
        return result
    return False


def string_to_token_list(string):
    import re
    token_list = re.split("([^0-9])", string)
    result = []
    for token in token_list:
        if token == "" or token == " ":
            continue
        to = is_digit(token)
        if to:
            result.append(to)
            continue
        result.append(token)
    result.append("end")
    return result

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_num(token_list)
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)


def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return Tree("*", a, b)
    return a


def get_num(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_num(token_list)
        return Tree("+", a, b)
    return a



def save_tree_preorder_in_list(tree, result):
    if tree is None: return 
    result.append(tree.cargo)
    save_tree_preorder_in_list(tree.left, result)
    save_tree_preorder_in_list(tree.right, result)
    return result

def save_tree_inorder_in_list(tree, result):
    if tree is None: return
    save_tree_inorder_in_list(tree.left, result)
    result.append(tree.cargo)
    save_tree_inorder_in_list(tree.right, result)
    return result


# left = Tree(2)
# right = Tree(3)
# tree = Tree(1, left, right)
# result = []
# save_tree_preorder_in_list(tree, result)
#print(result)


def pose_list_in_tree(result_preorder, result_inorder):
    if len(result_preorder) == 0:
        return 
    first = result_preorder[0]
    for i in range(0, len(result_inorder)):
        if result_inorder[i] == first:
            break
    tree = Tree(first)
    left = pose_list_in_tree(result_preorder[1 : i + 1], result_inorder[0 : i])
    right = pose_list_in_tree(result_preorder[i + 1 :], result_inorder[i + 1:])
    return Tree(tree, left, right)

    
# result_preorder123 = [1, 2, 3]
# result_inorder123 = [3, 2, 1]
# tree = pose_list_in_tree(result_preorder123, result_inorder123)
#print_tree_preorder(tree)
# print()
# print_tree_postorder(tree)

def save_tree_in_file(tree):
    result_preorder = []
    save_tree_preorder_in_list(tree, result_preorder)
    result_inorder = []
    save_tree_inorder_in_list(tree, result_inorder)
    myfile = open("tree.txt", "w")
    for v in result_preorder:
        myfile.write(str(v))
        myfile.write("@")
    myfile.write("\n")
    for v in result_inorder:
        myfile.write(str(v))
        myfile.write("@")
    myfile.write("\n")
    myfile.close()

def read_tree_in_file():
    myfile = open("tree.txt", "r")
    result_preorder_str = myfile.readline()
    result_preorder = result_preorder_str.split("@")
    result_preorder.pop()
    result_inorder_str = myfile.readline()
    result_inorder = result_inorder_str.split("@")
    result_inorder.pop()
    tree = pose_list_in_tree(result_preorder, result_inorder)
    return tree


# save_tree_in_file(tree)
# read_tree_in_file()
# print_tree_preorder(tree456)


# root = Tree("bird")
# save_tree_in_file(root)
# root123 = read_tree_in_file()
# print_tree_preorder(root123)






def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    Root = read_tree_in_file()
    # Start with a singleton
    root = Root
    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break
        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = str(tree.cargo)+ "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left
        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + str(guess) + "? "
        if yes(prompt):
            print("I rule!")
            continue
        # Get new information
        prompt = "What is the animal's name? "
        animal = input(prompt)
        prompt = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))
        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
    save_tree_in_file(Root)

animal()
# Root = read_tree_in_file()
# print_tree_preorder(Root)





























































