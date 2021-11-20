import sys
from collections import Counter

string = sys.stdin.readline().rstrip().upper()
slist = Counter(string).most_common(2)
if len(slist) == 1:
    print(slist[0][0])
elif slist[0][1] == slist[1][1]:
    print("?")
else:
    print(slist[0][0])
