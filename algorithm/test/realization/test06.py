list = []
for i in input():
    list.append(int(i))
if sum(list[:len(list)//2]) == sum(list[len(list)//2:]):
    print("LUCKY")
else:
    print("READY")