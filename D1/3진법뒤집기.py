def solution(n):
    answer = 0
    L = ''
    while n > 0:
        n, l = divmod(n, 3)
        L = L + str(l)  #3진수값
    return int(L, 3)