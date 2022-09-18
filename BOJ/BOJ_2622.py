import sys

# 성냥개비 개수 N
N = int(sys.stdin.readline())

# 출력할 삼각형의 개수
ans = 0
# 가장 짧은 삼각형 변의 길이 a
for a in range(1, N//3+1):
    # 두번째로 짧은 삼각형 변의 길이 b
    for b in range(a, (N-a)//2+1):
        # 가장 긴 변의 길이 c
        c = N - a - b
        # a + b > c인 경우 삼각형이 성립하므로 ans 1증가
        if a + b > c:
            ans += 1
# ans 출력
print(ans)