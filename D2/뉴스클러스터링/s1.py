# 뉴스 클러스터링
# 자카드 유사도: 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# ex) A = {1, 2, 3} B = {2, 3, 4} -> A교B = {2, 3}, A합B = {1, 2, 3, 4}
# 자카드 유사도 = 2/4
# A, B가 모두 공집합이면 J(A, B) = 1 <- 모든 문자에 특수문자가 겹쳐있는 경우..A, B가 공집합이 될 수 있음.
# 다중집합이면 교집합 = 다중 원소의 최소 개수, 합집합 = 다중 원소의 최대 개수
# 두 문자열의 자카드 유사도 검사하기

# 조건1. 대문자, 소문자 구분은 없음
# 조건2. 영문자로 된 글자 쌍만 유효하고, 나머지 숫자나 특수 문자 등이 들어 있으면 제외한다.
# str1, str2를 다중집합으로 만든다.
# 다중집합은 딕셔너리가 좋을듯?
def multi_setting(str):
    multi_set = {}
    for i in range(len(str)-1):
        # 영문자인지 확인
        if 97 <= ord(str[i]) <= 122 and 97 <= ord(str[i+1]) <= 122:
            chr = str[i]+str[i+1]
            if multi_set.get(chr): # 이미 있으면
                multi_set[chr] += 1
            else:
                multi_set[chr] = 1
    return multi_set

def solution(str1, str2):
    # 두 글자씩 끊어서 다중집합 원소로 만들기(set 자료형을 사용할 수는 없음)
    str1 = str1.lower()
    str2 = str2.lower()
    A = multi_setting(str1)
    B = multi_setting(str2)
    if not B: # 합집합이 공집합이면,
        return 1*65536
    # 교집합: 겹치는 원소의 최솟값
    # 합집합: 겹치는 원소의 최댓값 + 안겹치는 원소
    # 1. 교집합 구하기 + 합집합에서 겹치는거 + B에 없는거 개수 세기
    inter_result = 0
    union_result = 0
    for key, val in A.items():
        if B.get(key): # str1의 원소가 str2에 있으면
            inter_result += min(val, B.get(key))
            union_result += max(val, B.get(key))
        else:
            # union_result += 1 # 1이 아니라 개수만큼 더해줘야한다!!
            union_result += val

    # 2. 합집합 구하기
    # B에는 있는데 A에는 없는거 구하기
    for key, val in B.items():
        if not A.get(key):
            union_result += val
    return int((inter_result/ union_result) * 65536)

str1 = "handshake"
str2 = "shake hands"
str1 = "FRANCE"
str2 = "FRENCH"

result = solution(str1, str2)
print(result)


