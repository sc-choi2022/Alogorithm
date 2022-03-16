import sys
sys.stdin = open('input.txt')

# 중위순회를 위한 함수 inorder
def inorder(a):
    if a <= N:
        # 왼쪽
        inorder(a*2)
        print(binary[a], end='')
        # 오른쪽
        inorder(a*2+1)

for case in range(1, 10+1):
    N = int(input())
    binary = [0] * (N + 1)

    for i in range(N):
        info = list(input().split())
        # 완전 이진 트리 형식으로 주어지기 때문에 info[1]의 값만을 사용
        binary[i+1] = info[1]
    # 테스트 케이스 번호 출력
    print(f'#{case} ', end='')
    # 이어서 중위순회를 1부터 시작하여 값을 출력
    inorder(1)
    print()