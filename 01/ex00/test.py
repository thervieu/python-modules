from recipe import Recipe
from book import Book

if __name__ == "__main__":
    # Book()
    myBook = Book("myBook")
    print(str(myBook))

    # recipe1 = Recipe("recipe1", 10, 123, ['tomato', 'chip'], 'best recipe', 'lunch')
    # print(str(recipe1))

    # myBook.add_recipe(recipe1)
    # print(str(myBook))

    # print(str(myBook.get_recipe_by_name("recipe1")))
    # print(str(myBook.get_recipe_by_name("recipe_does_not_exist")))

    # recipe1 = Recipe("starter1", 1, 1, ['1', '2', '3'], 'best recipe1', 'starter')
    # recipe2 = Recipe("starter2", 2, 2, ['1', '2', '3'], 'best recipe2', 'starter')
    # recipe3 = Recipe("starter3", 3, 3, ['1', '2', '3'], 'best recipe3', 'starter')
    # myBook.add_recipe(recipe1)
    # myBook.add_recipe(recipe2)
    # myBook.add_recipe(recipe3)

    # for recipe in myBook.get_recipes_by_types('starter'):
    #     print(str(recipe))

    # print(str(myBook.get_recipe_by_name("starter3")))
    # print(str(myBook))
