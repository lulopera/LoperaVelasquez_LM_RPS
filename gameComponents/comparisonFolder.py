from random import randint

from gameComponents import gameVars, winLose

def comparison(player):

	computer = gameVars.choices[randint(0, 2)]

	if gameVars.player == computer:
		print("tie")

	elif (computer == "rock"):
		if (gameVars.player == "paper"):
			gameVars.computer_lives -= 1
			print("you win")
			
		else:
			print("you lose!")
			gameVars.player_lives -= 1


	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.computer_lives -= 1
			print("you win")

		else:
			print("you lose!")
			gameVars.player_lives -= 1


	elif (computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.computer_lives -= 1
			print("you win")
			
		else:
			print("you lose!")
			gameVars.computer_lives -= 1