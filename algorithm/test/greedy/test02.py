ss =[int(i) for i in input()]
ss.sort()
sum = 0
cnt = 0
for i in range(len(ss)):
    if ss[i] == 0 or ss[i]==1:
        sum+=ss[i]
    elif cnt==0 and ss[i]!=0:
        sum+=ss[i]
        cnt+=1
    elif cnt>0 and ss[i]!=0:
        sum*=ss[i]
print(sum)