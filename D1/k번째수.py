def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0] -1
        j = command[1]
        k = command[2] -1
        a = sorted(array[i:j])
        answer.append(a[k])
    return answer