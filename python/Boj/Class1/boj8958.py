for i in range(int(input())):
    str=input()
    a = 0
    sum = 0
    for j in str:
        if j=="O":
            a+=1
        else:
            a=0
        sum += a
    print(sum)
