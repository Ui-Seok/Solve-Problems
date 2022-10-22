n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer_0 = 0
answer_1 = 0
answer_1_ = 0

def get_nums(x, y, dims):
    global answer_0, answer_1, answer_1_

    num_check = arr[x][y]
    for i in range(x, x+dims):
        for j in range(y, y+dims):
            if arr[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        get_nums(x + k * dims//3, y + l * dims//3, dims//3)
                return

    if num_check == 0:
        answer_0 += 1
    elif num_check == 1:
        answer_1 += 1
    else:
        answer_1_ += 1
    
get_nums(0, 0, n)
print(f'{answer_1_}\n{answer_0}\n{answer_1}')