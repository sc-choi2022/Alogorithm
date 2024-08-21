import sys

# 나무의 개수 N
N = int(sys.stdin.readline())
# 첫날 나무들의 길이를 저장하는 배열 H
H = list(map(int, sys.stdin.readline().split()))
# 나무들이 자라는 길이를 저장하는 배열 A
A = list(map(int, sys.stdin.readline().split()))
trees = sorted(list(map(list, zip(H, A))), key=lambda x:x[1])

# 나무를 잘라서 구할 수 있는 최대 양 answer
answer = 0
for i in range(N):
    answer += trees[i][0] + (i * trees[i][1])

# answer을 출력
print(answer)