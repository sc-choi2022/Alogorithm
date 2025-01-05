import sys

# 정점의 개수 N
N = int(sys.stdin.readline())
# 트리에 속한 정점의 연결 개수를 저장하는 배열 tree
tree = [0] * (N+1)

for _ in range(N-1):
    # 간선의 정보 a, b
    a, b = map(int, sys.stdin.readline().split())
    tree[a] += 1
    tree[b] += 1

# 질의의 개수 Q
Q = int(sys.stdin.readline())

for _ in range(Q):
    # 질의 t, k
    t, k = map(int, sys.stdin.readline().split())

    if t == 1:
        # 단절점인 경우
        if tree[k] > 1:
            print('yes')
        # 단절점이 아닌 경우
        else:
            print('no')
    else:
        # 반드시 단절선이므로 yes 출력
        print('yes')