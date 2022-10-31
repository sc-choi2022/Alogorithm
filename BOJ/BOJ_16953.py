import sys
# B를 만드는데 필요한 연산의 수를 구하는 함수 dfs
def dfs(number, cnt):
    global ans
    # number가 B인 경우
    if number == B:
        # cnt와 ans 중 min값을 ans에 저장 후 return
        ans = min(cnt, ans)
        return
    # number의 값이 B보다 커지면 return
    if number > B:
        return
    # 2를 곱하는 연산
    dfs(number * 2, cnt + 1)
    # 1의 수의 가장 오른쪽에 추가하는 연산
    dfs(number * 10 + 1, cnt + 1)

# 정수 A, B
A, B = map(int, sys.stdin.readline().split())
# 출력할 연산의 최솟값 ans
ans = 1000000000

# 연산의 첫 값 A와 연산 횟수 0으로 dfs을 실행
dfs(A, 0)
# 만들 수 없는 경우에는 -1을 출력
if ans == 1000000000:
    print(-1)
else:
    # 연산의 최솟값에 1을 더한 값을 출력
    print(ans + 1)