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
            parent_index = self.parent(last_index)  # 부모 노드의 인덱스 구하기
            # 부모 노드의 값이 추가한 인덱스보다 작으면(자식 노드보다 작으면)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)  # 자식 노드와 부모 노드의 value를 교환!
                last_index = parent_index  # 인덱스를 부모 노드의 위치로 변경
                # 부모 노드의 인덱스는 신경쓰지 않아도 됨! self.parent를 통해 구하기 때문에
            # 부모 노드가 자식 노드보다 큰 값을 가지면
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index)  # pop()을 쓰기 위해 0자리(최댓값)와 끝자리(최솟값)의 값을 바꿔줌
        maxv = self.queue.pop()  # 아마 pop(0)보다 효율적이라 이걸로 쓰는듯?
        self.maxHeapify(0)  # 뭔지 밑에서 살펴보자.
        return maxv

    # 임시 root부터 자식들과 값을 비교해나가며 재정렬하는 함수
    def maxHeapify(self, i):
        left_index = self.leftchild(i)  # leftchild = index*2 + 1
        right_index = self.rightchild(i)  # rightchild = index*2 + 2
        max_index = i

        # 만약 max_index의 값이(부모노드) 자식노드(left, right)보다 작으면
        if left_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index
        # 이제 max_index는 부모 노드와 자식 노드(두 개)를 비교한 값 중 가장 큰 값의 인덱스이다.
        if max_index != i:  # 자기 자신이 아니면(부모 노드가 자식 노드보다 커서 변할 필요가 없는 경우가 아니면)
            self.swap(i, max_index)
            self.maxHeapify(max_index)  # 재귀형태로 반복, 결국 부모 노드가 자식 노드보다 큰 값을 가지게 됨

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def parent(self, index):
        return (index - 1) // 2

    def leftchild(self, index):
        return index * 2 + 1

    def rightchild(self, index):
        return index * 2 + 2

    def printHeap(self):
        print(self.queue)

if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(1)
    mh.printHeap()
    mh.insert(3)
    mh.printHeap()
    mh.insert(11)
    mh.printHeap()
    mh.insert(6)
    mh.printHeap()
    mh.insert(5)
    mh.printHeap()
    mh.insert(2)
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()