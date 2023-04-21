n, m = map(int, input().split())

count = 0
first_flag = False # B이면 0, W이면 1

#WWBWBWBWB
def increaseCount(row, first_flag):
    flag = first_flag
    count = 0
    print(row)
    for char in row:
        print("W flag and char: " if flag else "B flag and char: " , char)
        if not ((flag and char == "W") or (not flag and char == "B")):
            count += 1
        flag = not flag
    print("count in func: ", count)
    return count

for i in range(n):
    row = input()
    if i == 0 and row[0] == "W":
        first_flag = True
    print("first_flag: ", first_flag)
    count += increaseCount(row, first_flag)
    first_flag = not first_flag
print(count)