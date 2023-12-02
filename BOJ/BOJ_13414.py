import sys

# 수강가능 인원 K, 대기목록의 길이 L
K, L = map(int, sys.stdin.readline().split())
# 규칙에 따른 순서를 저장하는 딕셔너리 rule
rule = {}

for i in range(L):
    student = sys.stdin.readline().rstrip()
    rule[student] = i

lst = list(rule.items())
lst.sort(key=lambda x:x[1])

for accept in lst[:K]:
    print(accept[0])