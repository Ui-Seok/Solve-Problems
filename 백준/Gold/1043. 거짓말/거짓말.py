from collections import deque

n, m = map(int, input().split())
know_arr = list(map(int, input().split()))

# bfs로 풀기위한 딕셔너리 map 생성 (양방향), 파티정보를 담을 리스트 생성
maps = {i: list() for i in range(1, n+1)}
party_info = list()
for _ in range(m):
    p_list = list(map(int, input().split()))
    pp = p_list[0]  # 파티에 있는 사람 수
    pn = p_list[1:] # 파티에 참석한 사람의 번호
    party_info.append((pp, pn)) # 파티의 정보 담기

    for i in pn:
        maps[i] += pn

# maps에 중복으로 들어간 인자들 삭제
for i in range(1, n+1):
    maps[i] = list(set(maps[i]))

# 큐 생성 및 진실을 알고있는 사람 확인
if know_arr[0] == 0:
    print(m)
else:
    q = deque()
    check = [False for _ in range(n+1)]
    true_p = know_arr[1:]

    # 진실을 알고있는 사람을 큐에 넣고 True로 변경
    for p in true_p:
        q.append(p)
        check[p] = True
    
    while q:
        a = q.popleft()
        for x in maps[a]:
            if not check[x]:
                check[x] = True
                q.append(x)

    # 과장을 할 수 있는 파티 확인
    answer = 0
    for k, v in party_info:
        for v_ in v:
            if check[v_]:
                break
        else:
            answer += 1
    print(answer)