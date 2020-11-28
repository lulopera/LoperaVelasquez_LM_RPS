from random import randint

from gameComponents import gameVars, winLose, comparisonFolder



while gameVars.player is False:

	
	print("*©•©*©•©*©•©*©*©•©*©•/ Rock|Paper|Scissors /*©•©*©•©*©•©*©•©*©•©\n")

	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives, "\n")

	print("                    *©•©*©•©*©•©*©•©*©*©*©*\n")

	print("                             ~~~~~ ")
	print("                           <( ©•© )> ")
	print("                               -   \n")

	print("Choose your weapon! or type quit to exit\n")
	
	
	gameVars.player = input("Choose rock, paper or scissors: \n")

	if gameVars.player == "quit":
		print("You chose to quit")
		exit()


	computer = gameVars.choices[randint(0, 2)]


	print("user chose: " + gameVars.player)


	print("AI chose: " + computer)


	if gameVars.player == computer:
		comparisonFolder.comparison("tie")

	elif gameVars.player == gameVars.player_lives - 1:
		comparisonFolder.comparison("you lose")

	else:
		comparisonFolder.comparison("you win")
	


	if gameVars.computer_lives == 0:
		winLose.winorlose("won")


	elif gameVars.player_lives == 0:
		winLose.winorlose("lost")

	print("Player has:", gameVars.player_lives, "lives left")
	print("computer has:", gameVars.computer_lives, "lives left")

	gameVars.player = False
		
