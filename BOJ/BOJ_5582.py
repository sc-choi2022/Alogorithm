import sys

# 문자열1, 문자열2인 string1, string2
string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()

# dp
dp = [[0]*(len(string2) + 1) for _ in range(len(string1) + 1)]
