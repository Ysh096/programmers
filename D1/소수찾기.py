def solution(n):
    #n은 2이상
    primes = [2, 3]
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else: #n이 4이상일 때
        i = 2
        while i <= n:
            j = 0
            while j < len(primes):
                if i % primes[j] == 0: #소수로 나누어 떨어지면
                    break
                else: #나누어 떨어지지 않으면
                    j += 1 #다음 소수를 확인
                if j == len(primes):
                    primes.append(i)
            i += 1 #다음 숫자로

    return len(primes)

ans = solution(10)
print(ans)