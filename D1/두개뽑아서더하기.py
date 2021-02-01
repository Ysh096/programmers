def solution(numbers):
    answer = []
    #만약에, numbers 길이가 72라면?
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                result = numbers[i]+numbers[j]
                answer.append(result)
    A = set(answer)
    answer = list(A)
    answer.sort()
    return answer