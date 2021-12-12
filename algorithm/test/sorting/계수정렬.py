array = [7,5,9,0,3,1,6,2,1,4,8,0,5,2]
nlist = [0]*(max(array)+1)
for i in range(len(array)):
    nlist[array[i]]+=1

for i in range(len(nlist)):
    for j in range(nlist[i]):
        print(i,end=' ')
