from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    p = list(input().rstrip())
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    q = deque(arr)

    if n == 0:
        q = deque()

    rev_cnt = 0
    break_point = False
    for ps in p:
        if ps == "R":
            rev_cnt += 1
        else:
            try:
                if rev_cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            except:
                break_point = True
                print("error")
                break
    
    if not break_point:
        if rev_cnt % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")