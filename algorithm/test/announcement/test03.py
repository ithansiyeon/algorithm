for i in range(int(input())):
    grade = input()
    cnt = 0
    sum = 0
    for i in range(len(grade)):
        if grade[i] == 'O':
            cnt+=1
        else:
            cnt = 0
        sum+=cnt
    print(sum)