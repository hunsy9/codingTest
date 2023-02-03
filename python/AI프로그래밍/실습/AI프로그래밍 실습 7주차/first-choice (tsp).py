from problem import TSP

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    # Create an instance of TSP
    p = TSP()
    p.setVariables()  # 'p': [numCities, locations]
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    p.describe()
    p.displaySetting()
    # Report results
    p.report(solution, minimum)
    
def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC


main()
