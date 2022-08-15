n = int(input())
arr = [int(input()) for _ in range(n)]

def average(arr):
    answer = sum(arr) / len(arr)
    if answer < 0:
        return int(round(answer))
    else:
        return int(answer) + 1 if (answer - int(answer)) >= 0.5 else int(answer)

def median(arr):
    arr.sort()
    med = len(arr) // 2
    return arr[med]

def many(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        count = {}
        maxcount = 0
        an_cnt = 0
        for i in arr:
            if count.get(i) != None:
                count[i] += 1
            else:
                count[i] = 1
        for j in count:
            if count[j] > maxcount:
                maxcount = count[j]
                answer = j
                an_cnt = 0
            elif count[j] == maxcount:
                if an_cnt == 0 and answer < j:
                    answer = j
                    an_cnt += 1
        return answer

def ranges(arr):
    return arr[-1] - arr[0]

print(average(arr))
print(median(arr))
print(many(arr))
print(ranges(arr))