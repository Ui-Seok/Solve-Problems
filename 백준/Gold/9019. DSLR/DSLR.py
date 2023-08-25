from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    a, b = map(int, input().split())
    q = deque()
    visit = [False] * 10000
    visit[a] = True
    q.append((a, ""))

    while q:
        num, root = q.popleft()
        
        if num == b:
            print(root)
            break
    
        num_d = 2 * num % 10000
        if not visit[num_d]:
            q.append((num_d, root + "D"))
            visit[num_d] = True

        num_s = (num - 1) % 10000
        if not visit[num_s]:
            q.append((num_s, root + "S"))
            visit[num_s] = True

        num_l = (num % 1000 * 10) + (num // 1000)
        if not visit[num_l]:
            q.append((num_l, root + "L"))
            visit[num_l] = True

        num_r = (num % 10 * 1000) + (num // 10)
        if not visit[num_r]:
            q.append((num_r, root + "R"))
            visit[num_r] = True