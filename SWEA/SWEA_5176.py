import sys
sys.stdin = open('sample_input.txt')

def makeTree(n):
    global cnt
    print(n)
    # N까지의 자연수까지
    if n <= N:
        # 왼쪽노드는 현재 인덱스의 2배
        makeTree(n * 2)
        # 더이상 못가면 값넣고 cnt를 1 증가
        tree[n] = cnt
        print(n, tree)
        cnt += 1
        # 우측 노드는 인덱스 2배 + 1
        makeTree(n * 2 + 1)

T = int(input())
for case in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    # 이진 탐색트리에 처장할 첫 자연수 1
    cnt = 1
    # makeTree 함수에 노드의 root 번호 1을 넣어 시작
    makeTree(1)

    print(f'#{case} {tree[1]} {tree[N//2]}')