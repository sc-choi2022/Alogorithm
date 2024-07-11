import sys

# 테스트 케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 한문장의 단어의 수 N
    N = int(sys.stdin.readline())
    # 공개키 PK1, PK2
    PK1 = sys.stdin.readline().rstrip().split()
    PK2 = sys.stdin.readline().rstrip().split()
    