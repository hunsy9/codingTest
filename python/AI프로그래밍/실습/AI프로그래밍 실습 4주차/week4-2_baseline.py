def main():
    vicePresSet = createSetFromFile("VPres.txt")
    presSet = createSetFromFile("USPres.txt")
    onlyPresOrVPresSet = createPresOrVPres(vicePresSet,presSet)
    onlyPres = createConditionCheck(onlyPresOrVPresSet, presSet)
    onlyVPres = createConditionCheck(onlyPresOrVPresSet, vicePresSet)
    writeNamesToFile(onlyPres, "onlyVPres.txt")
    writeNamesToFile(onlyVPres, "onlyPres.txt")
def createSetFromFile(fileName):
    infile = open(fileName, 'r')
    namesSet = {name for name in infile}
    infile.close()
    return namesSet

def createPresOrVPres(set1, set2):
    return (set1 | set2) - (set1 & set2)

def createConditionCheck(querySet, baseSet):
    checkSet = [ querySet for querySet in baseSet ]
    return checkSet

def writeNamesToFile(setName, fileName):
    outfile = open(fileName, 'w')
    outfile.writelines(setName)
    outfile.close()
main()

'201924515 유승훈'