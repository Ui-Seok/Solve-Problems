def check(lists, n):
    if n % 2 == 0:
        left = lists[:n//2]
        right = lists[n//2:]
    else:
        left = lists[:n//2]
        right = lists[n//2 + 1:]
    if left == right[::-1]:
        return True
    else: return False

for _ in range(10):
    tc = int(input())
    palindrome = [list(input()) for _ in range(100)]
    max_length = 1
    # 슬라이딩 범위
    for i in range(100):
        # 슬라이딩에 맞춰 최대 조절
        for j in range(2, 101):
            # 슬라이딩 이동
            for k in range(101 - j):
                arr = palindrome[i][k:k+j]
                if check(arr, j):
                    if max_length < len(arr):
                        max_length = len(arr)
    # 슬라이딩 범위
    for i in range(max_length, 101):
        # 슬라이딩에 맞춰 최대 조절
        for j in range(101-i):
            # y 좌표
            for k in range(100):
                lists = []
                # x 좌표
                for p in range(j, j+i):
                    lists.append(palindrome[p][k])
                    if check(lists, i):
                        if max_length < len(lists):
                            max_length = len(lists)

    print('#{} {}'.format(tc, max_length))