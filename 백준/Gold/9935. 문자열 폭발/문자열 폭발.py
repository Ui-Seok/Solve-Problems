import sys
input = sys.stdin.readline

arr = input().strip()
bomb = input().strip()

bomb_len = len(bomb)
bomb_last = bomb[-1]

st = []
answer = ""

for s in arr:
    st.append(s)
    if s == bomb_last and "".join(st[-bomb_len:]) == bomb:
        del st[-bomb_len:]

answer = "".join(st)
if answer:
    print(answer)
else:
    print("FRULA")