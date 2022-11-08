import sys
# 주어지는 X
X = sys.stdin.readline().strip()

# 수의 앞에 0x이 주어진 경우 16진수
if X[:2] == '0x':
    print(int(X, 16))
# 수의 앞에 0이 주어진 경우 8진수
elif X[0] == '0':
    print(int(X, 8))
# 10진수인 경우
else:
    print(int(X))