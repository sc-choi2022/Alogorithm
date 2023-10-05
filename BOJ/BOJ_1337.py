import sys

# 배열의 크기 N
N = int(sys.stdin.readline())
# 배열 lst
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])
start, answer = 0, 0

cnt = 0
for i in range(N):
    cnt += 1
    while numbers[i] - numbers[start] > 4:
        start += 1
        cnt -= 1
    answer = max(answer, cnt)
# 입력으로 주어진 배열이 올바른 배열이 되게 하기 위해서 추가되어야할 원소의 최소 개수를 출력
print(0 if answer > 5 else 5 - answer)