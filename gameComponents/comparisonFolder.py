from gameComponents import gameVars, winLose

def comparison(status):

	if status == "tie":
		pre_message "It's a tie"

	elif (computer == "rock"):
		if (gameVars.player == "paper"):
			gameVars.computer_lives -= 1
			print("you", status)
			
		else:
			print("you lose!")
			gameVars.player_lives -= 1


	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.computer_lives -= 1
			print("you", status)

		else:
			print("you lose!")
			gameVars.player_lives -= 1


	elif (computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.computer_lives -= 1
			print("you", status)
			
		else:
			print("you lose!")
			gameVars.computer_lives -= 1