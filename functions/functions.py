def sum_to(n):
    """ Return the sum of 1 + 2 + 3 ... n """
    ss = 0
    for v in range(n + 1):
        ss = ss + v
    return ss


def seq3np1(n):
    """ Print the 3n + 1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end = ", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end = ".\n")


def num_digits(n):
    count = 0
    if n == 0:
        return 1
    if n < 0:
        n = -n
    while n != 0:
        count = count + 1
        n = n // 10
    return count


# a = num_digits(-12345)
# print(a)


def num_zero_and_five_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count


def print_multiples(n, high):
    for i in range(1, high + 1):
        print(n * i, end = "\t")
    print()


def print_mult_table(high):
    for i in range(1, high + 1):
        print_multiples(i, i)


# celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]
# # print(celebs)
# # print(len(celebs))

# for (nm, yr) in celebs:
#     if yr < 1980:
#         print(nm)


def sqrt(n):
    approx = n / 2.0
    while True:
        better = (approx + n / approx) / 2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

#print(sqrt(25))
# print(sqrt(25.0))
# print(sqrt(49.0))
# print(sqrt(81.0))


def count_odd_numbers(list):
    count = 0
    for x in list:
        if x % 2 == 1:
            count += 1
    return count


def count_words_length_five(list):
    count = 0
    for word in list:
        if len(word) == 5:
            count = count + 1
    return count


def print_triangular_numbers(n):
    for i in range(1, n + 1):
        a = i * (i + 1) // 2
        print(i, "\t", a)


#print_triangular_numbers(5)


def is_prime(n):
    a = n ** 0.5 + 1
    t = int(a)
    for i in range(2, t):
        if n % i == 0:
            return False
    return True

# print(is_prime(11))
# print(is_prime(35))
# print(is_prime(19941019))
# print(is_prime(19911121))


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels


#print(remove_vowels("compsci"))
def find(strng, ch):
    """
        Find and return the index of ch in strng.
        Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#print(find("compsci", "p"))
def count_word(text, word):
    count = 0
    for c in text:
        if c == word:
            count += 1
    return (count)

#print(count_word("banana", "a"))


def find2(strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#print(find2("banana", "a", 4))


def find4(strng, ch, start = 0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def find5(strng, ch, start = 0, end = None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


import string

def remove_punctuation(s):
    #punctuation = "!\"#$%'()*+,-./:;<=>?@[\\]^_'{|}~"
    s_sans_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_sans_punct += letter
    return s_sans_punct
#print(remove_punctuation("Wo/d"))


# s1 = "His name is {}!".format("Arthur")
# print(s1)

# name = "Alice"
# age = 10
# s2 = "I am {1} and I am {0} years old.".format(age, name)
# print(s2)

# n1 = 4
# n2 = 5
# s3 = "2 ** 10 = {0} and {1} * {2} = {3:.1f}".format(2 ** 10, n1, n2, n1 * n2)
# print(s3)


# n1 = "Paris"
# n2 = "Whitney"
# n3 = "Hilton"
# print("|||{0:<8}|||{1:^15}|||{2:>15}|||Born in {3}|||".format(n1, n2, n3, 1981))


def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    print(count)
    return count

#count_letters("banana", "a")


def count_letters2(string, letter):
    count = 0
    index = 0
    while index != -1:
        a = string.find(letter, index)
        if a == -1:
            print(count)
            return(count)
        else:
            count += 1
            index = a + 1

#count_letters2("banana", "a")


def multiplication_table(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print("{0} * {1} = {2}".format(i, j, i * j), end = "")
            if j != i + 1:
                print(end = " ")
        print()

#multiplication_table(12)


def reverse_string(string):
    lenth = len(string)
    new_string = ""
    for i in range(0, lenth):
        new_string += string[lenth - 1 - i]
    return new_string


# print(reverse_string("happy"))
# print(reverse_string("Python"))
# print(reverse_string(""))
# print(reverse_string("a"))


def mirror_string(string):
    new_string = string
    new_string += reverse_string(string)
    return new_string


# print(mirror_string("good"))
# print(mirror_string(""))
# print(mirror_string("Python"))
# print(mirror_string("a"))


def remove_letter(letter, string):
    ss = ""
    for i in string:
        if i != letter:
            ss += i
    return ss


# print(remove_letter("a", "apple"))
# print(remove_letter("a", "banana"))
# print(remove_letter("z", "banana"))
# print(remove_letter("i", "Mississippi"))
# print(remove_letter("b", ""))
# print(remove_letter("b", "c"))


def is_palindromes(string):
    new_string = reverse_string(string)
    ispa = True
    lenth = len(string)
    lenth = lenth // 2 + 1
    for i in range(0, lenth):
        if string[i] != new_string[i]:
            ispa = False
            break
    return ispa

#print(is_palindromes("abba"))


def count_substring(substring, string):
    count = 0
    length = len(substring)
    length2 = len(string)
    num = -1
    for i in string:
        num += 1
        if substring[0] == i:
            is_substring = True
            for j in range(0, length):
                if num + j >= length2 or substring[j] != string[num + j]:
                    is_substring = False
                    break
            if is_substring == True:
                count += 1
    return count

# print(count_substring("is", "Mississippi"))
# print(count_substring("an", "banana"))
# print(count_substring("nana", "banana"))
# print(count_substring("nanan", "banana"))
# print(count_substring("aaa", "aaaaaa"))


def remove_first_occur_string(substring, string):
    count = 0
    new_string = ""
    length = len(substring)
    length2 = len(string)
    num = -1
    for i in string:
        num += 1
        if substring[0] == i:
            is_substring = True
            for j in range(0, length):
                if num + j >= length2 or substring[j] != string[num + j]:
                    is_substring = False
                    break
            if is_substring == True:
                for m in range(0, num):
                    new_string += string[m]
                for m in range(num + length, length2):
                    new_string += string[m]
                return new_string
    return string

# print(remove_first_occur_string("an", "banana"))
# print(remove_first_occur_string("cyc", "bicycle"))
# print(remove_first_occur_string("iss", "Mississippi"))
# print(remove_first_occur_string("eggs", "bicycle"))

def remove_all_occur_string(substring, string):
    new_string = ""
    length1 = len(substring)
    length2 = len(string)
    i = 0
    while i < length2:
        if substring[0] != string[i]:
            new_string += string[i]
            i += 1
        else:
            is_substring = True
            for j in range(0, length1):
                if i + j >= length2 or substring[j] != string[i + j]:
                    is_substring = False
                    break
            if is_substring == True:
                i = i + length1
            else:
                new_string += string[i]
                i += 1
    return new_string


# print(remove_all_occur_string("an", "banana"))
# print(remove_all_occur_string("cyc", "bicycle"))
# print(remove_all_occur_string("iss", "Mississippi"))
# print(remove_all_occur_string("eggs", "bicycle"))


def pass_tuple(tuple):
    print(tuple[1])


pass_tuple(("jack", ["John", 1994]))

























