import sys
from collections import Counter

string = sys.stdin.readline().rstrip().upper()
slist = Counter(string).most_common(2)
if len(string) == 1:
    print(string)
elif slist[0][1] == slist[1][1]:
    print("?")
else:
    print(slist[0][0])
