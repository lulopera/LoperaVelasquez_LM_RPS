from gameComponents import gameVars


def winorlose(status):
	#print("called winorlose", status)

	if status == "won":
		pre_message = "You are the greatest winner in the world! "
	else:
		pre_message = "You failed, loser! "

	print(pre_message + "Would you like to play again?")
	
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":

		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("You chose to quit. Best of luck next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		# this is generating a bug -> need to fix this check
		choice = input("Y / N")