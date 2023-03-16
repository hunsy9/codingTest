def product(s, n):
    result = 1
    for i in range(s, s+n):
        result *= i
    return result

N = int(input())

sum = 0
multipliedResult = 1
startNum = 100000

for i in range(N+2):
    num = int(input())
    sum += num
    multipliedResult *= num
    if num < startNum:
        startNum = num

x_plus_y = sum - (N*((2 * startNum) + N-1)) / 2
x_multiply_y = multipliedResult / product(startNum, N)
x_minus_y = (x_plus_y**2 - 4 * x_multiply_y)**0.5

print(round((x_plus_y - x_minus_y) / 2))
print(round((x_plus_y + x_minus_y) / 2))






