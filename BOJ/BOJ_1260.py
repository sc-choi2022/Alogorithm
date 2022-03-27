# DFS 함수
def DFS(arr):
    while stack:
        temp = stack[-1]
        for i in range(N + 1):
            if arr[temp][i] == 1 and i not in visited:
                stack.append(i)
                visited.append(i)
                break
        else:
            stack.pop()
    return visited
# BFS 함수
def BFS(arr):
    while queue:
        temp = queue.pop(0)

        for i in range(N + 1):
            if arr[temp][i] == 1 and i not in visit:
                queue.append(i)
                visit.append(i)
    return visit
# 정점의 개수 N, 간선의 개수 M, 시작할 정점의 번호 V
N, M, V= map(int, input().split())
# 정점의 정보를 담을 리스트 arr
arr = [[0]*(N+1) for _ in range(N+1)]

# M개의 간선 정보를 리스트 arr에 반영한다.
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# DFS를 위해 stack과 visited에 시작 정점 정보를 추가한다.
stack = [V]
visited = [V]
# DFS 함수의 return 한 visited 리스트의 값을 차례로 출력한다.
print(*DFS(arr))
# BFS를 위해 queue와 visit에 시작 정점 정보를 추가한다.
queue = [V]
visit = [V]
# BFS 함수의 return 한 visit 리스트의 값을 차례로 출력한다.
print(*BFS(arr))