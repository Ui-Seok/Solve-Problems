l = int(input())
string = input()
answer = 0

for idx, s in enumerate(string):
    new_s = ord(s) - 96
    answer += new_s * (31 ** idx) % 1234567891

print(answer)