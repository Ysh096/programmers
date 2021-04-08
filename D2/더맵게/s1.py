# heapq는 우선순위 큐 알고리즘을 제공한다. 최소 힙의 형태로 원소가 정렬되며, 표준 모듈이다.
# heapq.heappush(heap, item): item을 heap에 추가
# heapq.heappop(heap): heap에서 가장 작은 원소를 pop(return도 함). 비어 있으면 indexError
# heapq.heapify(x): 리스트 x를 즉각적으로 heap으로 변환(O(N)의 시간복잡도)
# 사용시 기존 리스트를 힙처럼 사용할 것이 아니라면 heap = [] 처럼 빈 리스트를 만들고 내용을 heapq.~ 함수로 채워나가면 된다.

# import heapq
# # 섞은 음식의 스코빌 지수
# # 가장 맵지 않은 음식의 스코빌 지수 + 두 번째로 맵지 않은 음식의 스코빌 지수 * 2
# def solution(scoville, K):
#     heapq.heapify(scoville)
#     cnt = 0
#     while scoville[0] < K and len(scoville) > 1:
#         # 가장 안 매운 음식 뽑기, 뽑고 나면 heap이 재정렬됨! (뿌리 노드가 바뀌기 때문에 부모-자식 관계를 재정렬해야함)
#         least_spicy = heapq.heappop(scoville)
#         # 재정렬이 되고 나면 또 뿌리 노드에 최솟값이 있게 됨.
#         # [1, 3, 2, 9, 10, 12] 라면 3과 2는 처음에는 형제 관계라 1을 뽑고 나면 2와 3을 비교해야 할 것 같지만
#         # 1을 뽑고 난 후에는 [2, 3, 12, 9, 10] 으로 재정렬되어 2가 가장 앞(최솟값)에 위치하게 된다.
#         # 그래서 그냥 또 뽑으면 된다!
#         second_spicy = heapq.heappop(scoville)
#         new = least_spicy + second_spicy * 2
#         heapq.heappush(scoville, new)
#         cnt += 1
#     # while문이 끝난 경우는 가장 작은 값이 K보다 큰 경우거나,
#     # K보다 작고 scoville이 하나만 남은 경우이다.
#     if len(scoville) == 1 and scoville[0] < K:
#         return -1
#     else:
#         return cnt
#
#
#
#
# scoville = [1, 3, 2, 9, 10, 12]
# K = 7
#
# solution(scoville, K)

# # heap 직접 구현
# def heap_push(queue, n):
#     queue.append(n)
#     last_idx = len(queue) - 1
#     # 마지막으로 확인한 인덱스가 0 이상일 때
#     while 0 < last_idx:
#         parent_idx = last_idx//2
#         # 부모가 자식보다 크면
#         if queue[parent_idx] > queue[last_idx]:
#             # swap
#             queue[parent_idx], queue[last_idx] = queue[last_idx], queue[parent_idx]
#             last_idx = parent_idx
#         else: # 부모가 자식보다 작으면
#             break
#
#
# def heap_pop(queue):
#     # 맨 앞 값을 가져올 것
#     last_idx = len(queue)-1
#     # 더 이상 뽑을게 없을 때
#     if last_idx < 0:
#         return -1
#     # pop을 쓰기 위해 순서 바꾸기
#     queue[0], queue[last_idx] = queue[last_idx], queue[0]
#     min_value = queue.pop()
#
#     # 재정렬
#     min_heapify(queue, 0)
#     return min_value
#
# def min_heapify(queue, idx):
#     left_child = 2*idx + 1
#     right_child = 2*idx + 2
#     min_idx = idx
#     # 만약 min_idx 위치의 값이 left, right child보다 크면
#     if left_child <= len(queue) - 1 and queue[min_idx] > queue[left_child]:
#         min_idx = left_child
#     if right_child <= len(queue) - 1 and queue[min_idx] > queue[right_child]:
#         min_idx = right_child
#     # 이제 min_idx는 부모 노드와 자식 노드 두개를 비교한 값 중 가장 작은 값의 인덱스이다.
#     # 현재 위치가 아니면 swap
#     if min_idx != idx:
#         queue[idx], queue[min_idx] = queue[min_idx], queue[idx]
#         min_heapify(queue, min_idx)
#
# def solution(scoville, K):
#     min_heapify(scoville, 0)
#     cnt = 0
#     while scoville[0] < K and len(scoville) > 1:
#         # 가장 안 매운 음식 뽑기, 뽑고 나면 heap이 재정렬됨!
#         # (뿌리 노드가 바뀌기 때문에 부모-자식 관계를 재정렬해야함)
#         least_spicy = heap_pop(scoville)
#         # 재정렬이 되고 나면 또 뿌리 노드에 최솟값이 있게 됨.
#         # [1, 3, 2, 9, 10, 12] 라면 3과 2는 처음에는 형제 관계라 1을 뽑고 나면 2와 3을 비교해야 할 것 같지만
#         # 1을 뽑고 난 후에는 [2, 3, 12, 9, 10] 으로 재정렬되어 2가 가장 앞(최솟값)에 위치하게 된다.
#         # 그래서 그냥 또 뽑으면 된다!
#         second_spicy = heap_pop(scoville)
#         new = least_spicy + second_spicy * 2
#         heap_push(scoville, new)
#         cnt += 1
#     if len(scoville) == 1 and scoville[0] < K:
#         return -1
#     else:
#         return cnt
# scoville = [1, 3, 2, 9, 10, 12]
# K = 7
#
# print(solution(scoville, K))

def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def solution(scoville, K):
    heap = []
    for i in scoville:
        heappush(heap, i)
    cnt = 0
    while heap[0] < K and len(heap) > 1:
        # 가장 안 매운 음식 뽑기, 뽑고 나면 heap이 재정렬됨! (뿌리 노드가 바뀌기 때문에 부모-자식 관계를 재정렬해야함)
        least_spicy = heappop(heap)
        # 재정렬이 되고 나면 또 뿌리 노드에 최솟값이 있게 됨.
        # [1, 3, 2, 9, 10, 12] 라면 3과 2는 처음에는 형제 관계라 1을 뽑고 나면 2와 3을 비교해야 할 것 같지만
        # 1을 뽑고 난 후에는 [2, 3, 12, 9, 10] 으로 재정렬되어 2가 가장 앞(최솟값)에 위치하게 된다.
        # 그래서 그냥 또 뽑으면 된다!
        second_spicy = heappop(heap)
        new = least_spicy + second_spicy * 2
        heappush(heap, new)
        cnt += 1
    # while문이 끝난 경우는 가장 작은 값이 K보다 큰 경우거나,
    # K보다 작고 scoville이 하나만 남은 경우이다.
    if len(heap) == 1 and heap[0] < K:
        return -1
    else:
        return cnt




scoville = [1, 3, 2, 9, 10, 12]
K = 7

print(solution(scoville, K))