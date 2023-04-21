stack=[]
specialString=["(", ")", "[", "]"]
def strip_all_not_in_specialString(inputString):
    newString=[]
    for i in inputString:
        if i in specialString:
            newString.append(i)
    return newString

while True:
    inp = input()
    if inp == ".":
        break
    inputString = inp.strip()
    newString = strip_all_not_in_specialString(inputString)
    for i in newString:
        if len(stack) != 0 and (stack[-1] == "(" and i == ")" or stack[-1] == "[" and i == "]"):
            stack.pop()
        else:
            stack.append(i)
    print("yes") if len(stack)==0 else print("no")
    stack.clear()








