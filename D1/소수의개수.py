def solution(n):
    prime = [2, 3]
    if n == 2:
        return 1
    elif n <=4:
        return 2

    for num in range(5, n+1, 2):
        i = 1
        while prime[i] * prime[i] <= num:
            if num % prime[i] == 0:
                break
            i += 1
        else:
            prime.append(num)

    return len(prime)