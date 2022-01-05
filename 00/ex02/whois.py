import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit()
    nb = sys.argv[1]
    if nb.isnumeric() is True:
        num = int(nb)
    elif (nb.startswith('-') is True and nb[1::].isdigit() is True):
        num = int(nb)
    else:
        print("ERROR")
        sys.exit()
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
