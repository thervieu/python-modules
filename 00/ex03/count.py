import sys
from string import punctuation

def text_analyzer(text):
    if text == "":
        print("Please input a text")
        sys.exit()
    print("The text contains {} characters".format(len(text)))
    print("- {} upper letters".format(sum(1 for c in text if c.isupper())))
    print("- {} lower letters".format(sum(1 for c in text if c.islower())))
    print("- {} punctuation".format(sum(1 for c in text if c in punctuation)))
    print("- {} spaces".format(sum(1 for c in text if c == ' ')))
