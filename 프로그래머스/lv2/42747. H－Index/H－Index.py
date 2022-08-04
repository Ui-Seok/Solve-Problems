def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    print(citations)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            print(idx, citation)
            return idx
    return len(citations)