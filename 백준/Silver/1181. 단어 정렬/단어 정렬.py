n = int(input())

string_list = list(set([input() for _ in range(n)]))

answer = sorted(string_list, key = lambda x: (len(x), x))

for i in answer:
    print(i)