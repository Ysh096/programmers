def dec_to_123(n):
    # 3진법하고 미묘하게 다름
    # 1. n을 3으로 나눠서 나누어 떨어질 경우 몫-1, 나머지+3으로 표현
    # 2. n을 3으로 나눠서 몫이 3보다 큰 경우 3이하 값이 나올 때 까지 나눠주고, 나머지를 반환
    if n % 3 == 0: # 나머지가 0인 경우
        r = 3 # 나머지 = 3
        n = (n // 3) -1 # 몫 = 몫-1
        if n > 3:
            return dec_to_123(n) + str(r)
        else:
            return str(n) + str(r)
        
    else: # 나머지가 0이 아닌 경우
        r = n % 3
        n = n // 3
        if n <= 3:
            return str(n) + str(r)
        else: # 나눈 몫이 3보다 큰 경우
            return dec_to_123(n) + str(r)
        
def solution(n):
    ans = ''
    result = dec_to_123(n) # 결과 01, 02, 03, 11, ...
    for v in result:
        if v == '0':
            continue
        elif v == '3':
            ans += '4'
        else:
            ans += v
    return ans

# 다른 사람들 풀이(훨씬 간단함 ㅜㅜ)
def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 1:
            answer = '1' + answer
            n //= 3
        elif n % 3 == 2:
            answer = '2' + answer
            n //= 3
        else:
            answer = '4' + answer
            n = n//3 - 1
    return answer