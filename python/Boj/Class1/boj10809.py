ALPHABET="abcdefghijklmnopqrstuvwxyz"
s=input()
for i in ALPHABET:
    if i not in s:
        print("-1",end=' ')
    if i in s:
        print(str(s.index(i)),end=' ')

