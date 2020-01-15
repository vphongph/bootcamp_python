
class Recipe:	
	@staticmethod
	def info():
		return ("Recipe class, instance with\n\
	- name (str)\n\
	- cooking_lvl (int) : range 1 to 5\n\
	- cooking_time (int) : in minutes (no negative numbers)\n\
	- ingredients (list) : list of all ingredients each represented by a string\n\
	- recipe_type (str) : can be 'starter', 'lunch' or 'dessert'\n\
	- description (str) (can be empty) : description of the recipe\n")

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
		
		if not (isinstance(name, str) and isinstance(recipe_type, str)):
			raise TypeError(f"name and recipe_type must be a str")

		if description and not isinstance(description, str):
			raise TypeError(f"description must be a str")
		
		if not (isinstance(cooking_lvl, int) and isinstance(cooking_time, int)):
			raise TypeError(f"cooking_lvl and cooking_time and must be an int")

		if cooking_lvl < 1 or cooking_lvl > 5:
			raise ValueError(f"cooking_lvl must be between 1 and 5")

		if cooking_time < 0:
			raise ValueError(f"cooking_time can't be negative")


		if not isinstance(ingredients, list):
			raise TypeError(f"ingredients must be a list")

		self.name = name
		self.cooking_lvl = cooking_lvl	
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
 		return (f"Recipe of {self.name}\n\
	Level {self.cooking_lvl} of complexity\n\
	{self.cooking_time} minute(s) to cook\n\
	Ingredients : {self.ingredients}\n\
	To be eaten as {self.recipe_type}\n\
	Note : {self.description}\n")

