import random
import sys


while True:

	print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")

	to_guess = random.randint(1,99)
	# to_guess = 42
	attempt = 0

	# print(to_guess)

	while True:
		
		print("what's your guess between 1 and 99 ?")
		
		if to_guess == 42:
			print("Hint : it's THE answer...")
		
		answer = sys.stdin.readline().strip()
		
		if answer == "exit":
			print("Goodbye!")
			sys.exit()
		
		if not answer.isnumeric() and answer != '':
			print("That's not a number.\n")
		
		if answer.isnumeric() and answer != '':
			attempt +=1
			if int(answer) == to_guess:
				if attempt == 1:
					print(f"\nYOU ONE SHOT ME, I'M SAD :c\n\
You won in only {attempt} attempt!\n") 
				
				else:
					print(f"Congratulations, you've got it!\n\
You won in {attempt} attempts!\n")
				
				break
			else:
				if int(answer) < to_guess:
					print("Too low!")
				if int(answer) > to_guess:
					print("Too high!")
