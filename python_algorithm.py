def search_liner(xs, target):
    """ Find and return the index of target in sequences xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_liner(vocab, w) < 0):
            result.append(w)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


# bigger_vocab = load_words_from_file("vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} "
#         .format(len(bigger_vocab)), bigger_vocab[:6])


def text_to_words(the_text):
    """ 
        Return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                            ")
    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words."""
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


# book_words = get_words_in_book("abc.txt")
# print("There are {0} words in the book, the first 100 are\n{1}".
#         format(len(book_words), book_words[:100]))


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
            return -1
        mid_index = (lb + ub) // 2
        item_at_mid = xs[mid_index]
        if item_at_mid == target:
            return mid_index
        elif item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index
        print("lb = ", lb, "ub = ", ub)

#print(search_binary([1, 3, 5], 5))


def remove_adjacent_dups(xs):
    """
        Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result


# all_words = get_words_in_book("ALiceInWonderland.txt")
# all_words.sort()
# book_words = remove_adjacent_dups(all_words)
# print("There are {0} words in the book. Only {1} are unique.".
#         format(len(all_words), len(book_words)))
# print("The first 100 words are\n{0}".
#         format(book_words[:100]))


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def find_unknows_merge_pattern(vocab, wds):
    """
        Both the vocab and wds must be sorted. Return a new 
        list of words from wds that do not occur in vocab.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result
        if yi >= len(wds):
            return result
        if vocab[xi] == wds[yi]:
            yi += 1
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            result.append(wds[yi])
            yi += 1



def merge_both_in_lists(first_list, second_list):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(first_list):
            return result
        if yi >= len(second_list):
            return result
        if first_list[xi] == second_list[yi]:
            result.append(first_list[xi])
            xi += 1
        elif first_list[xi] < second_list[yi]:
            xi += 1
        else:
            yi += 1


def in_first_not_second_increase_list(first_list, second_list, result):
    xi = 0
    yi = 0
    while True:
        if xi >= len(first_list):
            return result
        if yi >= len(second_list):
            result.extend(first_list[xi:])
            return result
        if first_list[xi] == second_list[yi]:
            xi += 1
        elif first_list[xi] < second_list[yi]:
            result.append(first_list[xi])
            #print(result)
            xi += 1
        else:
            yi += 1

def in_either_first_or_second(first_list, second_list, result):
    result = in_first_not_second_increase_list(first_list, second_list, result)
    result = in_first_not_second_increase_list(second_list, first_list, result)
    return result


# first_list = [1, 3, 5, 7]
# second_list = [2, 3, 4, 5]
# result = []
# #result = in_first_not_second_increase_list(first_list, second_list, result)
# #result = in_either_first_or_second(first_list, second_list, result)
# result = in_first_not_second_increase_list(second_list, first_list, result)
# print(result)



def bagdiff(first_list, second_list):
    xi = 0
    yi = 0
    result = []
    while True:
        if xi >= len(first_list):
            result.extend(second_list[yi:])
            return result
        if yi >= len(second_list):
            result.extend(first_list[xi:])
            return result
        if first_list[xi] == second_list[yi]:
            xi += 1
            yi += 1
        elif first_list[xi] < second_list[yi]:
            result.append(first_list[xi])
            xi += 1
        else:
            yi += 1

print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))























