import sys

l = len(sys.argv) 

if l == 3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("InputError: only numbers")
else:
    if l > 3:
        print("InputError: too many arguments ")
    print("Usage: python operations.py\n\
Example:\n\
    python operations.py 10 3\n")
    sys.exit(1)

print(f"Sum:        {x + y}\n\
Difference: {x - y}\n\
Product:    {x * y}")

try:
    print(f"Quotient:   {x / y}")
    print(f"Remainder: {x % y}\n")
except ZeroDivisionError:
    print("Quotient:    ERROR (div by zero)")
    print("Remainder: ERROR (modulo by zero)\n")
