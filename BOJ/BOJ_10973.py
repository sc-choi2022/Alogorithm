import sys

# 순열을 이루는 수 N
N = int(sys.stdin.readline())
# 주어지는 순열 permutation
permutation = list(map(int, sys.stdin.readline().split()))

for i in range(N-1, 0, -1):
    if permutation[i] < permutation[i-1]:
        for j in range(N-1, 0, -1):
            if permutation[i-1] > permutation[j]:
                permutation[i-1], permutation[j] = permutation[j], permutation[i-1]
                # 사전순으로 이전 순열의 앞 순열을 permutation에 저장 후 출력
                permutation = permutation[:i] + sorted(permutation[i:], reverse=True)
                print(*permutation)
                # 종료
                exit()
# 사전순으로 가장 처음에 오는 순열인 경우 -1 출력
print(-1)