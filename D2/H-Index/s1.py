def solution(citations):
    citations.sort()
    L = len(citations)
    cnt = 0
    i = 0
    possible = []
    while i < L:
        h = L-i # citations[i]번 인용된 논문의 수
        if citations[i] < h:
            possible.append(citations[i])
            i += 1
        else:
            return h
    return citations[-1]
citations = [0, 1, 4, 5, 6]
print(solution(citations))