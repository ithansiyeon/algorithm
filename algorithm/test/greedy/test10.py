s = input()
cnt = 0
if s.count('1') < s.count('0'):
    for i in range(0,len(s)-1):
        if s[i]=='1':
            if s[i]!=s[i+1]:
                cnt+=1
else:
    for i in range(1,len(s)):
        if s[i]=='0':
            if s[i]!= s[i+1]:
                cnt+=1
print(cnt)

count1 = 0
count0 = 0
if s[0] == '1':
    count0+=1
else:
    count1+=1
for i in range(1,len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0+=1
        else:
            count1+=1
print(min(count0,count1))