from itertools import combinations
import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 학생의 수 N
    N = int(sys.stdin.readline())
    # 학생들의 MBTI를 저장하는 배열 mbti
    mbti = list(sys.stdin.readline().rstrip().split())

    if N > 32:
        print(0)
    else:
        # 심리적인 거리 answer
        answer = 12
        # 심리적인 거리를 구하는 세명의 경우의 수를 저장하는 배열 cases
        cases = list(combinations(mbti, 3))

        for A, B, C in cases:
            tmp = 0
            for i in range(4):
                tmp += int(A[i] != B[i]) + int(B[i] != C[i]) + int(C[i] != A[i])
            answer = min(answer, tmp)
        # 가장 가까운 세 학생 사이의 심리적인 거리 출력
        print(answer)