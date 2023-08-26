def dfs(current, target, visited, graph, length):
    if current == target:
        return length
    visited[current] = True
    max_length = 0
    for next_node, weight in graph[current]:
        if not visited[next_node]:
            max_length = max(max_length, dfs(next_node, target, visited, graph, length + weight))
    visited[current] = False
    return max_length

def solve(N, M, roads):
    graph = [[] for _ in range(N)]
    for a, b, c in roads:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))

    max_length = 0
    for i in range(N):
        for j in range(i+1, N):
            visited = [False] * N
            max_length = max(max_length, dfs(i, j, visited, graph, 0))
    return max_length

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
print(solve(N, M, roads))
