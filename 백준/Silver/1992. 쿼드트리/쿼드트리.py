n = int(input())

graph = list()
for _ in range(n):
    a = list(map(int, input()))
    graph.append(a)

def check_graph(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break
    if check == -1:
        print("(", end='')
        n = n // 2
        check_graph(x, y, n)
        check_graph(x, y + n, n)
        check_graph(x + n, y, n)
        check_graph(x + n, y + n, n)
        print(")", end='')
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

check_graph(0, 0, n)