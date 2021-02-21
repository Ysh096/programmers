def solution(new_id):
    new_id_1= new_id.lower() #1단계
    new_id_2 = ''
    for cha in new_id_1:
        try:
            if cha == '-' or cha == '_' or cha == '.' or (ord(cha)>=97 and ord(cha)<=122) or int(cha) or cha == '0':
                new_id_2 += cha
        except ValueError:
            pass
    #2단계 완료
    count = 0
    new_id_3 = ''
    for cha in new_id_2:
        if cha == '.':
            count += 1
            if count == 1:  #.이 한번 나온 경우에만
                new_id_3 += cha #추가
            elif count > 2:     #2번 이상 나왔으면
                pass            #패스
        if cha != '.':          #.이 아닌 문자가 나오면
            count = 0           #count를 0으로 돌리고
            new_id_3 += cha     #문자를 더함
    #3단계 완료
    if new_id_3[0] == '.': #처음 문자가 .이면
        new_id_4 = new_id_3[1:] #슬라이싱
        try:
            if new_id_4[-1] == '.': #처음 문자가 .인 경우 -> 마지막 문자가 .이면
                new_id_4 = new_id_4[:-1] #또 슬라이싱
        except IndexError: #현재 new_id_4가 비어있는 경우
            pass
    elif new_id_3[-1] == '.': #마지막 문자가 .이면
        new_id_4 = new_id_3[:-1] #슬라이싱
    else:
        new_id_4 = new_id_3 #.이 없으면
    # new_id_4 = new_id_3.strip('.') #쉽게 할 수 있었음..
    #4단계 완료
    
    if new_id_4 == "":
        new_id_5 = "a"
    else:
        new_id_5 = new_id_4
    #5단계 완료
    if len(new_id_5) >= 16:
        new_id_6 = new_id_5[:15]
        if new_id_6[-1] == '.':
            new_id_6 = new_id_6[:-1]
    else:
        new_id_6 = new_id_5
    #6단계 완료
    if len(new_id_6) <= 2:
        new_id_7 = new_id_6 + new_id_6[-1]*2 #마지막 문자를 2개 추가하고
        #길이 1 -> 길이 3, 길이 2 -> 길이 4
        new_id_7 = new_id_7[:3]              #길이 3이 되도록 맞춤
    else:
        new_id_7 = new_id_6
    #7단계 완료
    return new_id_7