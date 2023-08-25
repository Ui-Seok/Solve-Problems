import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

check_p = "IO" * n + "I"
answer = 0
for i in range(m - n):
    if s[i:(i + (2*n + 1))] == check_p:
        answer += 1

print(answer)