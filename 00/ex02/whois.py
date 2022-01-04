import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit()
    try:
        argvint = int(sys.argv[1])
    except:
        print("ERROR")
        sys.exit()
    if argvint % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
