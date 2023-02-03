from problem import Numeric

def main():
    p=Numeric()
    p.setVariables()
    gredientDescent(p)
    p.describe()
    displaySetting(p)
    p.report()


def gredientDescent(p):
    currentP = p.randomInit()  # 'current' is a list of value , problem에서 랜덤으로 x1x2뽑음
    valueC = p.evaluate(currentP)
    while True:
        nextP = p.takeStep(currentP, valueC)
        valueN = p.evaluate(nextP)
        if valueN >= valueC:
            break
        else:
            currentP = nextP
            valueC = valueN
    p.storeResult(currentP, valueC)


def displaySetting(p):
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print("Update rate:",p.getAlpha())
    print("Increment for calculating derivative", p.getDx())


main()
