import sys
sys.stdin = open('sample_input.txt')

def makeTree(n):
    global cnt
    # 자연수 N까지
    if n <= N:
        # 왼쪽 노드번호는 현재 노드번호*2
        makeTree(n * 2)
        # 더이상 못가면 값넣고 cnt를 1 증가
        tree[n] = cnt
        cnt += 1

        # 오른쪽 노드번호는 노드번호*2+1
        makeTree(n * 2 + 1)

T = int(input())
for case in range(1, T+1):
    N = int(input())
    # 1부터 N까지의 자연수를 담을 리스트 tree, 노드번호와 index를 맞추기 위해 N+1
    tree = [0]*(N+1)
    # 이진 탐색트리에 저장할 첫 자연수 1
    cnt = 1
    # makeTree 함수에 노드의 root 번호 1을 넣어 시작
    makeTree(1)
    # 테스트 케이스 번호, 루트에 저장된 값 tree[1], N/2번 노드의 값을 출력
    print(f'#{case} {tree[1]} {tree[N//2]}')