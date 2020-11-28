from gameComponents import gameVars


def winorlose(status):
	

	if status == "won":
		pre_message = "You won! You are the greatest winner in the world! "
	
	if status == "lost":
		pre_message = "You failed, loser! "

	print(pre_message + "Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		
		print("You chose to quit. Best of luck next time!")
		exit()

	elif choice == "Y" or choice == "y":

		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
	
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N")


	if choice == "Y" or choice == "y":

		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False

	else:
		print("You chose to quit. Best of luck next time!")
		exit()