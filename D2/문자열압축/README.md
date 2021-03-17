# 문자열 압축

###### 문제 설명

데이터 처리 전문가가 되고 싶은 **"어피치"**는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- s의 길이는 1 이상 1,000 이하입니다.
- s는 알파벳 소문자로만 이루어져 있습니다.

##### 입출력 예

| s                            | result |
| ---------------------------- | ------ |
| `"aabbaccc"`                 | 7      |
| `"ababcdcdababcdcd"`         | 9      |
| `"abcabcdede"`               | 8      |
| `"abcabcabcabcdededededede"` | 14     |
| `"xababcdcdababcdcd"`        | 17     |

### 입출력 예에 대한 설명

**입출력 예 #1**

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

**입출력 예 #2**

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

**입출력 예 #3**

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

**입출력 예 #4**

문자열을 2개 단위로 자르면 "abcabcabcabc6de" 가 됩니다.
문자열을 3개 단위로 자르면 "4abcdededededede" 가 됩니다.
문자열을 4개 단위로 자르면 "abcabcabcabc3dede" 가 됩니다.
문자열을 6개 단위로 자를 경우 "2abcabc2dedede"가 되며, 이때의 길이가 14로 가장 짧습니다.

**입출력 예 #5**

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

---

# 나의 풀이

처음에는 딕셔너리를 이용하여 풀려고 했으나 반복되는 만큼 카운트하고 나면 붙어있지 않은 같은 문자까지 세어버리는 문제가 발생했다. 그래서 그냥 반복되는지 확인하고, 반복이 끝나면 바로 출력하도록 만들어 보았다.

```python
def solution(s):
    # 자른 구간 별 길이가 들어갈 리스트
    ans = []
	# 주어진 문자열이 길이 1인 경우 그냥 1 반환(test case5)
    if len(s) == 1:
        return 1
	#i = 확인해 볼 압축 단위(1, 2, ..., s길이의 절반까지)
    for i in range(1, len(s)//2 + 1):
		# i 단위로 자른걸 일렬로 늘어놓을 리스트
        tmp_list = []
        for j in range(0, len(s), i):
            tmp_list.append(s[j:j+i]) 
        # 나중에 loop를 돌 때 얘를 만나면 남은걸 tmp_str에 추가하고 loop가 종료됨
		tmp_list.append(0)
		
		# 반복 횟수를 셀 변수
        cnt = 1
		# 압축 길이별 최종 문자를 저장할 임시 변수
        tmp_str = ''
        for idx in range(len(tmp_list)-1):
            # 현재 값 == 다음 값이면 반복되는 것이므로 cnt+=1
			# 예를 들어 길이 1인 경우 tmp_list = ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c', 0]
            if tmp_list[idx] == tmp_list[idx+1]:
                cnt += 1
			# 현재 값 != 다음 값이고 cnt가 1이 아니면 숫자와 함께 추가
            elif tmp_list[idx] != tmp_list[idx+1] and cnt != 1:
                tmp_str += str(cnt) + tmp_list[idx]
                cnt = 1
			# 현재 값 != 다음 값이고 cnt = 1이면 문자만 추가
            else:
                tmp_str += tmp_list[idx]

        ans.append(len(tmp_str))
    return min(ans)
```

코드 자체는 어렵지 않지만, 영 깔끔하지 못한 것이 마음에 걸린다. 다른 사람의 코드를 참고해보자.



```python
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
```

가장 추천을 많이 받은 코드인데, 확실히 깔끔해 보이긴 하지만 가독성이 좀 떨어지는 것 같다. 내 코드도 그렇게 나쁘지는 않은 듯?