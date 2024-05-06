import sys

# 자연수의 개수 N, 선택하는 개수 K
N, K = map(int, sys.stdin.readline().split())
# N개의 자연수를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 고른 수를 저장하는 choice
choice = []

for _ in range(K):
    idx = numbers.index(max(numbers))
    choice.append((idx, numbers[idx]))
    numbers[idx] = 0
choice.sort(key=lambda x:x[0])

# 주어진 N개의 수 중 K개의 수를 고를 때, 전체점수의 최댓값 answer
answer = 0
for i in range(K):
    answer += choice[i][1] - i

# answer 출력
print(answer)