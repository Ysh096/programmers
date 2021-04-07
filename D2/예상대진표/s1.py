# # 부전승은 발생하지 않는다.
# # n, a, b가 주어진다.
# def solution(n, a, b):
#     rnd = 1 # round
#     if a > b:
#         a, b = b, a
#     # a가 무조건 더 작은 값이라고 생각하고 계산하자.
#     # 짝수면 짝수-1번하고 붙게됨
#     # 홀수면 홀수+1번하고 붙게됨
#     while True:
#         if b-1 == a: # 종료조건
#             return rnd
#         if a % 2:
#             a = (a+1) // 2
#         else:
#             a = a // 2
#         if b % 2:
#             b = (b+1) // 2
#         else:
#             b = b // 2
#         rnd += 1
# # 7, 9, 27, 33번 테케 실패
# n = 8
# a = 6
# b = 8
# print(solution(n, a, b))
#
# # 통과! 종료조건을 잘 생각해야함.
# # 부전승은 발생하지 않는다.
# # n, a, b가 주어진다.
# def solution(n, a, b):
#     rnd = 1 # round
#     if a > b:
#         a, b = b, a
#     # a가 무조건 더 작은 값이라고 생각하고 계산하자.
#     # 짝수면 짝수-1번하고 붙게됨
#     # 홀수면 홀수+1번하고 붙게됨
#     while True:
#         if b%2 + b//2 == a%2 + a//2: # 종료조건
#             return rnd
#         if a % 2:
#             a = (a+1) // 2
#         else:
#             a = a // 2
#         if b % 2:
#             b = (b+1) // 2
#         else:
#             b = b // 2
#         rnd += 1


def solution(n,a,b):
    answer = 0
    # 완전이진트리의 가장 하위 자식노드로 보내주기
    # 부모노드가 같아질 때까지 부모노드로 이동하기
    while a != b:
        a //= 2
        b //= 2
        answer += 1
    return answer+1

n = 8
a = 4
b = 7
print(solution(n, a, b))