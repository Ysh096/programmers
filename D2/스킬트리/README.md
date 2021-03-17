# 스킬트리

##### 문제 설명

선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 `스파크 → 라이트닝 볼트 → 썬더`일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 `스파크 → 힐링 → 라이트닝 볼트 → 썬더`와 같은 스킬트리는 가능하지만, `썬더 → 스파크`나 `라이트닝 볼트 → 스파크 → 힐링 → 썬더`와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리[1](https://programmers.co.kr/learn/courses/30/lessons/49993#fn1)를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

##### 제한 조건

- 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
- 스킬 순서와 스킬트리는 문자열로 표기합니다.
  - 예를 들어, `C → B → D` 라면 "CBD"로 표기합니다
- 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
- skill_trees는 길이 1 이상 20 이하인 배열입니다.
- skill_trees의 원소는 스킬을 나타내는 문자열입니다.
  - skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

##### 입출력 예

| skill   | skill_trees                         | return |
| ------- | ----------------------------------- | ------ |
| `"CBD"` | `["BACDE", "CBADF", "AECB", "BDA"]` | 2      |

##### 입출력 예 설명

- "BACDE": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트립니다.
- "CBADF": 가능한 스킬트리입니다.
- "AECB": 가능한 스킬트리입니다.
- "BDA": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트리입니다.

------

# 나의 풀이

```python
def solution(skill, skill_trees):
    '''
    skill: 맞춰야 하는 스킬트리의 순서
    skill_trees: 사용자가 원하는 스킬트리 순서
    return: 스킬트리가 몇 개나 가능한가?
    '''
    minus = 0
    for user in skill_trees:
        stack = []
        for s in user:
            if s in skill:
                stack.append(s)
        while stack:
            last = stack.pop()
            last_idx = skill.find(last)
            if last_idx == 0 and len(stack) != 0: # C가 뽑혀 나왔으면 스택이 비어있어야 함
                minus += 1
                break
            elif last_idx == 0 and len(stack) == 0: # C가 뽑혀 나왔는데 스택이 비어있으면 그대로 종료
                break
            elif last_idx != 0 and len(stack) == 0: # 맨 처음 스킬이 아닌걸 뽑았는데 스택이 비어있으면
                minus += 1
                break
            elif skill[last_idx-1] != stack[-1]: # 이전 스킬이 옳지 않으면
                minus += 1
                break
    return len(skill_trees) - minus
```



처음에 한 생각이 다음과 같았다.

 1. skill에 들어있는 문자를 순서대로 스택에 쌓은 후, 나중에 확인할 때 바로 앞의 문자가 스택에 이미 존재하는지만 확인하면 되지 않을까? 존재하지 않는다면 불가능한 스킬트리임을 알려준다!

이를 그대로 구현해 본 것이 위의 코드인데, 뒤에서부터 읽으려고 하니 여러 가지 조건을 걸어줘야 했다. 결과적으로 문제는 풀 수 있었고, 시간도 그렇게 오래 걸리지는 않았지만, 좀 지저분하다는 느낌은 지울 수 없었다. 다른 사람의 풀이를 본 결과 허탈함을 살짝 느꼈다.

```python
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
```

뒤에서부터 비교해가느라 걸어주어야 했던 조건들은 앞에서부터 확인해가면 하나도 볼 필요 없는 것들이었다. 내가 뒤부터 본다는 생각에 지나치게 사로잡혀 아주 쉽게 풀 수 있는 문제를 약간 돌아서 푼 것 같다.



교훈! 뒤부터 확인할 때 뭔가 코드가 더러워진다면 앞부터 확인해보는건 어떨지??

