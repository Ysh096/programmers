def solution(strings, n):
    #n번째 문자 가져오기
    strings = sorted(strings)
    result = []
    for string in strings:
        pre_alpha = 'a' #e
        if string[n] >= pre_alpha:
            result = result + [string]            
        else:
            result = [string] + result
            
        pre_alpha = string[n]
        
    return print(result)

solution(['sun', 'bed', 'car'], 1)
