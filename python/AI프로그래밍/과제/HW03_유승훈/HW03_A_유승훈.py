import os.path
def readSetFromFile(): # implement functions
    mySet = set() #새로운 set생성
    if os.path.isfile('./Names.txt'): #Names.txt라는 파일이 존재하면
        infile = open('./Names.txt', 'r') #파일을 열어서
        for line in infile: #파일안의 1줄씩 꺼낸다.
            mySet.add(line.rstrip()) #set에 각 줄의 우공백을 제거한 것을 삽입
        infile.close()  # 열어둔 파일 닫기

    else: #Names.txt 존재하지 않는다면
        print("Names.txt does not exist.") #출력문 출력
        print("Terminate program.")
        exit(0) #프로그램 종료
    return mySet

def inputName(): #넣을 이름 받는 함수
    name = input("Enter a first name to be included: ")
    print("{} is added in Names.txt".format(name))
    return name

def insertSet(mySet, name): #set과 name 을 받아서 set에 name 추가하고, 알파벳순으로 정렬하고 set return 한다.
    mySet.add(name)
    mySet = sorted(mySet)
    return mySet

def writeToFile(modifiedSet):
    os.remove('./Names.txt') #원래 있던 Names.txt 삭제한다.
    outfile = open('Names.txt', 'w') #Names.txt를 쓰기전용으로 생성
    for line in list(modifiedSet): #set에 있는 라인들을 읽어서 txt파일 생성
        outfile.write(line+"\n")
    outfile.close()

def main():
    mySet = readSetFromFile()
    name = inputName()
    modifiedSet = insertSet(mySet, name)
    writeToFile(modifiedSet)

main()