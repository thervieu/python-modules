class Recipe:
    def __init__(self, name=str, cooking_lvl=int, cooking_time=int, ingredients=list, description=str, recipe_type=str):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__ (self):
        txt = ""
        txt = '{}:\ncooking_lvl: {}\ncooking_time: {}\ningredients: {}\ndescription: {}\nncooking_lvl: {}\n'.format(
                self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt
