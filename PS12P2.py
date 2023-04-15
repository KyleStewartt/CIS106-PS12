def displayNamesAndScores(namesList, scoresList):
    for name, score in zip(namesList, scoresList):
        print(name, score)
def displayNamesAndScoresReverse(namesList, scoresList):
    for name, score in zip(reversed(namesList), reversed(scoresList)):
        print(name, score)
lastNames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
examScores = [90, 85, 78, 92, 88, 76, 95, 89, 82, 93]
displayNamesAndScores(lastNames, examScores)
print("\n")
displayNamesAndScoresReverse(lastNames, examScores)