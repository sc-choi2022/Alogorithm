import sys

def function(X, Y, W):
    h1 = (X**2 - W**2)**0.5
    h2 = (Y**2 - W**2)**0.5
    C = h1 * h2 / (h1 + h2)
    return C

# 주어지는 사다리의 길이 X, Y와 두 사다리가 교차하는 높이 C
X, Y, C = map(float, sys.stdin.readline().split())
# 두 빌딩사이에 너비를 찾는 범위 S, E
S, E = 0, min(X, Y)
# 두 빌딩사이에 너비가 되는 수치 result
result = 0

# 오차가 10**-3까지 허용
while E-S > 0.001:
    M = (S+E)/2

    if function(X, Y, M) >= C:
        result = M
        S = M
    else:
        E = M

# result을 출력
print(result)