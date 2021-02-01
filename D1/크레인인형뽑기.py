def solution(board, moves):

    dolls = []
    for move in moves:
        for raw in board:
            if raw[move-1]: #True면
                dolls.append(raw[move-1])
                raw[move-1] = 0
                break
    # dolls = 인형이 순서대로 들어감
    count = 0
    idx = 0
    while idx+1 < len(dolls):
        pre_order = 0
        for idx, doll in enumerate(dolls):
            if pre_order == doll:  #앞뒤 인형 비교
                del dolls[idx]     #같으면 앞뒤 인형 삭제하고
                del dolls[idx-1]
                count += 2         #카운트
                idx = 0  #순서 초기화
                break    #for 문 나가기 - while문 조건 확인
            else:
                pre_order = doll
    return count