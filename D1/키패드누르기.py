def solution(numbers, hand):
    answer = ''
    keypad_row = {'1': '123', '2': '456', '3':'789', '4': '*0#'}
    keypad_col = {'1': '147*', '2': '2580', '3': '369#'}
    #기본 손위치
    L = '*'
    R = '#'
    L_row = 0
    L_col = 0
    R_row = 0
    R_col = 0
    number_row = 0
    number_col = 0
    numbers = [str(num) for num in numbers]
    for number in numbers:
        if number in '147':
            answer += 'L'
            L = number
        elif number in '369':
            answer += 'R'
            R = number
        else: #number in '2580'
            for key_row, val in keypad_row.items():
                if number in val:
                    number_row = int(key_row)
                if L in val:
                    L_row = int(key_row)
                if R in val:
                    R_row = int(key_row)

            for key_col, val in keypad_col.items():
                if number in val:
                    number_col = int(key_col)
                if L in val:
                    L_col = int(key_col)
                if R in val:
                    R_col = int(key_col)
            #모든 위치를 구함
            if abs(number_row-L_row) + abs(number_col-L_col) == abs(number_row-R_row) + abs(number_col-R_col):
                answer += hand[0].upper()
                if hand[0].upper() == 'R':
                    R = number
                else:
                    L = number
            elif abs(number_row-L_row) + abs(number_col-L_col) > abs(number_row-R_row) + abs(number_col-R_col):
                answer += 'R'
                R = number

            else:
                answer += 'L'
                L = number

    return answer


# 다른 사람 풀이
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer