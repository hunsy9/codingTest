class Rectangle:
    def __init__(self,width=1,height=1):
        self._width=width
        self._height=height
    def setWidth(self,width):
        self._width = width
    def setHeight(self,height):
        self._height = height
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def area(self):
        return str(self._width * self._height)
    def perimeter(self):
        return 2*(self._width+self._height)
    def __str__(self):
        return ("Width: "+ str(self._width) + "\nHeight: " +str(self._height))

def main():
    r=Rectangle()
    r.setWidth(5)
    r.setHeight(4)
    print("가로는 : ",r.getWidth() )
    print("높이는 : ",r.getHeight())
    print( r.__str__())
main()