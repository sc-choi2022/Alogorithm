from itertools import combinations
import sys, math
# 테스트케이스 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 수의 개수 N과 N개의 수를 담은 배열 numbers
    numbers = list(map(int, sys.stdin.readline().split()))
    # N개의 수로 combination을 구하여 coms로 저장
    coms = list(combinations(numbers[1:], 2))
    # 모든 쌍의 GCD의 합을 더할 변수 ans을 0으로 초기화
    ans = 0

    # 모든 쌍의 GCD을 ans에 더한다.
    for com in coms:
        ans += math.gcd(*com)
    # ans 출력
    print(ans)