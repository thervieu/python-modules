import sys
from string import punctuation


def text_analyzer(*args):
    """Counts the number of upper, lower, punctuation and spaces
in the given text"""
    if len(args) > 1:
        print("ERROR")
        return
    elif len(args) == 1:
        text = args[0]
    else:
        print("What is the text to analyse?")
        print(">> ", end='')
        text = input()
    print("The text contains {} characters".format(len(text)))
    print("- {} upper letters".format(sum(1 for c in text if c.isupper())))
    print("- {} lower letters".format(sum(1 for c in text if c.islower())))
    print("- {} punctuation".format(sum(1 for c in text if c in punctuation)))
    print("- {} spaces\n".format(sum(1 for c in text if c.isspace())))
