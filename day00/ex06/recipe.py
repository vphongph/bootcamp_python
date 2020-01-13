import sys
import re
import os.path

# cookbook = {'sandwich':
# 			{
# 				'ingredients':
# 				[
# 					'ham', 'bread', 'cheese' ,'tomatoes'
# 				],
# 				'meal':'lunch',
# 				'prep_time':'10',
# 			},
# 			'cake':
# 			{
# 				'ingredients':
# 				[
# 					'flour', 'sugar', 'eggs'
# 				],
# 				'meal':'dessert',
# 				'prep_time':'60',
# 			},
# 			'salad':
# 			{
# 				'ingredients':
# 				[
# 					 'avocado', 'arugula', 'tomatoes'
# 				],
# 				'meal':'lunch',
# 				'prep_time':'15',
# 			}}


if os.path.isfile('cookbook.txt'):
	fd = open("cookbook.txt","r")

	try:
		cookbook = eval(fd.read())
	except:
		fd.close()
		fd = open("cookbook.txt","w")
		cookbook = {}
		fd.write("{}")
		fd.close()

	fd.close()
else:
	fd = open("cookbook.txt","w")
	cookbook = {}
	fd.write("{}")
	fd.close()


def print_recipe(recipe=None, flag=0):

	if recipe == None or recipe == '' or not recipe in cookbook:
		print(f"\nRecipe '{recipe}' doesn't exist\n")
		return

	if flag == 0:
		print(f"Recipe for {recipe}:\n\
Ingredients list: {cookbook[recipe]['ingredients']}\n\
To be eaten for {cookbook[recipe]['meal']}.\n\
Takes {cookbook[recipe]['prep_time']} minutes of cooking.\n")

	if flag == 1:
		print(f"Name : {recipe}\n\
Ingredients : {cookbook[recipe]['ingredients']}\n\
Meal : {cookbook[recipe]['meal']}\n\
Time : {cookbook[recipe]['prep_time']}\n")

def add_recipe():

	recipe = '';
	ingredients = [];
	meal = '';
	prep_time = '';
	answer = '';

	while recipe == '':
		print("Name of the recipe ?")
		recipe = re.sub('\s+',' ',sys.stdin.readline()).strip()

	while ingredients == []:
		print("List of ingredients ? [separated by coma ',']")
		ingredients = list(filter(None, map(str.strip, re.sub('\s+',' ',sys.stdin.readline()).split(','))))

	while meal == '':
		print("Kind of meal ? [lunch, dinner, dessert, etc...]")
		meal = re.sub('\s+',' ',sys.stdin.readline()).strip()

	while prep_time == '' or not prep_time.isnumeric():
		print("Cooking time ? [in minutes]")
		prep_time = re.sub('\s+',' ',sys.stdin.readline()).strip()

	while answer != 'y' and answer != 'n':
		print(f"\nName : {recipe}\n\
Ingredients : {ingredients}\n\
Meal : {meal}\n\
Time : {prep_time}\n\n\
Confirm [y/n]")
		answer = re.sub('\s+',' ',sys.stdin.readline()).strip()

	if answer == 'y':
		cookbook[recipe] = {'ingredients' : ingredients,
							'meal' : meal,
							'prep_time' : prep_time}
		fd = open("cookbook.txt","w")
		fd.write( str(cookbook) )
		fd.close()
		print(f"\n{recipe} added !\n")

def remove_recipe(recipe=None):

	answer = '';

	if recipe == None or recipe == '' or not recipe in cookbook:
		print(f"\nRecipe '{recipe}' doesn't exist\n")
		return
	print_recipe(recipe, 1)
	while answer != 'y' and answer != 'n':
		print(f"Confirm [y/n]")
		answer = re.sub('\s+',' ',sys.stdin.readline()).strip()

	if answer == 'y':
		del cookbook[recipe]
		fd = open("cookbook.txt","w")
		fd.write(str(cookbook))
		fd.close()
		print(f"\n{recipe} deleted !\n")


flag_menu = 1

while True:

	flag_option = 1

	menu = None
	if flag_menu == 1:
		print("Please select an option by typing the corresponding number:\n\
1: Add a recipe\n\
2: Delete a recipe\n\
3: Print a recipe\n\
4: Print the cookbook\n\
5: Quit\n")

	menu = re.sub('\s+',' ',sys.stdin.readline()).strip()

	if menu == '1':
		add_recipe()
		flag_option = 0

	if menu == '2':
		print("Recipe to delete ?")
		recipe = re.sub('\s+',' ',sys.stdin.readline()).strip()
		remove_recipe(recipe)
		flag_option = 0

	if menu == '3':
		print("Recipe to print ?")
		recipe = re.sub('\s+',' ',sys.stdin.readline()).strip()
		print_recipe(recipe, 0)
		flag_option = 0

	if menu == '4':
		for recipe in cookbook:
			print(f"{recipe}")

		print("")
		flag_option = 0

	if menu == '5':
		sys.exit()
	if flag_option == 1:
		print("This option does not exist, please type the corresponding number.\n\
To exit, enter 5.\n")
		flag_menu = 0;
	else:
		flag_menu = 1;

