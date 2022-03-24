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