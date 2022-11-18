from collections import defaultdict
import sys

# 주어지는 단어 S
S = sys.stdin.readline().strip()

# 딕셔너리 alphabet 생성
alphabet = defaultdict(int)

# 알파벳 소문자를 key로 alphabet에 저장
for i in range(97, 123):
    alphabet[chr(i)]

# 주어지는 단어의 각 알파벳의 개수를 alphabet에 반영
for s in S:
    alphabet[s] += 1

# alphabet의 value를 출력
print(*alphabet.values())