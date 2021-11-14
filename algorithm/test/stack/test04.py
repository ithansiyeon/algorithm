import sys
string = []
while True:
    sen = sys.stdin.readline().rstrip()
    if sen == ".":
        break
    string.append(sen)

for s in string:
    loop = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack)==0 or stack.pop() != "(":
                print("no")
                loop = False
                break
        elif i == "]":
            if len(stack)==0 or stack.pop() != "[":
                print("no")
                loop = False
                break
    if len(stack) == 0 and loop:
        print("yes")
    elif len(s) !=0 and loop:
        print("no")
