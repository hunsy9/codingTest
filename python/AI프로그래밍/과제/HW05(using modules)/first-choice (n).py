from numeric import *

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': [expr, domain]
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p) #랜덤하게 나온 값 evaluate
    i = 0
    while i < LIMIT_STUCK: #한계횟수까지 반복
        successor = randomMutant(current, p) #랜덤하게 mutant를 뽑음
        valueS = evaluate(successor, p) #mutant로 값 evaluate
        if valueS < valueC: #새로 뽑은 것이 오차가 적다면??
            current = successor #새로 뽑은 mutant로 초기화
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomMutant(current, p): ### randomMutant를 호출할때마다 i와 d를 랜덤으로 만들어서 mutate함수의 파라미터로 넣어야함
    i=random.choice(range(len(current))) #current의 len을 구해서 배열로 만든다 ex)변수가 5개라면 i는 [0,1,2,3,4]중에 랜덤으로 고르게 함
    d=random.choice([DELTA,-DELTA]) #d와 같은 경우에도 델타가 음의 방향 양의 방향 둘중 하나로 움직여야 하므로 choice 메서드로 랜덤으로 고르게 함
    return mutate(current, i, d, p) # Return a random successor

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
