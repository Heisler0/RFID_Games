# With this program the player can use their cards to select a game to play.

import tarot, nowammies, rps
from time import sleep

games = {'Tarot' : tarot, 'No Wammies' : nowammies, 'RPS' : rps}
added = {}

help_text = "Type \'list\' to diplay the available games.\nType \'add\' to register one of your cards with a game.\nType \'added\' to see what games you have registered and are ready to play.\nType \'quit\' to exit Game Room.\n"

print("Welcome to the Python Game Room")
sleep(1)
print("To begin, choose a game from the list and add it to one of your cards.")
sleep(1)
print("When you have added a card you can scan it to play.")
sleep(1)
print(help_text)
print("Type \'help\' at anytime to display this text again.\n")
sleep(2)

def list_games():
	print('Games Available:')
	for key in games:
		print(key)
	print("")

def list_added():
	print('Games Added:')
	for key in added:
		print(key)
	print("")


main = True

while main:
	value = raw_input(" --> ")
	
	if(value == 'list'):
	#print list of games
		list_games()
	elif(value == 'added'):
	#print games registered to a game card
		list_added()
	elif(value == 'help'):
	#print the help text
		print(help_text)
	elif(value == 'add'):
	#add a game to a game card
		add = True
		if(len(games) == 0):
			add = False
			print("There are no more games to add.\n")
		while add:
			list_games()
			game = raw_input("Enter the game's name as it appears in the list or type \'exit\'\n --> ")
			if(game == 'exit'):
				add = False
			else:
				if(games.has_key(game)):
					card = raw_input("Scan a game card: ")
					if(added.has_key(card)):
						print("That card has already been used.")
					else:
						#add game to added dictionary
						added[card] = games[game]
						#remove game from game dictionary
						del games[game]
						print("Card " + card + " has been linked to " + game + ".\n")
						#exit add loop
						add = False
				else:
					print("That game does not exist\n")
	elif(added.has_key(value)):
	#play the game
		game = added[value]
		print('\n')
		game.main()
	elif(value == 'quit'):
		main = False
	else:
		print("Input was invalid")
		
