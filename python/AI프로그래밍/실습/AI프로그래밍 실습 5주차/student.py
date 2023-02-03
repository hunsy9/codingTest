class Student:
    def __init__(self, name="", semester=1):
        self._name = name
        self._semester = semester

    def setName(self, name):
        self._name = name
    def setSemester(self, semester):
        self._semester = semester
    def getName(self):
        return self._name
    def __str__(self):
        return self.getCourse()

class UGStudent(Student):
    def getCourse(self):
        return 'B.S'
    def getYear(self):
        year = self.getYear()
        if year == 1:
            return 'Freshman'
        elif year == 2:
            return 'Sophomore'
        elif year == 3:
            return 'Junior'
        else:
            return 'Senior'

    def __str__(self):
        return '### 3 ###'
class GStudent(Student):
    def __init__(self, name="", semester=1, course='M.S'):
        '### 4 ###'
        self._course = '### 5 ###'
    def setCourse(self, course):
        self._course = course
    def getCourse(self):
        return self._course

def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")
        semester = int(input('Current number of semesters(Positive Integer): '))
        category = input("Enter category (UG or G): ")
        if category.upper() == 'UG':
            st=UGStudent[name,semester]
        else:
            question = input("Is " + name + " the Master course (Y/N)? ")
            if question.upper() == 'Y':
                course = 'M.S'
            else:
                course = 'Ph.D'
            st = GStudent[name, semester,course]
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents

def displayResults(listOfStudents):
    print("\nNAME\tCourse\tYear")
    listOfStudents = 0
    listOfStudents.sort(key = lambda x : x.getCourse() )
    for student in listOfStudents:
        print(student)
        if isinstance(student,GStudent):
            numberOfGstudents += 1
    print("Number of Undergraduate students:", len(listOfStudents))
    print("Number of Graduate students:", numberOfGstudents)
def main():
    listOfStudents = obtainListOfStudents()
    displayResults(listOfStudents)
main()

#201924515 유승훈



