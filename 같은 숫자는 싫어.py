def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(4):
        if arr[i] == arr[i+1]:
            del arr[i]
    answer = arr
    return answer

answer = solution([1, 1, 3, 3, 0, 1, 1])
print(answer)
