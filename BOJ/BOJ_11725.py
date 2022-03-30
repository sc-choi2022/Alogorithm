N = int(input())

# 시작 노드부터 시작하는 dfs
def dfs(root):
    # stack에 시작노드 추가
    stack= [root]
    # stack이 비어있게 될 때까지
    while stack:
        # 부모노드
        temp = stack.pop()
        # 트리의 부모노드에 연결된 노드들에서
        for i in tree[temp]:
            # 부모노드가 아닌 것 노드가 있다면
            if visited[i] == 0:
                # 자식노드의 위치에 부모노드를 저장
                visited[i] = temp
                # 스택에 자식노드 추가
                stack.append(i)
# 일차원 배열로 tree의 정보를 담는 리스트 tree
tree = [[] for _ in range(N+1)]
# 자식노드의 번호를 인덱스로 부모의 노드를 담을 리스트 visited
visited= [0]*(N + 1)

# N-1개의 트리의 연결정보를 tree에 반영
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 1번 노드를 시작노드로 dfs 함수 실행
dfs(1)
# 2번째 노드부터 부모노드를 각 줄에 출력
for p in range(2, len(visited)):
    print(visited[p])