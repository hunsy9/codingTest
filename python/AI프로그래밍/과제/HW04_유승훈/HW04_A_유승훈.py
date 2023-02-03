class Quizzes:
    def __init__(self,listOfGrades): #생성자
        self._listOfGrades = listOfGrades

    def average(self): #평균구하기
        self._listOfGrades.remove(min(self._listOfGrades)) #최소 요소 지우기
        return sum(self._listOfGrades) / len(self._listOfGrades)

    def __str__(self): #average 메소드 호출
        return ("Quiz average: " + str(self.average()))
def main():
    listOfGrades=[int(input("Enter grade on quiz {}: ".format(i+1))) for i in range(6)] #1-6까지 grade입력
    q=Quizzes(listOfGrades)
    print(q)
main()

#201924515 유승훈

