import sys
# 주어지는 X, Y
X, Y = sys.stdin.readline().strip().split()
# 변수 X, Y에 Rev(X), Rev(Y)을 저장
X, Y = int(X[::-1]), int(Y[::-1])
# 변수 ans에 Rev(X) + Rev(Y)값을 저장
ans = str(X + Y)
# Rev(ans) Rev(Rev(X) + Rev(Y))을 출력
print(int(ans[::-1]))