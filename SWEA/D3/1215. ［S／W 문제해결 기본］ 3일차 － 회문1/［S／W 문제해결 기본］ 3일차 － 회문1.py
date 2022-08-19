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

for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8-n+1):
            lists = arr[i][j:j+n]
            if check(lists, n):
                count += 1

    for i in range(8-n+1):
        for j in range(8):
            lists = []
            for k in range(i, i+n):
                lists.append(arr[k][j])
                if check(lists, n):
                    count += 1

    print('#{} {}'.format(tc, count))