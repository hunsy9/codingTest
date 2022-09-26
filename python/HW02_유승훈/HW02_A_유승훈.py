median=0 #median을 초기값 설정을 해준다
initial=input("Enter a number as list : ") #list를 입력받는다.
removedList=list(map(int,initial.replace(" ","")[1:-1].split(","))) #받은 list형태는 사실은 string으로 받았으므로 list형태로 변환해준다
removedList.sort() #list를 정렬한다.
length=len(removedList)
if length%2==0: #length가 짝수이면
    median=(removedList[(int(length/2))-1]+removedList[int((length/2))])/2 #가운데 두숫자의 합을 더해 2로 나눔
else: #length가 홀수라면
    median=sum(removedList,0.0)/length #list의 합을 length로 나눔

print("Median: {}".format(median))




