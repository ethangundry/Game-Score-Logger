#TODO Make a system that keeps track of games that each person plays, and how many wins or losses they have, and to who.
#TODO Track the date and location of the games played.
#TODO Optionally make it track how much a person won or lost by.

from pick import pick

# User wants to track one of the games they just played. They start the program.
#TODO Add the option to choose to either add a new game or to track a game already put into the system. 
game = input("Hello! Please input the name of the game you want to track.")
while game == "":
    game = input("That isn't a valid name. Please input the name of the game you want to track.")
game = game.casefold()

fileRef = open("gamesLog.txt",'r')
gameList = fileRef.readlines()
isPresent = 0
for item in gameList:
    if item == game:
        isPresent = 1
        break
print(str(gameList))
if isPresent == 0:
    gameList = str(gameList)+game+"\n"
    fileRef = open("gamesLog.txt", 'w')
    fileRef.write(gameList)


# User then puts in the game and wants to write who they were playing it with.
playerList = []

# User enters the amount of players they were playing with.
playerAmount = input("Please input an amount of players as an integer.")
while playerAmount.isdigit() != True:
    playerAmount = input("That isn't an integer. Please input an amount of players as an integer.")
if int(playerAmount) >20:
    playerAmount = input("Please put in a smaller number of players.")

# User enters the names of each player.
for i in range(0, int(playerAmount)):
    player = input("Please input the name of the next player.")
    playerList.append(player)
print(playerList)

# User chooses who won the game. No cheating!
choiceTitle = "Please choose who won the game."
options = playerList
winner, index = pick(options, choiceTitle)
print(winner,"won the game. Congratulations",winner,"!")

fileRef.close()



