n = sorted(input(),reverse=True)
sum = int(n[0])
for i in range(1,len(n)):
    if n[i] == '0' or n[i] == '1':
        sum+=int(n[i])
    else:
        sum*=int(n[i])
print(sum)