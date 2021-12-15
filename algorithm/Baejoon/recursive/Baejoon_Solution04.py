n = int(input())
list = []
def hanoi(n,from_,to_,via):
    global cnt
    if n == 1:
        list.append([from_,to_])
        return

    hanoi(n-1,from_,via,to_)
    list.append([from_,to_])
    hanoi(n-1,via,to_,from_)

hanoi(n,1,3,2)
print(len(list))
for i in list:
    print(i[0],i[1])