count = 0
total = 0
print('Enter -1 to terminate entering numbers.')
num = int(input('Enter a nonnegative integer: '))
min = num
max = num
while num != -1:
    if num < 0:
        print('Wrong input!')
        break
    count += 1
    total += num
    if num < min:
        min = num
    if num > max:
        max = num
    num = int(input('Enter a nonnegative integer: '))
else:
    if count > 0:
        print('Minimum:', min)
        print('Minimum:', max)
        print('Average:', total/count)
    else:
        print('No nonnegative integers were entered.')

