from random import randint

from gameComponents import gameVars, winLose, comparisonFolder



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
		comparisonFolder.comparison("tie")

	elif computer == gameVars.computer_lives - 1:
		comparisonFolder.comparison("win")

	elif computer == gameVars.player_lives - 1:
		 comparisonFolder.comparison("lose")



	if gameVars.computer_lives is 0:
		winLose.winorlose("won")


	elif gameVars.player_lives is 0:
		winLose.winorlose("lost")

	print("Player has:", gameVars.player_lives, "lives left")
	print("computer has:", gameVars.computer_lives, "lives left")

	gameVars.player = False
		
