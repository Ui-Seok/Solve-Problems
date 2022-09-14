from collections import deque

for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    from_to = [[] for _ in range(101)]
    visit = [0] * 101
    
    for i in range(n):
        if i % 2 == 0:
            from_to[arr[i]].append(arr[i+1])
        
    q = deque()
    q.append(start)
    visit[start] += 1

    while q:
        a = q.popleft()
        for i in from_to[a]:
            if visit[i] == 0:
                visit[i] = visit[a] + 1
                q.append(i)
            else:
                continue
        
    max_visit = max(visit)

    for i in range(100, -1, -1):
        if visit[i] == max_visit:
            ans = i
            break
    
    print('#{} {}'.format(tc, ans))