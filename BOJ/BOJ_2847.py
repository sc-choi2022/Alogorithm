import sys

# 레벨의 수 N
N = int(sys.stdin.readline())
# 레벨의 점수를 담은 배열 numbers
numbers = [int(sys.stdin.readline()) for _ in range(N)]
# 최소 감소 횟수 answer
answer = 0

for i in range(N-2, -1, -1):
    if numbers[i] >= numbers[i+1]:
        answer += numbers[i] - (numbers[i+1] - 1)
        numbers[i] = numbers[i+1] - 1
# 점수를 몇 번 감소시키면 되는지 출력
print(answer)