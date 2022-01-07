import random


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if isinstance(text, str) is False:
        yield "ERROR: text not a string"
        return
    words = text.split(sep)
    if isinstance(option, str) and option in ('shuffle', 'unique', 'ordered'):
        if option == "shuffle":
            random.shuffle(words)
        elif option == "unique":
            words = list(set(words))
        elif option == "ordered":
            words = sorted(words)
    else:
        yield "ERROR: option should be in ('shuffle', 'unique', 'ordered')"
        return
    for elem in words:
        yield elem
