from problem import TSP


def main():
    # Create an instance of TSP
    p=TSP()
    p.setVariables()    # 'p': [numCities, locations]
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    p.describe()
    p.displaySetting()
    # Report results
    p.report(solution, minimum)
    
def steepestAscent(p):
    current = p.randomInit()  # 'current' is a list of city ids
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        (successor, valueS) = p.bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC
main()
