import sys
import string

def text_analyser(text=None):
	"Hello"
	if not text:
		return

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

# text_analyser(87987)
text_analyser("	qweqweq  we:L:K:98989   8(*(*(*   ")
print(text_analyser.__doc__)

