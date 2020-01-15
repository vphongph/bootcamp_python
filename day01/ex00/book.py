from recipe import Recipe
import datetime


class Book:	
	@staticmethod
	def info():
		return ("Recipe class, instance with\n\
	- name (str)\n\
	- last_update (datetime)\n\
	- creation_date (datetime)\n\
	- recipes_list (dict) : a dictionnary why 3 keys: 'starter', 'lunch', 'dessert'\n")

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		return Recipe.__str__(name)

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		pass

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		pass

	def __init__(self, name, last_update, creation_date, recipes_list=None):
		
		if not isinstance(name, str):
			raise TypeError(f"name must be a str")

		if not isinstance(last_update, datetime.date):
			raise TypeError(f"last_update must be a datetime")

		if not isinstance(creation_date, datetime.date):
			raise TypeError(f"last_update must be a datetime")

		if not isinstance(recipes_list, dict):
			raise TypeError(f"recipes_list must be a dict")

		self.name = name
		self.last_update = last_update	
		self.creation_date = creation_date
		self.recipes_list = recipes_list

	# def __str__(self):
		# return (f"Recipe of {self.name}\n\
	# Level {self.cooking_lvl} of complexity\n\
	# {self.cooking_time} minute(s) to cook\n\
	# Ingredients : {self.ingredients}\n\
	# To be eaten as {self.recipe_type}\n\
	# Note : {self.description}\n")


# lol = Recipe("ketchup", 1, 0, ['tomato','sugar'], "sauce", "Sweeeeeet")

# print (Recipe.info())
# print (lol)