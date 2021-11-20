import sys

cnt = 0
for i in range(int(sys.stdin.readline().rstrip())):
    slist = []
    s = sys.stdin.readline().rstrip()
    loop = False
    s1 = s[0]
    slist.append(s[0])
    for j in range(1,len(s)):
        if s1 == s[j]:
            slist.append(s[j])
        else:
            if s[j] in slist:
                loop = True
                break
            else:
                slist.append(s[j])
        s1 = s[j]
    if not loop:
        cnt+=1

print(cnt)
