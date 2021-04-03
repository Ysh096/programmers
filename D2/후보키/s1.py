from itertools import combinations

def transpose(relation, N, M):
    matrix = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            matrix[j][i] = relation[i][j]
    return matrix

def solution(relation):
    N = len(relation)
    M = len(relation[0])
    result = 0
    # 그냥 모든 경우 다 해보는 방향으로..
    tr_relation = transpose(relation, N, M) # transpose 해 놓고
    j_not_key = []
    for j in range(M):
        row = tr_relation[j]
        if len(set(row)) == len(row):
            result += 1 # 단독으로 후보키가 되는 열들은 추가해줌
        else:
            j_not_key.append(j) # 단독으로는 후보키가 아닌 열들

    # 후보키의 모든 조합 구하기
    j_length = len(j_not_key)
    key_combs = []
    if j_length == 1:
        return result
    else:
        for k in range(2, j_length+1):
            combs = combinations(j_not_key, k)
            for comb in combs:
                key_combs.append(comb)
    # print(key_combs)
    # ex) 1,2 열을 합친 것이 후보키가 되는지 확인
    # 되면 => 되는 리스트에 추가 [(1, 2)]
    # 1, 3 열을 합친 것이 리스트 원소의 subset인가? 아니라면 후보키가 되는지 확인
    # ...
    # 1, 2, 3 열을 합친 것이 리스트 원소의 subset인가? 아니라면 후보키가 되는지 확인
    possible_keys = []
    for keys in key_combs:
        # 최소조건 검사
        min_possible = True
        for possible_key in possible_keys:
            if set(possible_key).issubset(set(keys)):
                min_possible = False
                break
        if min_possible == False:
            continue

        tmp_relation = []
        possible = True
        for i in range(N):
            tmp_row = []
            for j in keys:
                tmp_row.append(relation[i][j])
                # 얘를 가지고 얘가 후보키가 되는지 확인해야 함.
            if tmp_row in tmp_relation:
                possible = False
                break
            else:
                tmp_relation.append(tmp_row)

        if possible == True: # 행별로 중복되는 값이 없을 때(후보키가 될 수 있을 때)
            possible_keys.append(keys)

    result += len(possible_keys)
    return result

relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(solution(relation))