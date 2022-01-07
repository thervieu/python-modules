class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if (isinstance(name, str) is False):
            raise TypeError("Recipe: name must be a string")
        if (name == ""):
            raise ValueError("Recipe: name must not be empty")
        if (isinstance(cooking_lvl, int) is False):
            raise TypeError("Recipe: cooking_lvl must be an int")
        if (cooking_lvl < 1):
            raise ValueError("Recipe: cooking_lvl must be strictly positive")
        if (isinstance(cooking_time, int) is False):
            raise TypeError("Recipe: cooking_time must be an int")
        if (cooking_time < 1):
            raise ValueError("Recipe: cooking_time must be strictly positive")
        if (isinstance(ingredients, list) is False):
            raise TypeError("Recipe: ingredients must be a list of strings")
        for s in ingredients:
            if (isinstance(s, str) is False):
                raise TypeError("Recipe: ingredient must be a string")
            if (s == ""):
                raise ValueError("Recipe: ingredients must not be empty")
        if (isinstance(description, str) is False):
            raise TypeError("Recipe: description must be a string")
        if (isinstance(recipe_type, str) is False):
            raise TypeError("Recipe: recipe_type must be a string")
        if (recipe_type != 'starter' and recipe_type != 'lunch'
                and recipe_type != 'dessert'):
            raise ValueError("Recipe: recipe_type must be in {}".format(
                "('starter','lunch', 'dessert')"))
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = ""
        txt = '{}:\n{}{}\n{}{}\n{}{}\n{}{}\nrecipe_type: {}\n'.format(
                self.name, "cooking_lvl: ", self.cooking_lvl, "cooking_time: ",
                self.cooking_time, "ingredients: ", self.ingredients,
                "description: ", self.description, self.recipe_type)
        return txt
