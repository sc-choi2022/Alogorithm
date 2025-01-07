import sys
# 장소의 수 N
N = int(sys.stdin.readline())
# 장소들의 꿀의 양을 저장하는 배열 H
H = list(map(int, sys.stdin.readline().split()))
# 배열 H의 누적합을 저장하는 배열 S
S = H[::]
# 가능한 최대의 꿀의 양 result
result = 0

for i in range(1, N):
    S[i] += S[i-1]

# 벌통의 위치가 N-1인 경우
# 한 마리의 벌의 위치는 0으로 고정
# 다른 한 마리의 벌의 위치 j
for j in range(1, N-1):
    result = max(result, 2*S[N-1]-H[0]-H[j]-S[j])

# 벌통의 위치가 0인 경우
# 한 마리의 벌의 위치는 N-1으로 고정
# 다른 한 마리의 벌의 위치 k
for k in range(1, N-1):
    result = max(result, S[N-1]-H[N-1]-H[k]+S[k-1])

# 벌통의 위치가 중앙인 경우
# 두 마리의 벌의 위치는 0과 N-1로 고정
# 벌통의 위치 l
for l in range(1, N-1):
    result = max(result, S[l]-H[0]+S[N-1]-S[l-1]-H[N-1])

# result 출력
print(result)