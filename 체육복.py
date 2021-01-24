def solution(n, lost, reserve):
    #reserve[i]가 lost에 있으면 +1
    #reserve[i]는 lost에 없지만, reserve[i]-1 or reserve[i]+1이 lost에 있으면 +1
    answer = n-len(lost)
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if reserve[i] == lost[j]:
                answer +=1
                reserve[i] = -1
            elif (reserve[i] + 1) == lost[j] or (reserve[i] - 1) == lost[j]:
                answer +=1
                reserve[i] = -1
                
    return answer


n = 5
L = [2, 4]
R = [1, 3, 5]
print(solution(n, L, R))
