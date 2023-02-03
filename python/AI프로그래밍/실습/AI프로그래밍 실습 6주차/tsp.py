import random
import math

NumEval = 0    # Total number of evaluations


def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    fileName = input("Enter the file name of a TSP: ")
    infile = open(fileName, 'r')
    # First line is number of cities
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()  # The rest of the lines are locations
    while line != '':
        locations.append(eval(line)) # Make a tuple and append
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table


def calcDistanceTable(numCities, locations):  ###

    table = []

    for i in range(numCities):
        row = []

        for j in range(len(locations)):
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]
            d = (dx ** 2 + dy ** 2) ** (1 / 2)
            row.append(d)

        table.append(row)

    print(table)  # for test
    return table  # A symmetric matrix of pairwise distances

def randomInit(p):   # Return a random initial tour
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init

def evaluate(current, p): ###
    ## Calculate the tour cost of 'current'
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids
    global NumEval #NumEval 을 글로벌로 선언
    NumEval +=1 #evaluate를 실행할때마다 1씩 증가
    table=p[2] #p에서 table을 빼옴
    goRoute=0 #randomInit을 통해 주어진 랜덤의 경로에서 시작부터 끝까지 가는 거리를 계산
    for i in range(len(current)-1):
        goRoute+=table[current[i+1]][current[i]] #goRoute에 table에서 값을 가져와 더함
    backRoute=table[current[-1]][current[0]] #끝에서 시작까지 가는 거리 table에서 받아옴

    cost = goRoute + backRoute #오고 가는 거리를 모두 더함
    return cost

def inversion(current, i, j):  ## Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

