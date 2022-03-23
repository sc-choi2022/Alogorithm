import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T + 1):
    # 노드의 개수 N, 리프 노드의 개수 M, 출력할 노드의 번호 L
    N, M, L = map(int, input().split())

    # 트리를 노드의 번호에 맞춰 담을 리스트 tree
    tree = [0] * (N + 1)
    # M개의 리프 노드의 정보를 tree에 추가
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    for i in range(N, 0, -1):
        # 부모 노드에 자신의 값을 더한다.
        tree[i//2] += tree[i]

    # 테스트 케이스 번호와 출력 노드의 값을 출력
    print(f'#{case} {tree[L]}')