n,r,c = map(int,input().split(" "))
cnt = 0
while n > 1:
    ran = 2 ** (n-1)
    if r >= ran and c >= ran: #4사분면
        cnt+=(ran**2)*3
        r-=ran
        c-=ran
    elif r >= ran and c < ran: #3사분면
        cnt+=(ran**2)*2
        r-=ran
    elif r < ran and c >= ran: #1사분면
        cnt+=(ran**2)
        c-=ran
    elif r < ran and c < ran: #2사분면
        pass
    n-=1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt+1)
if r == 1 and c == 0:
    print(cnt+2)
if r == 1 and c == 1:
    print(cnt+3)
