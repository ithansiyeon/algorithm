def solution(routes):
    routes = sorted(routes,key=lambda x:(x[0],x[1]))
    print(routes)
    end = routes[0][1]
    cnt = 1
    for i in range(1,len(routes)):
        print(end)
        if routes[i][0] > end:
            cnt+=1
            end = routes[i][1]
        else:
            end = min(end,routes[i][1])

    return cnt

print(solution([[-2,-1], [1,2],[-3,0]]))