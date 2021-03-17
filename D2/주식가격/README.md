# 주식 가격

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

##### 제한사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

##### 입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

##### 입출력 예 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.



### 문제 해결의 아이디어

---

스택을 잘 이용하면 해결 할 수 있을 것 같다.

스택을 만들어 주가의 맨 마지막 값을 pop하여 원래 순서대로 넣어주고, 그렇게 만들어진 나중 주식 가격의 리스트인 스택과 현재 주식 가격(prices의 맨 마지막 값)을 비교하여 가격이 떨어질 때 까지, 혹은 끝까지 세어가며 얼마나 오랜 시간동안 주가가 떨어지지 않았는지를 answer에 추가하였다.

```python
def solution(prices):
    answer = []
    stack = []
    while prices:
        tmp = 0  # answer에 넣을 값
        if stack:  # stack에 값이 있으면
            for value in stack:
                tmp += 1
                if prices[-1] <= value:  # 가격이 떨어지지 않았다면
                    pass
                else:
                    break  # 가격이 떨어졌으면
            stack = [prices.pop()] + stack
            answer = [tmp] + answer

        else:  # stack이 비어있으면
            answer.append(0)
            stack.append(prices.pop())

    return answer
```

이렇게 한 결과 정확성 테스트는 통과했지만 효율성 테스트는 단 하나도 통과하지 못하였다.

불필요한 부분을 제거한 결과는 다음과 같다.

```python
def solution(prices):
    answer = [0]
    stack = [prices.pop()] #초기값 설정
    while prices:
        tmp = 0  # answer에 넣을 값
        for value in stack:
            tmp += 1
            if prices[-1] > value:  # 가격이 떨어지지 않았다면
                break
        stack = [prices.pop()] + stack
        answer = [tmp] + answer

    return answer
```

이렇게 해도 효율성 테스트는 통과하지 못했다. 보다 근본적인 변화가 필요해 보였다.

pop을 사용하지 않고 인덱스를 이용해보기로 했다.

```python
def solution(prices):
    ans = []
    i = 0
    while i < len(prices)-1: #마지막 값은 무조건 0이므로 확인하지 않음
        j = i+1
        tmp = 1
        while j < len(prices)-1: # 현재 주가의 다음부터 확인
            if prices[i] <= prices[j]: # 주가가 떨어지지 않았다면
                j += 1
                tmp += 1
            else:
                break # 주가가 떨어졌다면 while문 종료, tmp를 결과에 추가
        ans.append(tmp)
        i += 1
    return ans + [0] # 마지막은 무조건 0
```

이렇게 코드를 작성한 결과 효율성 테스트를 통과할 수 있었다. 차이점이 뭘까? 스터디를 하면서 한번 알아봐야겠다.

