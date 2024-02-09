from collections import defaultdict
import sys

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 D, 연속해서 먹는 접시의 수 K, 쿠폰 번호 C
N, D, K, C = map(int, sys.stdin.readline().split())
# 벨트에 올려져 있는 회전 초밥의 정보를 저장하는 배열 sushi
sushi = [int(sys.stdin.readline()) for _ in range(N)]
# 연속해서 먹는 접시에 있는 초밥의 종류를 저장하는 딕셔너리 plate
plate = defaultdict(int)

# 손님이 먹을 수 있는 초밥 가짓수의 최댓값 answer
answer = 0

# 구간 인덱스 초기화
left, right = 0, K-1
# plate의 초기 조건, 쿠폰 번호 초밥과 첫 구간 인덱스의 초밥 종류를 plate에 저장
plate[C] += 1
for i in range(left, right+1):
    plate[sushi[i]] += 1

while left < N:
    answer = max(answer, len(plate))

    # 구간 재정의 후 plate 반영
    left += 1
    right += 1

    plate[sushi[left-1]] -= 1
    if not plate[sushi[left-1]]:
        del plate[sushi[left-1]]
    plate[sushi[right%N]] += 1

# 주어진 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값을 하나의 정수로 출력
print(answer)