import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 행렬 곱셈
def mul(mat_1, mat_2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat_1[i][k] * mat_2[k][j] % 1000
    
    return result

# 분할정복
def devide(a, b):
    if b == 1:
        return a
    else:
        tmp = devide(a, b // 2)
        if b % 2 == 0:
            return mul(tmp, tmp)    # b가 짝수인 경우
        else:
            return mul(mul(tmp, tmp), a)    # b가 홀수인 경우

result = devide(matrix, b)

for row in result:
    for col in row:
        print(col % 1000, end = " ")
    print()