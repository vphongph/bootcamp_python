from book import Book
from recipe import Recipe
import datetime

ketchup = Recipe("ketchup", 1, 0, ['tomato','sugar'], "dessert", "Sweeeeeet")

# print (Recipe.info())
# print (ketchup)


book = Book("Magic", datetime.date.today(), datetime.date.today(), {'dessert':[ketchup]})

print (book.get_recipe_by_name(ketchup))

# import gc
# for obj in gc.get_objects():
    # if isinstance(obj, Recipe) and obj.:
        # print(obj.name)
