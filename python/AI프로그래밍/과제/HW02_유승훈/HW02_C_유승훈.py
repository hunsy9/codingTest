a=input("Input list = ") #list입력받음
newList=list(map(int,a.replace(" ","")[1:-1].split(","))) #받은 list형태는 사실은 string으로 받았으므로 list형태로 변환해준다
newList.sort() #list 오름차순 정렬
EncodedList=[] #Encoded리스트 초기화
for i in range(10): #0~9까지 반복
    babyList = []
    count = 0
    for j in newList: #for문으로 newList에 i가 몇개 들어있는지 판별 후 count변수로 셈
        if i==j:
            count += 1
    babyList.append(i)
    babyList.append(count)
    EncodedList.append(babyList)
print("Encoded List = {}".format(EncodedList))
