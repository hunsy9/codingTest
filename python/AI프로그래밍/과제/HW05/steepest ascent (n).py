import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def createProblem(): ###
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    fileName = input("Enter the file name of a function:")
    ## Read in an expression and its domain from a file.
    varNames,low,up = [],[],[]
    for idx, line in enumerate(open(fileName)):
        if idx==0:
            expression = line
        else:
            data = line.split(",")
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
    domain = [varNames, low, up]
    #print(domain)           # for test
    return expression, domain


def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of value , problem에서 랜덤으로 x1x2뽑음
    valueC = evaluate(current, p) #주어진 식에 랜덤으로 뽑아진 x1x2를 넣어서 결과값 구함
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC


def randomInit(p): ###

    low, up = p[1][1],p[1][2]
    init = []
    for i in range(len(low)):
        init.append(random.randint(low[i],up[i]))
    #print(init)        #for test
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression->x1**2+x2**2
    varNames = p[1][0]  # p[1] is domain ->[x1,x2]
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def mutants(current, p): ###
    neighbors=[]
    for i in range(len(current)):
        neighbors.append(mutate(current,i,DELTA,p))
    for i in range(len(current)):
        neighbors.append(mutate(current, i, -DELTA, p))
    #print(neighbors)
    return neighbors     # Return a set of successors


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:] #current는 (-3,-1)
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): ###
    tempArray = []
    for i in range(len(neighbors)):
        tempArray.append(evaluate(neighbors[i],p))
    bestValue = min(tempArray)
    best = neighbors[tempArray.index(bestValue)]
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
