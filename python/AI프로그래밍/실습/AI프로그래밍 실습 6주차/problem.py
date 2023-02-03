DELTA=0.01
import random

class Problem:
    def __init__(self):
        self._solution = []
        self._value = 0
        self._numEval = 0
    def setVariables(self):
        pass
    def randomInit(self):
        pass
    def evaluate(self):
        pass
    def mutants(self):
        pass
    def randomMutant(self):
        pass
    def describe(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        print()
        print("Mutation step size:", DELTA)

    def getSolution(self):
        return self._solution

    def getValue(self):
        return self._value

    def getNumEval(self):
        return self._numEval

    def setNumEval(self,num=0):
        self._numEval += num

    def storeResult(self,solution,value):
        self._solution = solution
        self._value = value

    def report(self,solution, value):
        pass

class Numeric(Problem):
    def __init__(self):
        super().__init__()
        self._expression = ''
        self._domain = []
        self._delta = 0.01
        #for gradient descent
        self._alpha = 0.01
        self._dx = 10**(-4)

    def getAlpha(self):
        return self._alpha
    def getDx(self):
        return self._dx
    def getDelta(self):
        return self._delta

    def setVariables(self):  ###
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
        varNames, low, up = [], [], []
        for idx, line in enumerate(open(fileName)):  # enumerate로 인덱스와 라인 구분
            if idx == 0:
                self._expression = line  # 첫번째 줄이면 수식
            else:
                data = line.split(",")  # 변수,low,up이므로 split(",")사용
                varNames.append(data[0])
                low.append(float(data[1]))
                up.append(float(data[2]))
        self._domain = [varNames, low, up]

    def randomInit(self):  ###

        low, up = self._domain[1], self._domain[2]  # class의 domain을 가져옴
        init = []
        for i in range(len(low)):
            init.append(random.randint(low[i], up[i]))  # low와 up사이에서 랜덤하게 정수를 선택하여 append
        print(init)  # for test
        return init  # Return a random initial point
        # as a list of values

    def evaluate(self,current):
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        self.setNumEval(1)
        expr = self._expression  # expression 가져옴
        varNames = self._domain[0]  #  [varNames, low, up] -> varnames
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)  # exec으로 변수선언
        return eval(expr)

    def mutants(self,current):
        neighbors = []  # neighbors라는 빈 배열 선언
        for i in range(len(current)):  # current의 길이만큼 실행
            neighbors.append(self.mutate(current, i, self.getDelta()))  # +delta만큼 이동한 값을 neighbors에 추가
        for i in range(len(current)):
            neighbors.append(self.mutate(current, i, -self.getDelta()))  # -delta만큼 이동한 값을 neighbors에 추가
        return neighbors  # Return a set of successors

    def randomMutant(self,current):  ### randomMutant를 호출할때마다 i와 d를 랜덤으로 만들어서 mutate함수의 파라미터로 넣어야함
        i = random.choice(range(len(current)))  # current의 len을 구해서 배열로 만든다 ex)변수가 5개라면 i는 [0,1,2,3,4]중에 랜덤으로 고르게 함
        d = random.choice([self.getDelta(), -self.getDelta()])  # d와 같은 경우에도 델타가 음의 방향 양의 방향 둘중 하나로 움직여야 하므로 choice 메서드로 랜덤으로 고르게 함
        return self.mutate(current, i, d)  # Return a random successor


    def mutate(self,current, i, d):  ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        domain = self._domain  # [VarNames, low, up]
        l = domain[1][i]  # Lower bound of i-th
        u = domain[2][i]  # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:  # 범위 제한조건
            curCopy[i] += d
        return curCopy

    def bestOf(self,neighbors, p):  ###
        tempArray = []  # tempArray라는 빈 배열 선언
        for i in range(len(neighbors)):  # neighbors의 길이만큼 반복문 실행
            tempArray.append(p.evaluate(neighbors[i]))  # neighbors의 첫번째 튜플부터 순서대로 evaluate하여 tempArray에 넣음
        bestValue = min(tempArray)  # bestValue는 tempArray의 최솟값이 됌
        best = neighbors[tempArray.index(bestValue)]  # bestValue를 값으로 가지는 tempArray의
        return best, bestValue

    def takeStep(self,x,v):
        count=v
        temp=[] #[[x1+dx,x2,x3],[x1,x2+dx,x3],[x1+dx,x2,x3]] ->[g1,g2,g3] ->[x1-Ag1,--- ,--- ]
        for i in range(len(x)):
            tarr = x[:]
            tarr[i]+=self.getDx()
            temp.append(tarr)
        print(temp)
        a=self.gradient(temp,v)
        for i in range(len(temp)):
            temp[i]=x[i]-(self.getAlpha() * a[i])
        print(temp)
        for i in range(len(temp)):
            if self.isLegal(temp[i]):
                if temp[i] < count:
                    count = temp[i]
        return count
    def gradient(self,x,v):
        gradient=[]
        for i in range(len(x)):
            gradient.append((self.evaluate(x[i])-v)/self.getDx())
        print(gradient)
        return gradient

    def isLegal(self,x):
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            if (low[i] > x) or (x>up[i]):
                return False
        return True


    def describe(self):
        print()
        print("Objective function:")
        print(self._expression)  # Expression
        print("Search space:")
        varNames = self._domain[0]  # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def displaySetting(self,p):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        print()
        print("Mutation step size:", p.getDelta())

    def report(self,solution, value):
        print()
        print("Solution found:")
        print(tuple([[round(value, 3) for value in solution]]))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(value))
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))

class TSP(Problem):
    def __init__(self):
        super().__init__()
        self._locations = []
        self._numCities = 0
        self._distanceTable = []

    def setVariables(self):
        ## Read in a TSP (# of cities, locatioins) from a file.
        ## Then, create a problem instance and return it.
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')
        # First line is number of cities
        self._numCities = int(infile.readline())
        self._locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            self._locations.append(eval(line))  # Make a tuple and append
            line = infile.readline()
        infile.close()
        self._distanceTable = self.calcDistanceTable(self._numCities, self._locations)

    def calcDistanceTable(self,numCities, locations):  ###

        table = []

        for i in range(numCities):
            row = []

            for j in range(len(locations)):
                dx = locations[i][0] - locations[j][0]
                dy = locations[i][1] - locations[j][1]
                d = (dx ** 2 + dy ** 2) ** (1 / 2)
                row.append(d)

            table.append(row)

        return table  # A symmetric matrix of pairwise distances

    def randomInit(self):  # Return a random initial tour
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self,current):  ###
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        self.setNumEval(1)
        table = self._distanceTable
        goRoute = 0
        for i in range(len(current) - 1):
            goRoute += table[current[i + 1]][current[i]]
        backRoute = table[current[-1]][current[0]]

        cost = goRoute + backRoute
        return cost

    def randomMutant(self,current):  # Apply inversion
        while True:
            i, j = sorted([random.randrange(self._numCities)
                           for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def mutants(self,current):  # Apply inversion
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        # print(neighbors)
        return neighbors

    def inversion(self,current, i, j):  ## Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def bestOf(self,neighbors, p):  ###
        tempArray = []
        for i in range(len(neighbors)):
            tempArray.append(p.evaluate(neighbors[i]))
        bestValue = min(tempArray)
        best = neighbors[tempArray.index(bestValue)]
        return best, bestValue

    def describe(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end='')
            if i % 5 == 4:
                print()

    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")

    def tenPerRow(self,solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()

    def report(self,solution, minimum):
        print()
        print("Best order of visits:")
        self.tenPerRow(solution)  # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(minimum)))
        print()
        print("Total number of evaluations: {0:,}".format(self.getNumEval()))

# 서론:목적
# 결론 : 이걸통해서 뭘알수있었다.


