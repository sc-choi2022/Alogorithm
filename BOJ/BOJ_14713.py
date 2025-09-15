import sys

# 앵무새의 수 N
N = int(sys.stdin.readline())

# 앵무새가 말한 단어의 총 개수 answer
answer = 0

for _ in range(N):
    # 앵무새가 말한 문장 S
    S = sys.stdin.readline().rstrip()
