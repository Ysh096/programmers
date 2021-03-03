# #처음 시도한 풀이
# def solution(N, stages):
#     p_num = len(stages) #사람 수
#     c = 0
#
#     pre_results = []
#     for n in range(1, N+1):
#         try:
#             f = stages.count(n)/(p_num-c)
#             c += stages.count(n)
#             pre_results.append([f, n])
#         except ZeroDivisionError: #p_num-c = 0이 되는 경우, 이 경우  바로 전 단계에서 아무도 올라오지 못했음을 의미
#             pre_results.append([0, n])
#     pre_results = sorted(pre_results)
#
#     result = [pre_results[0][1]]
#     val = pre_results[0][0]
#     count = 0
#     for i in range(1, len(pre_results)):
#         if val == pre_results[i][0]: #앞선 요소와 같은 값을 가지면
#             count += 1
#             result.insert(count, pre_results[i][1]) #앞선 요소의 바로 뒤에 추가되도록
#         else:
#             count = 0 #앞선 요소와 다르면
#             val = pre_results[i][0]
#             result = [pre_results[i][1]] + result #그보다 앞에 추가!
#
#     return result
#
#
# #람다 함수를 이용한 풀이
# def solution(N, stages):
#     p_num = len(stages) #사람 수
#     c = 0
#
#     pre_results = []
#     for n in range(1, N+1):
#         try:
#             f = stages.count(n)/(p_num-c)
#             c += stages.count(n)
#             pre_results.append([f, n])
#         except ZeroDivisionError:
#             pre_results.append([0, n])
#
#     pre_results = sorted(pre_results, key= lambda x: (-x[0], x[1])) #0번째 요소를 기준으로 내림차순 정렬 후 1번째 요소를 기준으로 오름차순 정렬
#     result = [pre_result[1] for pre_result in pre_results]
#     return result


def solution(N, stages):
    cnt_list = [0] * (N + 2)  # 인덱스 맞춰주기 위해 1개, 모든 스테이지 완료한 경우 위해 1개
    for val in stages:
        cnt_list[val] += 1

    # 게임을 하는 사람의 수
    people = len(stages)
    result = [-100]  # 스테이지별 실패율
    clear = 0  # 이전 스테이지까지 플레이한 사람의 수
    for i in range(1, N + 1):  # 1번부터 N번 스테이지까지
        try:
            result.append(cnt_list[i] / (people - clear))
            clear += cnt_list[i]
        except ZeroDivisionError:
            break
    if len(result) < N + 1:  # 뒤로는 도전한 사람이 아직 없을 때
        while len(result) != N + 1:
            result.append(0)

    answer = []
    while len(answer) < N:
        max_val = -1
        max_idx = 0
        for i in range(len(result)):
            if max_val < result[i]:
                max_val = result[i]
                max_idx = i
        result[max_idx] = -100
        answer.append(max_idx)
    return answer

print(solution(4, [3, 3, 3, 3, 3]))