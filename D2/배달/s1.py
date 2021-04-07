# def solution(N, road, K):
#     # <POINT>
#     # 경우에 따라, 이미 방문한 정점을 다시 갈 수도 있다!
#     # 노드 간의 거리가 다르기 때문에 depth가 깊더라도, 최단거리 일 수 있기 때문이다.
#     # 그렇다면 모든 정점을 재방문 해야하는가? 그렇지 않다.
#     # 최단거리를 갱신할 수 있는 경우에만 재방문 하고, 그때의 거리로 갱신한다.
#
#     # 인접행렬을 만들고, 값은 정점 사이의 거리로 지정
#     matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
#     # 인접 행렬 생성
#     for i in range(len(road)):
#         v, w, d = road[i][0], road[i][1], road[i][2] # 노드1, 노드2, 걸리는 시간
#         # 0인 경우 바로 값 넣기
#         if not matrix[v][w]:
#
#             matrix[v][w] = d
#             matrix[w][v] = d
#         # 여기까지는 같다.
#         # 예제에서 같은 정점인데 거리가 2번 이상 주어지는 경우, 작은값으로 넣기 위함
#         else:
#             if d < matrix[v][w]:
#                 matrix[v][w] = d
#                 matrix[w][v] = d
#     print(matrix)
#
#     # visit은 1번 정점과의 최단거리로 지정할 것이기 때문에 초기값은 큰 수를 지정함.
#     visit = [99999999999] * (N + 1)
#
#     # DFS, BFS 상관 X
#     que = [1]
#     visit[1] = 0
#
#     while que:
#         v = que.pop(0)
#         for i in range(len(matrix[v])):
#             # 연결되어 있고, 현재 방문 경로가 최단 거리인 경우
#             if matrix[v][i] and matrix[v][i] + visit[v] < visit[i]:
#                 if visit[v] + matrix[v][i] <= K:
#                     que.append(i)
#                     visit[i] = matrix[v][i] + visit[v]
#
#     result = 0
#     for i in range(len(visit)):
#         if visit[i] <= K:
#             result += 1
#
#     return result

#
# def solution(N, road, K):
#     answer = 0
#     graph = [[10001 for _ in range(N + 1)] for _ in range(N + 1)]
#     visited = [0] * (N + 1)
#     memo = [500001] * (N + 1)
#
#     # 2가지 이상 갈래 있을 경우 작은 것만 저장합니다.
#     for i in road:
#         if graph[i[0]][i[1]] >= i[2]:
#             graph[i[0]][i[1]] = i[2]
#             graph[i[1]][i[0]] = i[2]
#
#     # DFS로 모든 경로를 파악합니다.
#     def dfs(v, distance):
#
#         # 만일 거리가 K보다 커진다면 바로 리턴합니다.
#         if distance > K:
#             return
#
#         # 현재 위치보다 더 작은 값이 들어오게 되면 지정해줍니다.
#         if memo[v] > distance:
#             memo[v] = distance
#         # 더 크면 바로 리턴합니다.
#         else:
#             return
#
#         # 방문 처리를 해줍니다.
#         visited[v] = 1
#         for i in range(1, N + 1):
#             # 어떤 시간값이 들어있고, 방문하지 않았다면
#             if graph[v][i] < 10001 and visited[i] == 0:
#                 dfs(i, distance + graph[v][i])
#                 visited[i] = 0
#
#     dfs(1, 0)
#
#
#     for i in range(1, N + 1):
#         if memo[i] != 500001:
#             answer += 1
#
#     return answer

def get_min_idx(dists, visited, N):
    min_val = 987654321
    min_idx = 0
    for i in range(2, N + 1):
        if visited[i] == False: # 방문하지 않았으면
            if min_val > dists[i]:
                min_val = dists[i]
                min_idx = i
    return min_idx

def solution(N, road, K):
    answer = 0
    INF = 987654321
    graph = [[INF if i != j else 0 for j in range(N + 1)] for i in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    for info in road:
        graph[info[0]][info[1]] = min(graph[info[0]][info[1]], info[2])
        graph[info[1]][info[0]] = graph[info[0]][info[1]]

    dists = graph[1].copy()


    min_idx = get_min_idx(dists, visited, N)
    visited[min_idx] = True

    while min_idx:

        for i in range(1, N + 1):
            new_dist = dists[min_idx] + graph[min_idx][i]
            if dists[i] > new_dist:
                dists[i] = new_dist
        min_idx = get_min_idx(dists, visited, N)
        visited[min_idx] = True

    for i in range(1, N + 1):
        if dists[i] <= K:
            answer += 1
    return answer



road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
N = 5
K = 3

print(solution(N, road, K))
