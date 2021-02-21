def solution(participant, completion):
    A = sorted(participant)
    B = sorted(completion)
    for i in range(len(participant)):
        try:
            if A[i] != B[i]:
                return A[i]
        except: #A[end]의 경우
            return A[i]