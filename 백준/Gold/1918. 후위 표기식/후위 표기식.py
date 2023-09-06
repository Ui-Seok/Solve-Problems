import sys
input = sys.stdin.readline

arr = list(input())
st = []
result = ""

for s in arr:
    if s.isalpha():
        result += s

    else:
        if s == "(":
            st.append(s)
        elif s == "*" or s == "/":
            while st and (st[-1] == "*" or st[-1] == "/"):
                result += st.pop()
            st.append(s)
        elif s == "+" or s == "-":
            while st and st[-1] != "(":
                result += st.pop()
            st.append(s)
        elif s == ")":
            while st and st[-1] != "(":
                result += st.pop()
            st.pop()

while st:
    result += st.pop()

print(result)