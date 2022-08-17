n = int(input())
arr = [int(input()) for _ in range(n)]

# 산술평균
def average(arr):
    answer = sum(arr) / len(arr)
    return round(answer)

# 중앙값
def median(arr):
    arr.sort()
    med = len(arr) // 2
    return arr[med]

# 최빈값
def many(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        count = {}
        maxcount = 0
        an_cnt = 0
        for i in arr:
            # 딕셔너리에 있을때 count 1 추가
            if count.get(i) != None:
                count[i] += 1
            # 딕셔너리가 없을때 count 만들기
            else:
                count[i] = 1
        for j in count:
            if count[j] > maxcount:
            # 전체적으로 돌면서 maxcount 업데이트
                maxcount = count[j]
                answer = j
                an_cnt = 0
            elif count[j] == maxcount:
                # maxcount가 나오고 한번 더 나올시 멈춰주는 코드 -> 두번째로 작은 값
                if an_cnt == 0 and answer < j:
                    answer = j
                    an_cnt += 1
        return answer

# 범위
def ranges(arr):
    return arr[-1] - arr[0]

print(average(arr))
print(median(arr))
print(many(arr))
print(ranges(arr))