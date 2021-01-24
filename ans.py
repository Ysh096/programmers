def solution(answers):
    L = len(answers) #만약 문제 수가 58개다?
    M1 = [1, 2, 3, 4, 5]
    M2 = [2, 1, 2, 3, 2, 4, 2, 5]
    M3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    (a1, b1) = divmod(L, len(M1)) #a = 몫, b = 나머지
    (a2, b2) = divmod(L, len(M2))
    (a3, b3) = divmod(L, len(M3))
    AM1 = M1 * a1 + M1[:b1]
    AM2 = M2 * a2 + M1[:b2]
    AM3 = M3 * a3 + M1[:b3] #세 학생의 답을 리스트로 표현
    
    def comparation(AM, ans):
        acc = 0
        F1 = list(zip(AM, ans))
        for e in F1:
            if e[0] == e[1]:
                acc +=1
            else:
                pass
        return acc
    acc1 = comparation(AM1, answers) #맞은 개수
    acc2 = comparation(AM2, answers)
    acc3 = comparation(AM3, answers)
    comp = [acc1, acc2, acc3]
    answer = []
    
    vmax = max(comp)
    for i, val in enumerate(comp):
        if vmax == val:
            answer.append(i+1)
    
    return AM2

answer = solution([1, 2, 3, 4, 5])

