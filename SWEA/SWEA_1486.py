from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    # 점원의 명수 N, 선반의 높이 B
    N, B = map(int, input().split())
    # 점원들의 키들을 담을 리스트 height
    height = list(map(int, input().split()))
    # 모든 경우의 수에 대해 B와의 차이를 담을 리스트 answer
    answer = []
    # 점원의 명수에 따라 나오는 모든 경우의 수를 구한다.
    for i in range(1, N+1):
        result = list(combinations(height, i))
        # i명의 점원의 키로 만들 수 있는 모든 높이 중 B보다 같거나 큰 값이 있다면 그 차이를 ans에 추가
        for re in result:
            if sum(re)-B >= 0:
                answer.append(sum(re)-B)
    # 테스트 케이스 번호와 answer에 모든 값 중 가장 작은 값을 출력
    print(f'#{case} {min(answer)}')


def DFS(n, ssum):
    # 값을 갱신해 줄 sol
    global sol

    # N에 도착 전에 ssum - B이 sol보다 커지면 멈춘다.
    if ssum - B >sol:
        return

    # N에 도착하면
    if n == N:
        # ssum이 B보다 크거나 같고 ssum - B이 sol보다 작으면
        if ssum >= B and sol > ssum - B:
            # sol을 ssum - B로 저장
            sol = ssum - B
        return

    # lst의 다음 인덱스를 진행
    # ssum에 현재값을 반영
    DFS(n+1, ssum+lst[n])
    # ssum에 현재값 반영하지 않음
    DFS(n+1, ssum)

# 테스트케이스
T = int(input())
for case in range(1, T+1):
    # 점원의 인원 N, 선반의 높이 B
    N, B = map(int, input().split())
    # 점원들의 키의 합을 담을 리스트 lst
    lst = list(map(int, input().split()))
    sol = 100000

    # lst의 0번 인덱스에서 합이 0일 때부터 DFS 시작
    DFS(0, 0)

    print(f'#{case} {sol}')