from problem import Numeric

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    p = Numeric()
    p.setVariables()
    firstChoice(p)
    p.describe()
    p.displaySetting(p)
    p.report()
    
def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of values
    valueC = p.evaluate(current) #랜덤하게 나온 값 evaluate
    i = 0
    while i < LIMIT_STUCK: #한계횟수까지 반복
        successor = p.randomMutant(current) #랜덤하게 mutant를 뽑음
        valueS = p.evaluate(successor) #mutant로 값 evaluate
        if valueS < valueC: #새로 뽑은 것이 오차가 적다면??
            current = successor #새로 뽑은 mutant로 초기화
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    p.storeResult(current, valueC)


main()
