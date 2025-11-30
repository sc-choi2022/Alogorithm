import sys

# 암호문 S
S = sys.stdin.readline().rstrip()
# 사전에 있는 단어의 수 N
N = int(sys.stdin.readline())

words = [sys.stdin.readline().rstrip() for _ in range(N)]