class GotCharacter:

    def __init__(self, first_name, is_alive):
        if (isinstance(first_name, str) is False):
            raise TypeError("Recipe: first_name must be a string")
        if (first_name == ""):
            raise ValueError("Recipe: first_name must not be empty")
        if (isinstance(is_alive, bool) is False):
            raise TypeError("Recipe: is_alive must be a string")
        if (is_alive is False):
            raise ValueError("Recipe: is_alive must be True on init")
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        txt = ""
        txt = '{}:\n{}{}\n{}{}\n{}{}\n{}{}\nrecipe_type: {}\n'.format(
                self.name, "cooking_lvl: ", self.cooking_lvl, "cooking_time: ",
                self.cooking_time, "ingredients: ", self.ingredients,
                "description: ", self.description, self.recipe_type)
        return txt


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
