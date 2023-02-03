while True:
    arr=list(map(lambda x:int(x)**2,input().split()))
    if arr == [0,0,0]:
        break
    maxNum=max(arr)
    arr.remove(maxNum)
    if maxNum== arr[0]+arr[1]:
        print("right")
    else:
        print("wrong")
