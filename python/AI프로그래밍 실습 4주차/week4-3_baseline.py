import pickle
def main():
    nations = getDictionary("UNdict.dat")
    print("Enter an area", end=' ')
    area = input("in positive integers: ")
    continentDict = constructAreaNations(nations,area)
    displaySortedResults(continentDict)

def getDictionary(fileName):
    infile = open(fileName,'rb')
    countries = pickle.load(infile)
    infile.close()
    return countries

def constructAreaNations(nations, area):
    areaDict = { '### 1 ###' for nation in nations if '### 2 ###' >= '### 3 ###' }
    return areaDict

def displaySortedResults(dictionaryName):
    continentList = sorted(dictionaryName.items(), key=lambda k: '### 4 ###', reverse=True)
    for k in continentList:
        print(" {0:s}: {1:,}".format(k[0], '### 5 ###'))

main()
'2022123456 홍길동'