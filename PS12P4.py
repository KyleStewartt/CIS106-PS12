def displayPlayerStats(namesList, averagesList):
    for name, average in zip(namesList, averagesList):
        print(name, average)
def searchPlayer(name, namesList, averagesList):
    if name in namesList:
        index = namesList.index(name)
        print(name, averagesList[index])
    else:
        print("Name not found")
filename = 'player_data.txt' # Please change this to the path of your file
playerNames = []
battingAverages = []
with open(filename) as file:
    for line in file:
        name, average = line.strip().split()
        playerNames.append(name)
        battingAverages.append(float(average))

displayPlayerStats(playerNames, battingAverages)
while True:
    userInput = input("Enter a last name or type 'quit' to exit: ")
    if userInput.lower() == 'quit':
        break
    searchPlayer(userInput, playerNames, battingAverages)