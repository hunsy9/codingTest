import sys
set = []
def add(num):
    if num not in set:
        set.append(num)
def remove(num):
    if num in set:
        set.remove(num)
def check(num):
    if num in set:
        print(1)
    else:
        print(0)
def toggle(num):
    if num in set:
        set.remove(num)
    else:
        set.append(num)
def all():
    set.clear()
    for i in range(1,21):
        set.append(i)
def empty():
    set.clear()
def commandController(command, num):
    if command == "add": add(num)
    if command == "remove": remove(num)
    if command == "check": check(num)
    if command == "toggle": toggle(num)

N=int(input())
for i in range(N):
    inputString = sys.stdin.readline()
    command = inputString.split(" ")[0].rstrip()
    if command == "all":
        all()
    elif command == "empty":
        empty()
    else:
        num = int(inputString.split(" ")[1])
        commandController(command,num)
