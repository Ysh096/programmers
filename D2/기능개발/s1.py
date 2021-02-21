def calculation(progresses, speeds, day):
    if progresses != []:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]*day
        return progresses
    else:
        return []

def solution(progresses, speeds):
    result = []
    #맨 앞에 있는 숫자를 100으로 만든 후에 나머지 숫자를 확인하자.
    while progresses != []: #빈 리스트가 되지 않는 한에서
        prior = progresses.pop(0)
        speed = speeds.pop(0)
        v, r = divmod(100-prior, speed)
        if r > 0:
            day = v + 1 #day = 첫 번째 기능이 완성되는 데 걸리는 시간
            #나머지는 하루 있다가 처리하는 것.. 처음에 day = v+r로 계산했다가 2, 4, 11번 테스트케이스에서 실패했었음.
            #나머지 테케에서는 맞은게 의문이다.
        else:
            day = v
        cnt = 1 #일단 하나의 기능은 배포한다.
        #이 때 나머지 기능들의 상태는?
        remain_states = calculation(progresses, speeds, day)
        #만약 0번째 이후부터 연속적으로 100 이상의 값을 가지면, 100미만 값이 나올 때 까지 배포
        while remain_states != []: #비어 있지 않은 경우
            if remain_states[0] >= 100:
                remain_states.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break # 완성도가 100 미만인 경우
        result.append(cnt)
    return result


# progresses = [40, 93, 30, 55, 60, 65]
# speeds = [60, 1, 30, 5, 10, 7]
# result = [1, 2, 3]
# progresses = [93, 30, 55, 60, 40, 65]
# speeds = [1, 30, 5, 10, 60, 7]
# result2 = [2, 4]
# progresses=[93, 30, 55, 60]
# speeds = [1, 30, 5, 40]
# result = [2, 2]
# progresses = [99, 99, 99, 99, 99]
# speeds = [3, 3, 3, 3, 3]
# result = [5]
progresses = [1, 1, 1, 1]
speeds = [100, 50, 34, 25]
result = [1, 1, 1, 1]


ans = solution(progresses, speeds)
print(ans)