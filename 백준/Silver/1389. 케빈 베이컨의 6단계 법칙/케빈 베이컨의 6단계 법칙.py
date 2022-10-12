from collections import deque

n, m = map(int, input().split())
fr = dict()
for _ in range(m):
    a, b = map(int, input().split())

    if fr.get(a) == None:
        fr[a] = [b]
    else:
        if b in fr[a]:
            continue
        else:
            fr[a].append(b)

    if fr.get(b) == None:
        fr[b] = [a]
    else:
        if a in fr[b]:
            continue
        else:
            fr[b].append(a)

min_kv = 1000
fr_num = 0
for k in fr.keys():
    kevin_k = 0
    for i in range(1, n+1):
        if k == i:
            continue
        else:
            visited = [0 for _ in range(n+1)]
            q = deque()
            q.append(k)

            while q:
                a = q.popleft()
                if i in fr[a]:
                    kevin_k += visited[a]
                    break
                for v in fr[a]: 
                    if visited[v] == False:
                        visited[v] = visited[a] + 1
                        q.append(v)

    if kevin_k < min_kv:
        min_kv = kevin_k
        fr_num = k
    elif kevin_k == min_kv:
        if k < fr_num:
            fr_num = k
print(fr_num)