import sys

# 문자열 S
S = sys.stdin.readline().rstrip()
# 문자열 S의 길이, S의 a의 개수 A
L, A = len(S), S.count('a')
# 문자열이 이어진 것을 표현하기 위해 문자열 S 두개를 이어준다.
S = S + S
# A 길이의 구간에 b의 개수
cnt = S[:A].count('b')
# 필요한 교환의 회수의 최솟값 answer
answer = cnt
for i in range(L):
    answer = min(answer, cnt)
    if S[i] == 'b':
        cnt -= 1

    if S[A+i] == 'b':
        cnt += 1
# 필요한 교환의 회수의 최솟값을 출력
print(answer)