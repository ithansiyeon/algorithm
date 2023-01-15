n,k = map(int,input().split())
alist = list(map(int,input().split()))
aSorted = [0]*n # 정렬 배열은 반드시 전역 변수로 선언
cnt = 0
def merge(a,l,m,r):
    global cnt
    i,j,t = l,m+1,l
    # 작은 순서대로 배열에 삽입
    while i <= m and j <= r:
        if a[i] <= a[j]:
            aSorted[t] = a[i]
            i+=1
        else:
            aSorted[t] = a[j]
            j+=1
        t+=1
    # 남은 데이터도 배열에 삽입
    if i > m:
        for p in range(j,r+1):
            aSorted[t] = a[p]
            t+=1
    else:
        for p in range(i,m+1):
            aSorted[t] = a[p]
            t+=1
    # 정렬된 데이터를 삽입
    for p in range(l,r+1):
        a[p] = aSorted[p]
        cnt+=1
        if cnt == k:
            print(aSorted[p])
def merge_sort(a,l,r):
    # 크기가 1보다 큰 경우
    if l < r:
        m = (l+r) // 2
        merge_sort(a,l,m)
        merge_sort(a,m+1,r)
        merge(a,l,m,r)

merge_sort(alist,0,n-1)
if cnt < k:
    print(-1)


