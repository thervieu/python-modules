import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            print("InputError: too many arguments")
        if len(sys.argv) == 2:
            print("InputError: not enough arguments")
        print("Usage: {}Example:\n\tpythonoperations.py 10 3".format(
                "python operations.py <number1> <number2>\n"))
        sys.exit()
    nb = sys.argv[1]
    nb2 = sys.argv[2]
    if nb.isnumeric() is True:
        num1 = int(nb)
    elif (nb.startswith('-') is True and nb[1::].isdigit() is True):
        num1 = int(nb)
    else:
        print("InputError: only numbers")
        print("Usage: {}Example:\n\tpython operations.py 10 3".format(
                "python operations.py <number1> <number2>\n"))
        sys.exit()
    if nb2.isnumeric() is True:
        num2 = int(nb2)
    elif (nb2.startswith('-') is True and nb2[1::].isdigit() is True):
        num2 = int(nb2)
    else:
        print("InputError: only numbers")
        print("Usage: {}Example:\n\tpython operations.py 10 3".format(
                "python operations.py <number1> <number2>\n"))
        sys.exit()
    print("Sum:\t\t{}".format(num1 + num2))
    print("Difference:\t{}".format(num1 - num2))
    print("Product:\t{}".format(num1 * num2))
    print("Quotient:\t{}".format(
        "ERROR (div by zero)" if num2 == 0 else num1 / num2))
    print("Remainder:\t{}".format(
        "ERROR (modulo by zero)" if num2 == 0 else num1 % num2))
