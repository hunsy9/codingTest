num = int(input('Enter a pyramid level: '))
cnt = 1
for i in range(num):
    s=''
    for j in range(num - i):
        s += ' '
    for j in range(cnt):
        s += '*'
    print(s)
    cnt += 2

