a,b,c = map(int,input().split(" "))
print(-1 if c-b <= 0 else (a//(c-b)+1))
