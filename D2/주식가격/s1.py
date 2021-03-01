# def solution(prices):
#     answer = [0]
#     stack = [prices.pop()]
#     while prices:
#         tmp = 0  # answer에 넣을 값
#         for value in stack:
#             tmp += 1
#             if prices[-1] > value:  # 가격이 떨어지지 않았다면
#                 break
#         stack = [prices.pop()] + stack
#         answer = [tmp] + answer
#
#     return answer
#
# print(solution([1, 2, 3, 2, 3]))

def solution(prices):
    ans = []
    i = 0
    while i < len(prices)-1:
        j = i+1
        tmp = 1
        while j < len(prices)-1:
            if prices[i] <= prices[j]:
                j += 1
                tmp += 1
            else:
                break
        ans.append(tmp)
        i += 1
    return ans + [0]

print(solution([1, 2, 3, 2, 3]))