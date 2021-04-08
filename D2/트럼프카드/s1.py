from itertools import combinations

# 52장의 카드에서 숫자가 겹치지 않게 5개 조합 만들기
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
         27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
         40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# 숫자 % 13 해서 이미 뽑은 수면 뽑지 않기
result = list(combinations(cards, 5))
# print(len(result))
answer = 0
for i in range(len(result)):
    temp_result = [0, 0, 0, 0, 0]
    for j in range(5):
        temp_result[j] = result[i][j] % 13
    if len(temp_result) == len(set(temp_result)): # 겹치면 집합의 길이가 달라짐
        answer += 1
print(answer)

52C1 * 48C1 * 44C1 * 40C1 * 36C1 / 5! = 1317888
