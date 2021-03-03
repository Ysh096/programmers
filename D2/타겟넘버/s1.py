arr = [3, 6, 7, 1, 5, 4]

def solution(numbers, target):
    # 부분집합 구하기를 응용해볼 수 있을 것 같다.
    n = len(numbers)
    cnt = 0
    for i in range(1<<n):
        tmp = []
        for j in range(n):
            if i & (1<<j): # 둘을 비교해서 둘 다 1이면
                tmp.append(1)
            else:
                tmp.append(0)
        print(tmp)
        result = 0
        for idx, val in enumerate(tmp):
            if val == 0:
                result += numbers[idx]
            else:
                result -= numbers[idx]
        if result == target:
            cnt += 1
    return cnt

print(solution([3, 6, 7, 1, 5, 4], 26))