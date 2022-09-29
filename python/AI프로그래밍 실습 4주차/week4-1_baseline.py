def main():
    statesList = createListFromFile("States.txt")
    createSortedFile(statesList, "StatesCount.txt")

def createListFromFile(fileName):
    infile = open(fileName, '### 1 ###')
    desiredList = ['### 2 ###' for line in infile]
    infile.close()
    return desiredList

def createSortedFile(listName, fileName):
    listName.sort(key=lambda k: '### 3 ###', '### 4 ###')
    for i in '### 5 ###':
        listName[i] = listName[i] + "\n"
    outfile = open(fileName, '### 6 ###')
    outfile.writelines(listName)
    outfile.close()

main()