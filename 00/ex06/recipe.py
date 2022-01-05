
recipes = {
        'sandwich': ('ham', 'bread', 'cheese', 'tomatoes', 'lunch', '10'),
        'cake': ('flour', 'sugar', 'eggs', 'dessert', '60'),
        'salad': ('avocado', 'arugula', 'tomatoes', 'spinach', 'lunch', '15')
    }


def addRecipe():
    print("Please enter the NEW recipe's name:")
    print(">> ", end='')
    input_ = input()
    if input_ in recipes:
        print("Recipe already exists\n")
    else:
        recipes[str(input_)] = []
        recipe = recipes[input_]
        while True:

            print("Please enter a new ingredient:")
            print("if that's enough, input 'ok'")
            print(">> ", end='')
            input_ = input()
            if input_ == 'ok':
                break
            recipe.append(input_)
        while True:

            print("What type of meal is it ? (lunch, dessert)")
            print(">> ", end='')
            input_ = input()
            if input_ == 'lunch' or input_ == 'dessert':
                recipe.append(input_)
                break
            print("type not authorized\n")
        while True:

            print("How long to cook it ? (uint please)")
            print(">> ", end='')
            nb = input()
            if nb.isnumeric() is True:
                time = int(nb)
            elif (nb.startswith('-') is True and nb[1::].isdigit() is True):
                time = int(nb)
            else:
                print("please input an int\n")
                continue
            if time <= 0:
                print("please input a positive int > 0\n")
                continue
            recipe.append(nb)
            break
    return


def delRecipe():
    print("Please enter the recipe's name you want to delete:")
    print(">> ", end='')
    input_ = input()
    if input_ in recipes:
        del recipes[input_]
        print("{} deleted!\n".format(input_))
    else:
        print("Recipe already does not exist\n")


def printRecipe():
    print("Please enter the recipe's name to get its details:")
    print(">> ", end='')
    input_ = input()
    if input_ in recipes:
        recipe = recipes[input_]
        print("Recipe for {}".format(input_))
        print("Ingredients list: {}".format(recipe[:-2:]))
        print("To be eaten for {}.".format(recipe[-2]))
        print("Takes {} minutes of cooking.\n".format(recipe[-1]))
    else:
        print("Recipe does not exist\n")


def printCookBook():
    print("Here are all the recipes:")
    for recipe in recipes.items():
        print("{}".format(recipe[0]))
    print("")


if __name__ == "__main__":
    while True:
        print("{}{}{}".format(
            "Please select an option by typing the corresponding number:\n",
            "1: Add a recipe\n2: Delete a recipe\n",
            "3: Print a recipe\n4: Print the cookbook\n5: Quit"
        ))
        print(">> ", end='')
        input_w = input()
        if input_w.isnumeric() is True:
            nb = int(input_w)
        else:
            print("This option does not exist, {}".format(
                "please type the corresponding number.\nTo exit, enter 5.\n"
            ))
            continue
        if nb == 1:
            addRecipe()
        elif nb == 2:
            delRecipe()
        elif nb == 3:
            printRecipe()
        elif nb == 4:
            printCookBook()
        elif nb == 5:
            break
        else:
            print("This option does not exist, {}".format(
                "please type the corresponding number.\nTo exit, enter 5.\n"
            ))
    print("Goodbye!")
