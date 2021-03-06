# 다리를 지나는 트럭(lv2)

lv2 부터는 설명과 함께 코드를 작성해야겠다. 모든 문제가 알고리즘을 처음 접하는 나로써는 쉽지 않고, 다른 사람의 아이디어를 빌려 정리하는 수준으로 일단 해결해 보자.



### 문제

---

트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

| 경과 시간 | 다리를 지난 트럭 | 다리를 건너는 트럭 | 대기 트럭 |
| --------- | ---------------- | ------------------ | --------- |
| 0         | []               | []                 | [7,4,5,6] |
| 1~2       | []               | [7]                | [4,5,6]   |
| 3         | [7]              | [4]                | [5,6]     |
| 4         | [7]              | [4,5]              | [6]       |
| 5         | [7,4]            | [5]                | [6]       |
| 6~7       | [7,4,5]          | [6]                | []        |
| 8         | [7,4,5,6]        | []                 | []        |

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

##### 제한 조건

- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

##### 입출력 예

| bridge_length | weight | truck_weights                   | return |
| ------------- | ------ | ------------------------------- | ------ |
| 2             | 10     | [7,4,5,6]                       | 8      |
| 100           | 100    | [10]                            | 101    |
| 100           | 100    | [10,10,10,10,10,10,10,10,10,10] | 110    |

---



### 문제 해결의 아이디어

트럭이 움직이는 것을 pop을 이용해서 다들 표현을 했다. 스택보다는 큐 문제인듯(아직 큐를 안 배움)



1. 0을 다리 길이만큼 늘어놓은 리스트인 bridge = []*bridge_length 를 만들어준다. 
2. 마지막 항에 truck_weigths의 맨 앞을 pop해서 넣어준다.
3. 그럼 이 트럭이 다리에 올라간게 된다. 이제 이 트럭을 움직이면서 무게 측정도 해야 한다.
4. 트럭을 움직이는 방법으로, bridge의 맨 앞을 pop 해주는 방법이 있다. 그런데 이렇게 하면 다리의 길이가 달라지므로 맨 뒤에 계속해서 값을 추가해 줘야 하는데, 0을 넣을지, 트럭을 넣을지 결정해야 한다. 다리가 견딜 수 있는 하중을 넘지 않는다면 트럭을 넣어주고, 넘는다면 0을 넣어주면 된다.

큐에 익숙하지 않아 직접 생각해내진 못했지만, 아이디어만 보고 코드를 스스로 짜 보았다.

```python
def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    bridge[-1] = truck_weights.pop(0) # ---(1)
    time = 1
    while bridge: # 다리가 텅텅 빌 때 까지
        bridge.pop(0)
        time += 1
        if truck_weights: # 아직 더 건널 트럭이 있는 경우 ---(3)
            if sum(bridge) + truck_weights[0] <= weight:
                # 한계 하중을 넘지 않으면
                bridge.append(truck_weights.pop(0))
            else: # 한계 하중을 넘으면
                bridge.append(0) # ---(2)
        else:
            pass
    return time
```

파이참을 통해 디버깅을 두 번 정도 하고 나서 완성할 수 있었다. 

(1) 우선 다리를 다리 길이만큼 0으로 채워 넣고, 맨 마지막에 처음 들어갈 트럭을 넣고, 시간을 1로 초기화 해 놓았다.

(2) 그 다음 생각한 것은, pop을 통해 트럭을 한 칸씩 앞으로 옮겨주며, 동시에 뒤에 0 혹은 새로운 트럭을 들여놓는 방법이다. 가장 안쪽의 if문을 제일 먼저 작성하였고, bridge에 있는 트럭의 무게와 새롭게 들어가게 될 트럭의 무게가 한계 하중을 넘지 않으면 pop을 해서 새로운 트럭을 맨 뒤에 append 해주고, 한계 하중을 넘으면 pop을 하지 않고 그냥 0을 추가해 다리의 길이를 유지했다.



(3) 종료 조건이 아주 중요했다. 맨 처음에는 `while truck_weights:`를 써 보았는데, 이 경우 아직 다리에 있는 트럭이 끝까지 가지 않았더라도 대기 트럭이 없으면 함수가 종료되는 문제가 있었다. 당연한 것인데 디버깅 하기 전에는 알지 못했다.

 그 다음 시도한 것이 `while bridge:`인데, 이건 확신을 가지고 사용했다. pop을 계속해서 하면서, 뒤에 대기 트럭도 없게 된다면 결국 bridge는 []가 되어 while문이 []이 될 때 끝나게 될 것이었기 때문이다. 

 그런데 문제가 하나 발생했다. 대기 트럭이 없는 경우 truck_weights = []이 되고, truck_weights[0]에서 인덱스 에러가 발생하는 것이었다. 이를 해결하기 위해 truck_weights[0]을 하기 전에 if 문을 통해 truck_weights가 비어 있는지 확인하는 과정을 거쳤다. 비어 있다면 아무것도 하지 않고 pass 하도록 하여, while문을 다시 수행하도록 만들었다.

### 개선의 여지

---

 sum을 사용한 것이 마음에 걸려 수정해보았다.

```python
def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    bridge[-1] = truck_weights.pop(0)
    time = 1
    W = bridge[-1]
    while bridge: # 더 넣을 트럭이 없어질 때 까지
        W -= bridge[0] # 제거하는 대상만큼 무게가 가벼워짐 (0 또는 트럭의 무게)
        bridge.pop(0)
        time += 1
        if truck_weights:
            if W + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0)) # 한계 하중을 넘지 않으면
                W += bridge[-1] # 트럭이 들어오며 무게가 늘어남
            else: # 한계 하중을 넘으면
                bridge.append(0)
        else:
            pass
    return time
```

현재 무게를 저장하는 W라는 변수를 만들어 불필요한 sum을 제거하였다. 계산 횟수가 감소하였을 것이다.



개선 전!

| 테스트 1 〉  | 통과 (12.29ms, 10.2MB)   |
| ------------ | ------------------------ |
| 테스트 2 〉  | 통과 (1558.28ms, 10.1MB) |
| 테스트 3 〉  | 통과 (0.02ms, 9.98MB)    |
| 테스트 4 〉  | 통과 (334.02ms, 10.4MB)  |
| 테스트 5 〉  | 통과 (9619.40ms, 10.2MB) |
| 테스트 6 〉  | 통과 (1737.77ms, 10.2MB) |
| 테스트 7 〉  | 통과 (6.74ms, 10.1MB)    |
| 테스트 8 〉  | 통과 (0.35ms, 10.2MB)    |
| 테스트 9 〉  | 통과 (5.86ms, 10.3MB)    |
| 테스트 10 〉 | 통과 (0.44ms, 10.3MB)    |
| 테스트 11 〉 | 통과 (0.01ms, 10.1MB)    |
| 테스트 12 〉 | 통과 (0.44ms, 10.1MB)    |
| 테스트 13 〉 | 통과 (2.42ms, 10.3MB)    |
| 테스트 14 〉 | 통과 (0.02ms, 10.2MB)    |



개선 후!

| 테스트 1 〉  | 통과 (1.14ms, 10.3MB)   |
| ------------ | ----------------------- |
| 테스트 2 〉  | 통과 (46.70ms, 10.3MB)  |
| 테스트 3 〉  | 통과 (0.02ms, 10.3MB)   |
| 테스트 4 〉  | 통과 (10.78ms, 10.2MB)  |
| 테스트 5 〉  | 통과 (288.91ms, 10.2MB) |
| 테스트 6 〉  | 통과 (43.71ms, 10.3MB)  |
| 테스트 7 〉  | 통과 (3.02ms, 10.1MB)   |
| 테스트 8 〉  | 통과 (0.14ms, 10.3MB)   |
| 테스트 9 〉  | 통과 (3.09ms, 10.2MB)   |
| 테스트 10 〉 | 통과 (0.19ms, 10.3MB)   |
| 테스트 11 〉 | 통과 (0.01ms, 10.2MB)   |
| 테스트 12 〉 | 통과 (0.26ms, 10.3MB)   |
| 테스트 13 〉 | 통과 (1.15ms, 10.4MB)   |
| 테스트 14 〉 | 통과 (0.02ms, 10.1MB)   |

확실히 속도가 매우 빨라졌다!

