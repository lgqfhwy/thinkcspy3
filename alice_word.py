def text_to_words(the_text):
    """ 
        Return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")
    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
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
    maxmun = 0
    for (k, v) in letter_items:
        if len(k) > maxmun:
            maxmun = len(k)
            i = k
        if len(k) < 4:
            m = 3
        elif len(k) < 8:
            m = 3
        else:
            m = 2
        endfile.writelines(str(k) + "\t" * m + str(v) + "\n")
        # endfile.write("\t\t\t")
        # endfile.write(str(v))
        # endfile.write("\n")
    endfile.close()
    print("The longest word is {0}, it has {1} characters.".format(i, maxmun))

text = "alice.txt"
count_letters_occurs_in_alphabet_in_file(text)









