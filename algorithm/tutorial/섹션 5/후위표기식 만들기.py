import sys

sys.stdin = open("in5.txt", "rt")
data = list(input())

oper = []
for i in range(len(data)):
    chr = data[i]
    if chr.isdigit():
        print(chr,end="")
    else:
        if oper:
            while True and oper:
                if (oper[-1] == "*" or oper[-1] == "/") and (chr != "(" and chr!=")"):
                    print(oper.pop(),end="")
                else:
                    break
            while True and oper:
                if (chr == "+" or chr == "-") and (oper[-1] == "+" or oper[-1] == "-"):
                    print(oper.pop(), end="")
                else:
                    break
            if chr == ")":
                while True:
                    c = oper.pop()
                    if c == "(":
                        break
                    else:
                        print(c,end="")
            else:
                oper.append(chr)
        else:
            oper.append(chr)

while oper:
    print(oper.pop())

