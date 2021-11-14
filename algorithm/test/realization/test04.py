words = input()
alpa = ""
num = 0
for i in words:
    if i>='A' and i<='Z':
        alpa+=i
    else:
        num+=int(i)
print("".join(sorted(alpa))+str(num))
