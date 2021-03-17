from itertools import combinations

def solution(orders, course):
    result = []
    # 세트메뉴 구성 개수별 계산
    for i in course:
        # 메뉴가 얼마나 반복되는지 판단하기 위한 딕셔너리(order의 모든 조합을 넣을 것)
        course_iter = {}
        # 한 손님의 order에 대해 ex) "XYZ", "XWY", "WXA" 각각에 대해
        for order in orders:
            keys = []
            # course 수만큼 조합을 뽑아본다. (튜플이 나옴) ex) ("X", "Y"), ("X", "Z"), ("Y", "Z")
            for menus in list(combinations(order, i)):
                # 튜플을 리스트로 만들고 오름차순 정렬 ex) ('X', 'W') -> ['W', 'X']
                menus = sorted(list(menus))
                # 문자열을 합치고 key 목록에 추가
                keys.append(''.join(menus))
            # 키를 딕셔너리에 추가하며 개수를 셈
            for key in keys:
                try:
                    course_iter[key] += 1 # 키가 딕셔너리에 있을 때
                except:
                    course_iter[key] = 1 # 키가 없을 때

        # 키 개수의 최대값 구하기
        max_val = 0
        for val in course_iter.values():
            if val > max_val:
                max_val = val

        # 2명 이상이 주문했고 가장 많이 주문된 세트메뉴 찾기
        for key, val in course_iter.items():
            if val == max_val and val > 1:
               result.append(key)
    # 오름차순 정렬
    result.sort()
    return result

테스트 1 〉	통과 (0.19ms, 10.1MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (0.20ms, 10.2MB)
테스트 4 〉	통과 (0.20ms, 10.2MB)
테스트 5 〉	통과 (0.20ms, 10.2MB)
테스트 6 〉	통과 (0.41ms, 10.3MB)
테스트 7 〉	통과 (0.60ms, 10.3MB)
테스트 8 〉	통과 (4.21ms, 10.3MB)
테스트 9 〉	통과 (2.82ms, 10.4MB)
테스트 10 〉	통과 (3.76ms, 10.4MB)
테스트 11 〉	통과 (2.14ms, 10.3MB)
테스트 12 〉	통과 (2.51ms, 10.3MB)
테스트 13 〉	통과 (5.02ms, 10.4MB)
테스트 14 〉	통과 (2.90ms, 10.3MB)
테스트 15 〉	통과 (3.18ms, 10.4MB)
테스트 16 〉	통과 (1.20ms, 10.3MB)
테스트 17 〉	통과 (0.63ms, 10.2MB)
테스트 18 〉	통과 (0.27ms, 10.2MB)
테스트 19 〉	통과 (0.04ms, 10.2MB)
테스트 20 〉	통과 (0.84ms, 10.2MB)

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))