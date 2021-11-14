loc = input()
cnt = 0
if ord(loc[0])+2 < 104 and int(loc[1])+1 < 8:
    cnt+=1
if ord(loc[0])+2 < 104 and int(loc[1])-1 >= 1:
    cnt+=1
if ord(loc[0])-2 >= 97 and int(loc[1])+1 < 8:
    cnt+=1
if ord(loc[0])-2 >= 97 and int(loc[1])-1 >= 1:
    cnt+=1
if int(loc[1])+2 <= 8 and ord(loc[0])+1 <= 104:
    cnt+=1
if int(loc[1])+2 <= 8 and ord(loc[0])-1 >= 97:
    cnt+=1
if int(loc[1])-2 >= 1 and ord(loc[0])+1 <= 104:
    cnt+=1
if int(loc[1])-2 >= 1 and ord(loc[1])-1 >= 97:
    cnt+=1
print(cnt)
