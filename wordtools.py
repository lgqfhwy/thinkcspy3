import string
def cleanword(str):
    ss = ""
    for letter in str:
        if letter not in string.punctuation:
            ss += letter
    return ss

#print(cleanword("what what"))
# print(cleanword("'now'"))
# print(cleanword("?+='w-o-r-d!,@$()'"))

def has_dashdash(str):
    length = len(str)
    for i in range(0, length):
        if str[i] == '-':
            if i < length - 1:
                if str[i + 1] == '-':
                    return True
    return False

# print(has_dashdash("distance--but"))
# print(not has_dashdash("several"))
# print(has_dashdash("spoken--"))
# print(not has_dashdash("-yo-yo-"))

def extract_words(str):
    ss = ""
    for letter in str:
        if letter in string.punctuation:
            ss += " "
        else:
            ss += letter
    new_list = ss.split()
    num = -1
    for i in new_list:
        num += 1
        new_list[num] = i.lower()
    return new_list

# print(extract_words("Now is the time! 'Now', is the time? Yes, now"))
# print(extract_words("she tried to curtsey as she spoke--fancy"))

def wordcount(substr, words):
    count = 0
    for i in words:
        if i == substr:
            count += 1
    return count

# ss = ["now", "is", "time", "is", "now", "is", "is"]
# print(wordcount("now", ss))
# print(wordcount("is", ss))
# print(wordcount("time", ss))
# print(wordcount("frog", ss))


def longestword(words):
    longest = 0
    sum = 0
    for i in words:
        sum = len(i)
        if sum > longest:
            longest = sum
    return longest

# print(longestword(["a", "apple", "pear", "grape"]))
# print(longestword(["a", "am", "I", "be"]))
# print(longestword(["this", "supercalifragilisticexpialidocious"]))
# print(longestword([]))
