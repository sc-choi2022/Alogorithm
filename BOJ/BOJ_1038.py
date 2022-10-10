import sys
from itertools import combinations

N = int(sys.stdin.readline())
answer = []
# 최대 감소하는 수는 9876543210
for i in range(1, 11):
    for j in combinations(range(10), i):
        # 감소하는 수 순서로 리스트 생성
        number = sorted(list(j), reverse=True)
        # 각 수로 감소하는 수를 생성하여 answer에 추가
        answer.append(int(''.join(map(str, number))))
# 감소하는 수를 정렬
answer.sort()
# N번째 감소하는 수가 있는 경우 출력 없는 경우 -1을 출력
print(answer[N] if len(answer) > N else -1)