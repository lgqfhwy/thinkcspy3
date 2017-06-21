def find_hypot(side1, side2):
    a = side1 ** 2 + side2 ** 2
    return a ** 0.5

# side1 = 3.5
# side2 = 4
# a = find_hypot(side1, side2)
# print(a)
def is_rightangled(side1, side2, longside):
    if side1 > side2 and side1 > longside:
        tmp = longside
        longside = side1
        side1 = tmp
    elif side2 > side1 and side2 > longside:
        tmp = longside
        longside = side2
        side2 = tmp
    a = side1 ** 2 + side2 ** 2
    a = a ** 0.5
    if abs(a - longside) < 0.0000001:
        return True
    return False

# a = is_rightangled(5, 4, 4)
# print(a)
import math
a = math.sqrt(2.0)
print(a, a * a)
print(a * a == 2.0)