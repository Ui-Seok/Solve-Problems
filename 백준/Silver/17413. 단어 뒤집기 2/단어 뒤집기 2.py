import sys
input = sys.stdin.readline

arr = input().strip()

st = []
answer = ""
point = False
for i in arr:
    if i == " " and not point:
        while st:
            answer += st.pop()
        answer += " "

    if i == "<":
        if st:
            while st:
                answer += st.pop()
        answer += i
        point = True

    elif i == ">":
        answer += i
        point = False

    elif point:
        answer += i

    elif not point and i != " ":
        st.append(i)

if st:
    while st:
        answer += st.pop()

print(answer.strip())