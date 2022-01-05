import Recipe from recipe
import time

recipes_types = ('starter', 'lunch', 'dessert')

class Book:

    def __init__(self, name=str, last_update=time.Time, creation_date=time.Time, recipes_list=dict):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = {
            'starter': []
            'lunch': []
            'dessert': []
            }
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for item in self.recipes_list:
            for recipe in item[1]:
                if recipe.name == name:
                    return recipe
        
        return None

    def get_recipes_by_types(self, recipe_type=str):
        """Get all recipe names for a given recipe_type """
        if recipes_type is in
        return recipes_list[recipe_type]

    def add_recipe(self, recipe=Recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
