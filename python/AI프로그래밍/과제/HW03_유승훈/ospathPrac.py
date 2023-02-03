import os.path

def readSetFromFile(): # implement functions
    mySet = set()
    if os.path.isfile('./Names.txt'):
        infile = open('./Names.txt', 'r')
        for line in infile:
            mySet.add(line.rstrip())
    else:
        print("Names.txt does not exist.")
        print("Terminate program.")
        exit(0)
    infile.close()
    return mySet


def inputName():
    name=input("Enter a first name to be included: ")
    return name

def insertSet(mySet, name):
    mySet.add(name)
    mySet = sorted(mySet)
    return mySet

mySet=readSetFromFile()
name=inputName()
print(insertSet(mySet,name))