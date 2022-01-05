import sys
from random import randint

if __name__ == "__main__":
    print("{}{}{}".format(
        "This is an interactive guessing game!\nYou have to enter a number",
        "between 1 and 99 to find out the secret number.\n",
        "Type 'exit' to end the game.\nGood luck!\n"))
    rand_num = randint(1, 99)
    guess_count = 0
    while True:
        print("What's your guess between 1 and 99?")
        print(">> ", end='')
        input_ = input()
        guess_count += 1
        if input_.isnumeric() is True:
            num = int(input_)
        else:
            if input_ == 'exit':
                print('Goodbye!')
                sys.exit()
            print("That's not a number.")
            continue
        if num == rand_num:
            break
        print("Too high!" if num > rand_num else "Too low!")
    if rand_num == 42:
        print("{}{}".format(
            "The answer to the ultimate question of life, ",
            "the universe and everything is 42."))
    if guess_count != 1:
        print('Congratulations, you\'ve got it!')
        print('You won in {} attempts!'.format(guess_count))
    else:
        print('Congratulations, you got it on your first try!')
