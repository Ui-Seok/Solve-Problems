'''
시작시간: 19시 01분
종료시간:
'''

def solution(w,h):
    answer = 1
    if w > h:
        if w % h != 0:
            wasted = (w // h) + 1
        else:
            wasted = w // h
        answer = (w * h) - (h * wasted)
    elif w < h:
        if h % w != 0:
            wasted = (h // w) + 1
        else:
            wasted = h // w
        answer = (w * h) - (w * wasted)
    else:
        answer = (w * h) - w
    if answer % 2 != 0:
        answer -= 1
    return answer