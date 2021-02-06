def solution(dartResult):
    dartResult = list(dartResult)
    L = len(dartResult)
    for i in range(L):
        try:
            dartResult[i] = int(dartResult[i]) #정수는 int형으로 바꿔주기
        except:
            pass

    R_dartResult = []
    k = 0
    while k < len(dartResult):
        if type(dartResult[k]) == int:
            if type(dartResult[k+1]) == int:
                R_dartResult.append(str(dartResult[k]) + str(dartResult[k+1]))
                R_dartResult[-1] = int(R_dartResult[-1])
                k += 2
            else:
                R_dartResult.append(dartResult[k])
                k += 1
        else:
            R_dartResult.append(dartResult[k])
            k += 1            
    #1. 처음은 dartResult[0]으로 시작.
    #2. 숫자를 만나거나 끝에 도달한 경우에 주의
    #3. 숫자인 경우 초기화 및 이전 것 저장
    answer = []
    L = len(R_dartResult)
    ans = R_dartResult[0]
    i = 1
    j = -1
    while i < L:
        val = R_dartResult[i]
        if type(val) == int:
            answer.append(ans)
            ans = val
            j += 1
        elif val == "S":
            ans = ans ** 1
        elif val == "D":
            ans = ans ** 2
        elif val == "T":
            ans = ans ** 3
        elif val == "*":
            ans = (ans) * 2
            try:
                answer[j] = answer[j] * 2
            except:
                pass
        elif val == "#":
            ans = ans * (-1)
        i += 1
    answer.append(ans)
    return sum(answer)


#모범 풀이
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


#모범 풀이2
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)