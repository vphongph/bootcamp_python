import sys
import re
import string

if len(sys.argv) == 3 and not sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
	output = list(filter(lambda x : len(x) > int(sys.argv[2]), re.sub('\s+',' ',sys.argv[1].translate(str.maketrans('', '', string.punctuation))).strip().split(' ')))
	print(output)
else:
	print("ERROR")