import sys
# PN의 정보 N
N = int(sys.stdin.readline())
# 문자열 S의 길이 M
M = int(sys.stdin.readline())
# 문자열 S
S = sys.stdin.readline().strip()

# 시작 위치와 PN의 N을 확인할 cnt, Pn의 포함 개수 ans
start, cnt, ans = 0, 0, 0

while start < (M - 1):
    # start:start+3의 위치가 IOI인 경우
    if S[start:start + 3] == 'IOI':
        # PN을 만드는 조건 성립으로 cnt 1 증가
        cnt += 1
        # 다음 IO을 확인하기 위해 start 2 증가
        start += 2
        # 만약 cnt가 N으로 PN이 완성되었다면 ans 1 증가하고 다음 2칸을 점프하기 때문에 cnt 1 감소
        if cnt == N:
            ans += 1
            cnt -= 1
    # IOI로 시작하지 않는 경우
    else:
        # start을 다음 위치로 지정하기 위해 start 1 증가 cnt 0으로 초기화
        start += 1
        cnt = 0
# S에 PN이 포함되어 있는 횟수 ans 출력
print(ans)