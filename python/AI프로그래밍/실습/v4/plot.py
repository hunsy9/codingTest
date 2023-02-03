
from matplotlib import pyplot as plt

def getPlots(fileName):
    f=open(fileName,"r")
    x=[]
    y=[]
    for idx,line in enumerate(f):
        x.append(idx)
        y.append(eval(line.strip()))
    f.close()
    return x,y

def main():
    plt.figure()
    x1,y1 = getPlots("first.txt")
    x2,y2 = getPlots("anneal.txt")
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.xlabel("Number of Evaluations")
    plt.ylabel("Tour Cost")
    plt.title("Search Performance(TSP-100)")
    plt.show()