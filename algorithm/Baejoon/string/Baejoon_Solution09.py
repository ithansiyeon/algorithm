clist = ['c=','c-','dz=','d-','lj','nj','s=','z=']
sum = 0
s = input()
for i in clist:
    n = s.count(i)
    sum+=n
    if n > 0:
        s=s.replace(i," ")
print(sum+len(s.replace(" ","")))