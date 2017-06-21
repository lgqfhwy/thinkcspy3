import string
def remove_punctuation(s):
    ss = ""
    for letter in s:
        if letter not in string.punctuation:
            ss += letter
    return ss

def count_letter_in_text(text, letter):
    count_word = 0
    count_letter = 0
    text_remove_punctuation = remove_punctuation(text).split()
    for ch in text_remove_punctuation:
        count_word += 1
        for le in ch:
            if le == letter:
                count_letter += 1
                break
    print("Your text contains {0} worlds, of which {1} ({2:.1f}%) contain an \"{3}\""
            .format(count_word, count_letter, count_letter * 1.0 / count_word * 100, letter))
    return (count_word, count_letter)


text = """
            In the following examples, input and output are distinguished by
            the presence or absence of prompts (>>> and ...): to repeat the 
            example, you must type everything after the prompt, when the prompt 
            appears; lines that do not begin with a prompt are output from the 
            interpreter. Note that a secondary prompt on a line by itself in 
            an example means you must type a blank line; this is used to end 
            a multi-line command.
        """
count_letter_in_text(text, 'e')










