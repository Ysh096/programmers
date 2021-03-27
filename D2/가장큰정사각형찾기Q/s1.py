def solution(board):
    N = len(board) # row 길이
    M = len(board[0]) # column 길이
    result = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                for k in range(1, min(N-i, M-j)):
                    # 바로 밑과 옆 행, 열 확인
                    row = board[i+k]
                    if 0 in row[j:j+k+1]:
                        area = k ** 2
                        result.append(area)
                        break
                    for row in range(i, i+k+1):
                        if board[row][j + k] == 0:
                            area = k ** 2
                            result.append(area)
                            break
                    area = (k+1) ** 2
                    result.append(area)
    return max(result)


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
# board = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))