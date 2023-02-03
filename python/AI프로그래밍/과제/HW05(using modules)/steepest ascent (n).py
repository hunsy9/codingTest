from numeric import *


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': [expr, domain]
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p) #인접 값들 구하기
        successor, valueS = bestOf(neighbors, p) #인접한 값들 중에 최선의 값 구하기
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): ###
    neighbors=[] #neighbors라는 빈 배열 선언
    for i in range(len(current)): #current의 길이만큼 실행
        neighbors.append(mutate(current, i, DELTA, p)) #+delta만큼 이동한 값을 neighbors에 추가
    for i in range(len(current)):
        neighbors.append(mutate(current, i, -DELTA, p))#-delta만큼 이동한 값을 neighbors에 추가
    return neighbors     # Return a set of successors

def bestOf(neighbors, p): ###
    tempArray = [] #tempArray라는 빈 배열 선언
    for i in range(len(neighbors)): #neighbors의 길이만큼 반복문 실행
        tempArray.append(evaluate(neighbors[i],p)) #neighbors의 첫번째 튜플부터 순서대로 evaluate하여 tempArray에 넣음
    bestValue = min(tempArray) #bestValue는 tempArray의 최솟값이 됌
    best = neighbors[tempArray.index(bestValue)] #bestValue를 값으로 가지는 tempArray의
    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
