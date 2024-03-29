import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


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
    for idx, line in enumerate(open(fileName)): #enumerate로 인덱스와 라인 구분
        if idx==0:
            expression = line #첫번째 줄이면 수식
        else:
            data = line.split(",") #변수,low,up이므로 split(",")사용
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
    domain = [varNames, low, up]
    print(domain)           # for test
    return expression, domain

def randomInit(p): ###

    low, up = p[1][1], p[1][2]  # p[1]이 domain을 뜻하므로 low는 p[1][1], up은 p[1][2]
    init = []
    for i in range(len(low)):
        init.append(random.randint(low[i], up[i]))  # low와 up사이에서 랜덤하게 정수를 선택하여 append
    print(init)  # for test
    return init  # Return a random initial point
    # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain: [varNames, low, up]
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment) #exec으로 변수선언
    return eval(expr)

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u: #범위 제한조건
        curCopy[i] += d
    return curCopy

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

