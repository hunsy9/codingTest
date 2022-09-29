def main():
    vicePresSet = createSetFromFile("VPres.txt")
    presSet = createSetFromFile("USPres.txt")
    onlyPresOrVPresSet = createPresOrVPres(vicePresSet,presSet)
    onlyPres = createConditionCheck(onlyPresOrVPresSet, '### 1 ###')
    onlyVPres = createConditionCheck(onlyPresOrVPresSet, '### 2 ###')
    writeNamesToFile(onlyPres, "onlyVPres.txt")
    writeNamesToFile(onlyVPres, "onlyPres.txt")


def createSetFromFile(fileName):
    infile = open(fileName, 'r')
    namesSet = {name for name in infile}
    infile.close()
    return namesSet

def createPresOrVPres(set1, set2):
    return '### 3 ###'

def createConditionCheck(querySet, baseSet):
    checkSet = [ '### 4 ###' ]
    return checkSet

def writeNamesToFile(setName, fileName):
    outfile = open(fileName, 'w')
    outfile.writelines(setName)
    outfile.close()

main()