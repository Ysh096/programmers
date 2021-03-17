# heapq는 우선순위 큐 알고리즘을 제공한다. 최소 힙의 형태로 원소가 정렬되며, 표준 모듈이다.
# heapq.heappush(heap, item): item을 heap에 추가
# heapq.heappop(heap): heap에서 가장 작은 원소를 pop(return도 함). 비어 있으면 indexError
# heapq.heapify(x): 리스트 x를 즉각적으로 heap으로 변환(O(N)의 시간복잡도)
# 사용시 기존 리스트를 힙처럼 사용할 것이 아니라면 heap = [] 처럼 빈 리스트를 만들고 내용을 heapq.~ 함수로 채워나가면 된다.

import heapq
# 섞은 음식의 스코빌 지수
# 가장 맵지 않은 음식의 스코빌 지수 + 두 번째로 맵지 않은 음식의 스코빌 지수 * 2
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K and len(scoville) > 1:
        # 가장 안 매운 음식 뽑기, 뽑고 나면 heap이 재정렬됨! (뿌리 노드가 바뀌기 때문에 부모-자식 관계를 재정렬해야함)
        least_spicy = heapq.heappop(scoville)
        # 재정렬이 되고 나면 또 뿌리 노드에 최솟값이 있게 됨.
        # [1, 3, 2, 9, 10, 12] 라면 3과 2는 처음에는 형제 관계라 1을 뽑고 나면 2와 3을 비교해야 할 것 같지만
        # 1을 뽑고 난 후에는 [2, 3, 12, 9, 10] 으로 재정렬되어 2가 가장 앞(최솟값)에 위치하게 된다.
        # 그래서 그냥 또 뽑으면 된다!
        second_spicy = heapq.heappop(scoville)
        new = least_spicy + second_spicy * 2
        heapq.heappush(scoville, new)
        cnt += 1
    # while문이 끝난 경우는 가장 작은 값이 K보다 큰 경우거나,
    # K보다 작고 scoville이 하나만 남은 경우이다.
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    else:
        return cnt




scoville = [1, 3, 2, 9, 10, 12]
K = 7

solution(scoville, K)