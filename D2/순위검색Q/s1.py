def solution(info, query):
    candis = [] # 지원자 조건
    tmp_condis = []
    condis = [] # 분류 조건
    for cand in info:
        candis.append(cand.split())
    for cond in query:
        tmp_condis = []
        for tmp_cond in cond.split():
            if tmp_cond == 'and':
                continue
            tmp_condis.append(tmp_cond)
        condis.append(tmp_condis)
    # condis 에는 원하는 지원자의 조건만 넣어놓았음.
    # candis 에는 지원자의 조건만 넣어놓았음.
    result = []
    for cond in condis:
        '''
        cond example = ['java', 'backend', 'junior', 'pizza', '100']
        '''
        cnt = 0
        for cand in candis:
            if int(cond[-1]) <= int(cand[-1]):
                for i in range(0, 4):
                    if cond[i] == cand[i] or cond[i] == '-':
                        pass
                    else:
                        break
                    if i == 3:
                        cnt += 1
        result.append(cnt)
    return result

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

print(solution(info, query))