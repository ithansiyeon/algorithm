from collections import Counter

x_list = []
y_list = []
for i in range(3):
    a,b = input().split(" ")
    x_list.append(a)
    y_list.append(b)
print(Counter(x_list).most_common()[-1][0],Counter(y_list).most_common()[-1][0])
