def main():
    statesList = createListFromFile("States.txt")
    createSortedFile(statesList, "StatesCount.txt")

def createListFromFile(fileName):
    infile = open(fileName, 'r')
    desiredList = [ line.rstrip() for line in infile]
    infile.close()
    return desiredList

def createSortedFile(listName, fileName):
    listName.sort(key=lambda k: listName.count(k), reverse=True)
    for i in len(listName):
        listName[i] = listName[i] + "\n"
    outfile = open(fileName, 'w')
    outfile.writelines(listName)
    outfile.close()

main()

'201924515 유승훈'