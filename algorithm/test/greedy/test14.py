n,m = map(int,input().split(" "))
plist = list(map(int,input().split(" ")))+[0]
array = []
cnt = 0
for i in range(m):
    if plist[i] in array:
        continue
    if len(array) < n:
        array.append(plist[i])
        continue
    if plist[i] not in array:
        cnt += 1
        index1 = 0
        index2 = 0
        for j in range(n):
            try:
                idx = plist[i+1:].index(array[j])
                if index1 < idx:
                    index1 = idx
                    index2 = j
            except:
                index2 = j
                break
        array[index2]=plist[i]
    else:
        pass
print(cnt)


