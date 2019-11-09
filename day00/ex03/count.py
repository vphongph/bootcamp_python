import sys
import string


def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,\n\
punctuation and spaces in a given text.
    """
    if not text:
        print("What is the text to analyse?")
        text = sys.stdin.read()
        # text = sys.stdin.readline()

    if not isinstance(text, str):
        print("argument have to be a string")
        return

    length = len(text)
    upper = sum(map(str.isupper, text))
    lower = sum(map(str.islower, text))
    punct = sum([1 for i in text if i in string.punctuation])
    space = sum(map(str.isspace, text))

    print(f"The text contains {length:d} characters:\n\
- {upper:d} upper letters\n\
- {lower:d} lower letters\n\
- {punct:d} punctuation marks\n\
- {space:d} spaces")