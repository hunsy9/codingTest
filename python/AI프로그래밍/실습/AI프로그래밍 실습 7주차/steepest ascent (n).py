# from numeric import *
from problem import Numeric


def main():

    p = Numeric()
    p.setVariables()
    solution, minimum = steepestAscent(p)
    p.describe()
    p.displaySetting(p)
    p.report(solution,minimum)
    # Create an instance of numerical optimization problem
    # p = createProblem()   # 'p': [expr, domain]

    
def steepestAscent(p):
    currentP = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(currentP)
    while True:
        neighbors = p.mutants(currentP) #인접 값들 구하기
        successor, valueS = p.bestOf(neighbors, p) #인접한 값들 중에 최선의 값 구하기
        if valueS >= valueC:
            break
        else:
            currentP = successor
            valueC = valueS
    return currentP, valueC



main()
