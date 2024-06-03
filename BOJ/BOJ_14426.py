import sys

# Method 1

# 문자열의 개수 N, 입력으로 주어지는 문자열의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 집합 S에 포함되어 있는 문자열을 저장하는 배열 S
S = sorted(list(sys.stdin.readline().rstrip() for _ in range(N)))
# 검사해야하는 문자열을 저장하는 배열 C
C = sorted(list(sys.stdin.readline().rstrip() for _ in range(M)))
# 포함되는 접두사의 개수 answer
answer = 0
idx = 0

while C:
    prefix = C.pop(0)
    # 더이상 접두사가 없는 경우 break
    if prefix > S[-1]:
        break
    # 접두사 후보의 길이 L
    L = len(prefix)
    for i in range(idx, N):
        if prefix == S[i][:L]:
            idx = i
            answer += 1
            break

# answer 출력
print(answer)

# Method 2

# 문자열의 개수 N, 입력으로 주어지는 문자열의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 집합 S에 포함되어 있는 문자열을 저장하는 배열 S
S = sorted(list(sys.stdin.readline().rstrip() for _ in range(N)))
# 검사해야하는 문자열을 저장하는 배열 C
C = sorted(list(sys.stdin.readline().rstrip() for _ in range(M)))
# 포함되는 접두사의 개수 answer
answer = 0
# 접두사를 확인하는 문자열의 위치 idxS, idxC
idxS, idxC = 0, 0

while idxS < N and idxC < M:
    # 접두사가 맞는 경우
    if S[idxS][:len(C[idxC])] == C[idxC]:
        answer += 1
        idxC += 1
    # 다음 접두사 후보를 확인해야하는 경우
    elif S[idxS] > C[idxC]:
        idxC += 1
    # 다음 문자열을 확인해야하는 경우
    elif S[idxS] < C[idxC]:
        idxS += 1

# answer을 출력
print(answer)