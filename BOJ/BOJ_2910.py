from collections import defaultdict
import sys

# 메시지의 숫자의 길이 N, 숫자의 기준 값 C
N, C = map(int, sys.stdin.readline().split())
# 메시지 수열을 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
cnt = defaultdict(int)

for number in numbers:
    cnt[number] += 1

cnt = list(cnt.items())
# 1. 빈도순대로 정렬
# 2. 등장하는 횟수가 같다면, 먼저 나온 것이 앞
cnt.sort(key=lambda x:(-x[1], numbers.index(x[0])))

# 입력으로 주어진 수열을 빈도 정렬한 다음 출력
for c in cnt:
    A, B = c
    for i in range(B):
        print(A, end=' ')