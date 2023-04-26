from collections import defaultdict
import sys

def check():
    global cnt
    if alphabet['A'] >= A and alphabet['C'] >= C and alphabet['G'] >= G and alphabet['T'] >= T:
        cnt += 1

# 임의로 만든 DNA 문자열의 길이 S, 비밀번호로 사용할 부분문자열의 길이 P
S, P = map(int, sys.stdin.readline().split())

# 임의로 만든 DNA 문자열 DNA
DNA = sys.stdin.readline().rstrip()

# 부분문자열에 포함되어야 할 A, C, G, T의 최소 개수
A, C, G, T = map(int, sys.stdin.readline().split())
alphabet = defaultdict(int)
cnt = 0
for i in range(P):
    alphabet[DNA[i]] += 1
check()

for j in range(P, S):
    alphabet[DNA[j-P]] -= 1
    alphabet[DNA[j]] += 1
    check()
# 만들 수 있는 비밀번호의 종류의 수를 출력
print(cnt)