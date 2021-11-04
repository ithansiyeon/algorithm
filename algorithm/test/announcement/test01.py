for i in range(int(input())):
    nlist = list(map(int,input().split(" ")))
    mean = sum(nlist[1:])/nlist[0]
    cnt = 0
    for n in nlist[1:]:
        if n > mean:
            cnt+=1
    print('%0.3f%%'%(cnt/nlist[0]*100))


