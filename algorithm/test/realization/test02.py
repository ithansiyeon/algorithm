n = int(input())
h = 0
m = 0
s = 0
cnt = 0
while h<=n:
    if '3' in str(s) or '3' in str(m) or '3' in str(h):
        cnt+=1
    if s+1 == 60:
        s = 0
        if m+1 == 60:
            m=0
            h+=1
        else:
            m+=1
    else:
        s+=1
print(cnt)

