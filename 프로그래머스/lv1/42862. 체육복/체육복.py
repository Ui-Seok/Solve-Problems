def solution(n, lost, reserve):
    answer = 0
    students = {}
    
    for i in range(n):
        students[i + 1] = 1
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
        
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
            
    for _, i in students.items():
        if i != 0:
            answer += 1
    return answer