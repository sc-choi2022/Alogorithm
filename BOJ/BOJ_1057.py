import sys

# 참가자의 수 N, 김지민의 번호 A, 임한수의 번호 B
N, A, B = map(int, sys.stdin.readline().split())
# 라운드 번호를 세는 cnt
cnt = 0

while A != B:
    A -= A//2
    B -= B//2
    cnt += 1
# cnt 출력
print(cnt)