def populateDictionary(): # implement functions
    newdict = dict() #dictionary 선언
    infile = open('./Units.txt','r') #읽기전용으로 Units.txt를 연다
    for line in infile: #Units.txt에 있는 line들을 한줄씩읽는다.
        key,value = line.rstrip().split(",") #우공백 없애고 ','기준으로 split하여 key,value에 집어넣는다.
        newdict[key] = float(value) #value를 float로 형변환하여 dictinary를 만든다.
    return newdict

def getInput(): #세가지 인자를 받는다.
    orig = input("Unit to convert from: ")
    dest = input("Unit to convert to: ")
    length = float(input("Enter length in {}s: ".format(orig)))

    return orig, dest, length

def main():
    feet = populateDictionary() #파일로 feet라는 dictionary 생성
    orig, dest, length = getInput() #getInput함수로부터 세개 인자 받아옴
    ans = length * feet[orig] / feet[dest] #계산
    print("Length in {0}: {1:,.4f}".format(dest, ans)) #출력

main()