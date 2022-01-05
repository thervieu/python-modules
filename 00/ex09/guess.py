import sys
from random import randint

if __name__ == "__main__":
    rand_num = randint(1, 99)
    guess_count = 0
    while True:
        print("What's your guess between 1 and 99?")
        print(">> ", end='')
        input_ = input()
        guess_count += 1
        try:
            num = int(input_)
        except input_.isnum() is False:
            if input_ == 'exit':
                print('Goodbye!')
                sys.exit()
            print("That's not a number.")
            continue
        if num == rand_num:
            break
        print("Too high!" if num > rand_num else "Too low!")
    print('Congratulations, you\'ve got it!')
    print('You won in {} attempts!'.format(guess_count))
