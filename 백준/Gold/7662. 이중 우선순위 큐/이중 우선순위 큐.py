import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = int(input())

    # 리스트 생성
    max_arr = list()
    min_arr = list()
    answer = ''

    # 출력 조건 변수 생성
    check = [False for _ in range(a)]

    for idx in range(a):
        k, n = input().split()
        # 처음 문자가 I 일 때, 리스트에 숫자 추가
        if k == 'I':            
            # max 리스트와 min 리스트에 각각 숫자 추가
            heapq.heappush(max_arr, (-int(n), idx))
            heapq.heappush(min_arr, (int(n), idx))

            # 해당 인덱스 위치에 숫자가 있음을 확인
            check[idx] = True

        # 처음 문자가 D 일 때
        else:
            # 최소값 제거
            if int(n) == -1:
                # max에서 지워졌던 값을 제거하기 위한 반복 과정
                while min_arr and not check[min_arr[0][1]]:
                    heapq.heappop(min_arr)
                # min을 지우고 해당 index를 False로 변경하여 지웠다는 것을 체크
                if min_arr:
                    check[min_arr[0][1]] = False
                    heapq.heappop(min_arr)
            # 최대값 제거
            else:
                # min에서 지워졌던 값을 제거하기 위한 반복 과정
                while max_arr and not check[max_arr[0][1]]:
                    heapq.heappop(max_arr)
                # max를 지우고 해당 index를 False로 변경하여 지웠다는 것을 체크
                if max_arr:
                    check[max_arr[0][1]] = False
                    heapq.heappop(max_arr)

    # 마지막으로 한번 더 수행하여 지워졌던 값을 제거
    while min_arr and not check[min_arr[0][1]]:
        heapq.heappop(min_arr)
    while max_arr and not check[max_arr[0][1]]:
        heapq.heappop(max_arr)

    if max_arr and min_arr:
        answer = str(-max_arr[0][0]) + ' '
        answer += str(min_arr[0][0])
    else:
        answer = 'EMPTY'    

    print(answer)
