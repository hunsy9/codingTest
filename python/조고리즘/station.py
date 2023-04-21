import math
import numpy as np
def getDistanceFromDotToLine(startPos, endPos , Dot):
    vec1 = [ai - bi for ai, bi in zip(startPos, Dot)]
    vec2 = [ci - di for ci, di in zip(endPos, Dot)]
    area = getLengthOfLine(np.cross(vec1,vec2))
    print("area: ",area)
    AB = getDistance(startPos,endPos)
    distance = area / AB
    print("distance: ",distance)
    return distance
def getDistance(pos1, pos2):
    return math.sqrt(sum([(pos1i-pos2i)**2 for pos1i, pos2i in zip(pos1,pos2)]))
def getLengthOfLine(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
def innerProduct(vec1,vec2):
    return sum([vec1i*vec2i for vec1i, vec2i in zip(vec1,vec2)])
def getAngle(vec1, vec2):
    return abs(np.dot(vec1,vec2)) / (getLengthOfLine(vec1) * getLengthOfLine(vec2))
def getLineEquation(pos, directionVector):
    return [[i,j] for i, j in zip(pos, directionVector)]
def isMeet(abEquation,cdEquation):
    A=np.array([[1,1],[2,4]])
    B=np.array([cdEquation[0][0] - abEquation[0][0]],[cdEquation[1][0] - abEquation[1][0]],[cdEquation[2][0] - abEquation[2][0]])
    print(B)
    try:
        np.linalg.solve(A, B)
        return True
    except:
        return False
def main():
    aPos = np.array(list(map(float, input().split())))
    bPos = np.array(list(map(float, input().split())))
    cPos = np.array(list(map(float, input().split())))
    dPos = np.array(list(map(float, input().split())))

    vec1 = [ai - bi for ai, bi in zip(aPos, bPos)]
    vec2 = [ci - di for ci, di in zip(cPos, dPos)]

    print(vec1,vec2)

    abEquation = getLineEquation(aPos, vec1)
    cdEquation = getLineEquation(cPos, vec2)

    print("Equation: ", abEquation,cdEquation)

    angle = getAngle(vec1, vec2)

    # if isMeet(abEquation, cdEquation):
    #     print("교점을 가짐")
    #     print(0)
    #     return
    if round(angle) == 1:
        print("평행")
        print(getDistanceFromDotToLine(aPos,bPos,cPos))
        return

main()








