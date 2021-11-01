n = int(input())
person = list(map(int,input().split(" ")))
person.sort()
result = 0
count = 0
for i in person:
    count += 1
    if count >= i:
        result+=1
        count = 0
print(result)

