import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            print("InputError: too many arguments")
        if len(sys.argv) == 2:
            print("InputError: not enough arguments")
        print("Usage: {}Example:\n\tpythonoperations.py 10 3".format(
                "python operations.py <number1> <number2>\n"), end='')
        sys.exit()
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except sys.argv[1].isnum() is False or sys.argv[2].isnum() is False:
        print("InputError: only numbers")
        print("Usage: {}Example:\n\tpythonoperations.py 10 3".format(
                "python operations.py <number1> <number2>\n"), end='')
        sys.exit()
    print("Sum:\t\t{}".format(num1 + num2))
    print("Difference:\t{}".format(num1 - num2))
    print("Product:\t{}".format(num1 * num2))
    print("Quotient:\t{}".format("ERROR (div by zero)" if num2 == 0 else num1 / num2))
    print("Remainder:\t{}".format("ERROR (modulo by zero)" if num2 == 0 else num1 % num2), end='')
