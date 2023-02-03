arr=input().lower() #"zza"
newArr=list(set(arr)) #za
cnt=[]
for i in newArr:
    count = arr.count(i)
    cnt.append(count)
if cnt.count(max(cnt))>=2:
    print("?")
else:
    print(newArr[(cnt.index(max(cnt)))].upper())