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
    areaDict = { nation for nation in nations if nations[nation]['area'] >= int(area) }
    return areaDict

def displaySortedResults(dictionaryName):
    continentList = sorted(dictionaryName.items(), key=lambda k: len(dictionaryName[0]), reverse=True)
    for k in continentList:
        print(" {0:s}: {1:,}".format(k[0], k[1]['area']))

main()

'201924515 유승훈'