def solution(operations):
    answer = []
    for i in operations:
        l = i.split()
        a = l[0]
        b = int(l[1])
        if a == "I":
            answer.append(b)
        elif answer:
            if b == 1:
                answer.remove(max(answer))
            elif b == -1:
                answer.remove(min(answer))
        else:
            continue
    if answer:
        answer = [max(answer), min(answer)]
    else:
        answer = [0, 0]
    return answer