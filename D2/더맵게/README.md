# lv2. 더 맵게

###### 문제 설명

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

```
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
```

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- scoville의 길이는 2 이상 1,000,000 이하입니다.
- K는 0 이상 1,000,000,000 이하입니다.
- scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

##### 입출력 예

| scoville             | K    | return |
| -------------------- | ---- | ------ |
| [1, 2, 3, 9, 10, 12] | 7    | 2      |

##### 입출력 예 설명

1. 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
   새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
   가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
2. 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
   새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
   가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.



# Heap 알고리즘

*우선순위 큐: 우선순위의 개념을 큐에 도입한 자료 구조로, 데이터들이 우선순위를 가져 우선순위가 높은 데이터가 먼저 나간다.



### Heap이란?

- 완전 이진 트리의 일종
- 우선순위 큐를 위하여 만들어진 자료구조
- 반정렬 상태를 유지
  - 큰 값이 상위 레벨, 작은 값이 하위 레벨이 있는 정도로 정렬되어 있음
  - 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 이진 트리!
- 힙 트리는 중복값을 허용한다. (?)



### 최대 힙

- 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리



### 최소 힙

- 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리



### Heap의 특징

- **노드 원소 값의 대소 관계는 오로지 부모 노드와 자식 노드 간에만 성립하며, 특히 형제 사이에는 대소관계가 정해지지 않은 상태이다.**

- 힙의 시간복잡도는 삽입, 삭제 모두 O(logn)이다.
  - 원소의 삽입, 삭제가 일어날 때, 전체 원소의 반만큼의 값과 비교하기 때문!



### 최대 힙 구현하기

```python
class MaxHeap(object):
    def __init__(self):
        self.queue = []
    # 배열에 값을 추가하는 방법!
    def insert(self, n):
        # 맨 마지막에 삽입할 원소를 임시로 추가
        self.queue.append(n)
        last_index = len(self.queue) - 1
        # 부모를 타고 올라가며 크기를 비교
        while 0 <= last_index:
            parent_index = self.parent(last_index) # 부모 노드의 인덱스 구하기
            # 부모 노드의 값이 추가한 인덱스보다 작으면(자식 노드보다 작으면)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index) # 자식 노드와 부모 노드의 value를 교환!
                last_index = parent_index # 인덱스를 부모 노드의 위치로 변경
                # 부모 노드의 인덱스는 신경쓰지 않아도 됨! self.parent를 통해 구하기 때문에
            # 부모 노드가 자식 노드보다 큰 값을 가지면
            else:
                break
                
    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index) # pop()을 쓰기 위해 0자리(최댓값)와 끝자리(최솟값)의 값을 바꿔줌
        maxv = self.queue.pop() # 아마 pop(0)보다 효율적이라 이걸로 쓰는듯?
        self.maxHeapify(0) # 뭔지 밑에서 살펴보자.
        return maxv
    
    # 임시 root부터 자식들과 값을 비교해나가며 재정렬하는 함수
    def maxHeapify(self, i):
        left_index = self.leftchild(i) # leftchild = index*2 + 1
        right_index = self.rightchild(i) # rightchild = index*2 + 2
        max_index = i
        
        # 만약 max_index의 값이(부모노드) 자식노드(left, right)보다 작으면
        if left_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index
        # 이제 max_index는 부모 노드와 자식 노드(두 개)를 비교한 값 중 가장 큰 값의 인덱스이다.
        if max_index != i: # 자기 자신이 아니면(부모 노드가 자식 노드보다 커서 변할 필요가 없는 경우가 아니면)
            self.swap(i, max_index)
            self.maxHeapify(max_index) # 재귀형태로 반복, 결국 부모 노드가 자식 노드보다 큰 값을 가지게 됨
            
    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]
        
    def parent(self, index):
        return (index-1) // 2
    
    def leftchild(self, index):
        return index*2 + 1
    def rightchild(self, index):
        return index*2 + 2
    def printHeap(self):
        print(self.queue)
```



# 나의 풀이

```python
# heapq는 우선순위 큐 알고리즘을 제공한다. 최소 힙의 형태로 원소가 정렬되며, 표준 모듈이다.
# heapq.heappush(heap, item): item을 heap에 추가
# heapq.heappop(heap): heap에서 가장 작은 원소를 pop(return도 함). 비어 있으면 indexError
# heapq.heapify(x): 리스트 x를 즉각적으로 heap으로 변환(O(N)의 시간복잡도)
# 사용시 기존 리스트를 힙처럼 사용할 것이 아니라면 heap = [] 처럼 빈 리스트를 만들고 내용을 heapq.~ 함수로 채워나가면 된다.
​
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
```

