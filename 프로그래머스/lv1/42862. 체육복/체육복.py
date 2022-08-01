def solution(n, lost, reserve):
    answer = 0
    students = {}
    
    # 현재 옷을 가지고 있는 학생들의 dictionary
    for i in range(n):
        students[i + 1] = 1
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
        
    # 학생이 옷을 2벌 가지고 있으면서 양옆의 학생이 옷이 없을때 주는 조건
    for student, cloth in students.items():
        if student == 1 and cloth == 2: 
            if students[2] == 0:
                students[2] += 1
                students[1] -= 1
        elif student == n and cloth == 2:
            if students[n - 1] == 0:
                students[n - 1] += 1
                students[n] -= 1
        elif cloth == 2:
            if students[student - 1] == 0:
                students[student - 1] += 1
                students[student] -= 1
            elif students[student + 1] == 0:
                students[student + 1] += 1
                students[student] -= 1
                
    # 옷을 가지고 있는 학생의 숫자 카운트
    for _, i in students.items():
        if i != 0:
            answer += 1
    return answer