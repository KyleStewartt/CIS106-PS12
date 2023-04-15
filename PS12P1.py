def displayNames(namesList):
    for name in namesList:
        print(name)

def displayNamesReverse(namesList):
    for name in reversed(namesList):
        print(name)
lastNames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
displayNames(lastNames)
print("\n")
displayNamesReverse(lastNames)