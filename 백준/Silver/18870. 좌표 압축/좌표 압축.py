import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 다시 정렬을 하기 위해 딕셔너리로 value에 input값을 저장
num_dict = dict()
for idx, num in enumerate(arr):
    num_dict[idx] = num

# value를 기준으로 오름차순으로 정렬
num_dict = dict(sorted(num_dict.items(), key=lambda x: x[1]))
# print(num_dict)
# value값을 0부터 시작해서 변경, 만약 같은 숫자라면 같은 value 부여
val = -1
prev = list(num_dict.values())[0] - 1
for x in num_dict:
    if prev == num_dict[x]:
        num_dict[x] = val
    else:
        prev = num_dict[x]
        val += 1
        num_dict[x] = val

# 다시 key별로 오름차순으로 정렬
num_dict = dict(sorted(num_dict.items(), key=lambda x: x[0]))

# value값을 리스트로 변환 후 하나씩 출력
answer = list(num_dict.values())
print(*answer)