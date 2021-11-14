s = input()
for i in list(range(ord('a'),ord('z')+1)):
    try:
        print(s.index(chr(i)),end=" ")
    except:
        print(-1,end=" ")