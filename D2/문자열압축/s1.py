# def solution(s):
#     # dictionary를 이용하면 좋지 않을까?
#     ans = []
#     if len(s) == 1:
#         return 1
#     for i in range(1, len(s)//2 + 1): # 확인해 볼 자름 단위
#         tmp_list = []
#         for j in range(0, len(s), i):
#             tmp_list.append(s[j:j+i]) # 일단 i 단위로 자른걸 일렬로 늘어놔보자.
#         tmp_list.append(0) # padding
#         cnt = 1 # 반복 횟수를 셀 변수
#         tmp_str = ''
#         for idx in range(len(tmp_list)-1):
#             # 현재 값 == 다음 값이면 반복되는 것이므로 cnt+=1
#             if tmp_list[idx] == tmp_list[idx+1]:
#                 cnt += 1
#             elif tmp_list[idx] != tmp_list[idx+1] and cnt != 1:
#                 tmp_str += str(cnt) + tmp_list[idx]
#                 cnt = 1
#             else: #cnt == 1일 때
#                 tmp_str += tmp_list[idx]
#
#         ans.append(len(tmp_str))
#         print(tmp_str)
#     return min(ans)
# solution('a')

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
