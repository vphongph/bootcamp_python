import sys

if len(sys.argv) == 1:
    sys.exit(1)

if len(sys.argv) > 2 or not sys.argv[1].isdigit():
    print("ERROR")
    sys.exit(1)

# try:
#   int(sys.argv[1])
# except ValueError:
#   print("ERROR")
#   sys.exit(1)

if sys.argv[1] == "0":
    print("I'm Zero.")
elif int(sys.argv[1]) % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
