def solution(n):
    q = n  # while문이 시작하도록 하는 초기값
    num_list = []
    while q != 0:
        r = q % 10  # 나머지 먼저 구하기
        q = q // 10  # 몫
        num_list += [r]
    # num_list의 역방향 정렬
    # 선택정렬
    i = 0
    while i in range(len(num_list)):
        max_num = num_list[i]
        for j in range(i + 1, len(num_list)):
            if max_num < num_list[j]:
                max_num = num_list[j]
                idx = j
        if max_num != num_list[i]:
            num_list[i], num_list[idx] = num_list[idx], num_list[i]
        i += 1
    return num_list

a = solution(118372)
print(a)