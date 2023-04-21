def print_fish(fish_bread):
    for i in fish_bread:
        print(i, end=' ')
    print()

def find_num(fish_bread, num):
    for i in range(len(fish_bread)):
        if num == fish_bread[i] or num == fish_bread[i] * -1:
            return i

def check_bread(fish_bread):
    for i in range(len(fish_bread)):
        if i + 1 != fish_bread[i]:
            return False
    return True

def reverse_fish_bread(fish_bread, start):
    for i in range(start, len(fish_bread)):
        if fish_bread[i] != i + 1:
            temp = find_num(fish_bread, i + 1)
            if temp > i:
                fish_bread[i:temp+1] = fish_bread[i:temp+1][::-1]
                for j in range(i, temp + 1):
                    fish_bread[j] *= -1
                return fish_bread
            elif temp < i:
                fish_bread[temp:i+1] = fish_bread[temp:i+1][::-1]
                for j in range(temp, i + 1):
                    fish_bread[j] *= -1
                return fish_bread
            else:
                fish_bread[temp] *= -1
                return fish_bread
    return fish_bread

def make_ans(fish_bread):
    temp_bread, flag = [], False
    for i in range(len(fish_bread)):
        temp_bread = reverse_fish_bread(fish_bread, i)
        print_fish(temp_bread)
        if check_bread(temp_bread):
            print("one")
            flag = True
            break
        else:
            temp_bread = reverse_fish_bread(temp_bread, 0)
            print_fish(temp_bread)
            if check_bread(temp_bread):
                print("two")
                flag = True
                break
    if not flag:
        print("over")

def make_input(n):
    for j in range(5):
        fish_bread = list(map(int, input().split()))
        make_ans(fish_bread)

n = int(input())
make_input(n)
