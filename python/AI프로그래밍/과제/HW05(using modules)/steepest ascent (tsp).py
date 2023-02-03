from tsp import *


def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': [numCities, locations]
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def steepestAscent(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): # Inversion only
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = inversion(current, i, j)
            count += 1
            neighbors.append(curCopy)
    return neighbors

def bestOf(neighbors, p): ###
    tempArray = []  # tempArray라는 빈 배열 선언
    for i in range(len(neighbors)):  # neighbors의 길이만큼 반복문 실행
        tempArray.append(evaluate(neighbors[i], p))  # neighbors의 첫번째 튜플부터 순서대로 evaluate하여 tempArray에 넣음
    bestValue = min(tempArray)  # bestValue는 tempArray의 최솟값이 됌
    best = neighbors[tempArray.index(bestValue)]  # bestValue를 값으로 가지는 tempArray의
    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

main()
