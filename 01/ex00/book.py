from recipe import Recipe
from datetime import datetime


class Book:

    def __init__(self, name):
        if (isinstance(name, str) is False):
            raise TypeError("Book: name must be a string")
        if (name == ""):
            raise ValueError("Book: name must not be empty")
        self.name = name
        print("name", self.name)
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        print("date:", self.creation_date)
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
            }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name}
            and returns the instance"""
        if (isinstance(name, str) is False):
            raise TypeError("Book: get_recipe_by_name: name must be a string")
        for item in self.recipes_list:
            for recipe in self.recipes_list[item]:
                if recipe.name == name:
                    self.last_update = datetime.now()
                    return recipe
        print("No recipe with name '{}'".format(name))
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (isinstance(recipe_type, str) is False):
            raise TypeError("Book: get_recipes_by_types: {}".format(
                "recipe_type must be a string"
            ))
        if (recipe_type != 'starter' and recipe_type != 'lunch'
                and recipe_type != 'dessert'):
            raise ValueError("Book: get_recipes_by_types: {}{}".format(
                "recipe_type must be in ",
                "('starter','lunch', 'dessert')"))
        self.last_update = datetime.now()
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        if (isinstance(recipe, Recipe) is False):
            raise TypeError("Book: add_recipe: recipe must be a Recipe")
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def __str__(self):
        txt = ""
        txt = '{}\n{}{}\nlast_update: {}\nrecipes_list:\n\n'.format(
            self.name,
            "creation_date: ",
            self.creation_date,
            self.last_update)
        for item in self.recipes_list:
            for recipe in self.recipes_list[item]:
                txt += str(recipe) + '\n'
        return txt
