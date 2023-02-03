
class Rectangle:
    def __init__(self, origin_x=0, origin_y=0, width=1, height=1):
        self._origin_x, self._origin_y = origin_x, origin_y
        self._width, self._height = width, height

    def setOrigin(self, origin_x, origin_y):
        self._origin_x, self._origin_y = origin_x, origin_y

    def calcPoint(self, x_move, y_move):
        point_x, point_y = self._origin_x, self._origin_y
        if x_move:
            point_x += self._width
        if y_move:
            point_y += self._height
        return point_x, point_y
    def getPoints(self):
        bool_list = [(False,False), (True,False), (True,True), (False, True)]
        point_list = [self.calcPoint(x,y) for x, y in bool_list]
        return point_list
    def area(self):
        return self._width * self._height

    def __str__(self):
        points = self.getPoints()
        return ("Point 1: "+str(points[0])+"\nPoint 2: "+str(points[1])+"\nPoint 3: "+str(points[2])+"\nPoint 4: "+str(points[3]))

#201924515 유승훈