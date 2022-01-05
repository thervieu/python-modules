
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
        print(recipe)
        while True:

            print("What type of meal is it ? (lunch, dessert)")
            print(">> ", end='')
            input_ = input()
            if input_ == 'lunch' or input_ == 'dessert':
                recipe.append(input_)
                break
            print("type not authorized\n")
        print(recipe)
        while True:

            print("How long to cook it ? (uint please)")
            print(">> ", end='')
            input_ = input()
            try:
                mytime = int(input_)
            except input_.isnum() is False:
                print("please input an int\n")
                continue
            if mytime <= 0:
                print("please input a positive int > 0\n")
                continue
            recipe.append(input_)
            print(recipe)
            break
    return


def delRecipe():
    print("Please enter the recipe's name you want to delete:")
    print(">> ", end='')
    input_ = input()
    if input_ in recipes:
        del recipes[input_]
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
        print("Takes {} minutes of cooking.".format(recipe[-1]))
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
        try:
            nb = int(input_w)
        except input_.isnum() is False:
            print("This option does not exist, {}".format(
                "please type the corresponding number.\nTo exit, enter 5."
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
                "please type the corresponding number.\nTo exit, enter 5."
            ))
    print("Goodbye!")
