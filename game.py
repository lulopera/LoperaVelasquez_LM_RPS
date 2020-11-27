from random import randint

from gameComponents import gameVars, winLose



while gameVars.player is False:

	
	print("===============*/ RPS /*====================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===================================")
	print("Choose your weapon! or type quit to exit\n")
	
	

	gameVars.player = input("Choose rock, paper or scissors: \n")

	if gameVars.player == "quit":
		print("You chose to quit")
		exit()



	computer = gameVars.choices[randint(0, 2)]

	print("user chose: " + gameVars.player)


	print("AI chose: " + computer)

	if (computer == gameVars.player):
		print("tie")


	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose!")
			
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose!")

		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.player_lives -= 1
			print("you lose!")
			
		else:
			print("you win!")
			gameVars.computer_lives -= 1


	if gameVars.player_lives is 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winLose.winorlose("won")


	print("Player has:", gameVars.player_lives, "lives left")
	print("computer has:", gameVars.computer_lives, "lives left")

	gameVars.player = False
		
