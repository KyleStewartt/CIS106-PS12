def findHighestAndLowest(namesList, scoresList):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0
    for i, score in enumerate(scoresList):
        if score > high_var:
            high_var = score
            high_index = i
        if score < low_var:
            low_var = score
            low_index = i
    print("Highest:", namesList[high_index], high_var)
    print("Lowest:", namesList[low_index], low_var)
filename = 'data.txt' # Please change this to the path of your file
lastNames = []
examScores = []
with open(filename) as file:
    for line in file:
        name, score = line.strip().split()
        lastNames.append(name)
        examScores.append(int(score))
findHighestAndLowest(lastNames, examScores)