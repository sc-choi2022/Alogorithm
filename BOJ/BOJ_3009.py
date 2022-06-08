# X의 좌표를 담을 리스트
X = []
# Y의 좌표를 담을 리스트
Y = []

# 3개의 좌표 값
for _ in range(3):
    # 주어진 좌표 x, y
    x, y = map(int, input().split())
    # x와 y가 각각 X, Y에 포함 된 경우에는 X,Y에서 제거
    # 포함하지않는다면 추가
    if x in X:
        X.remove(x)
    else:
        X.append(x)

    if y in Y:
        Y.remove(y)
    else:
        Y.append(y)
# X[0], Y[0] 출력
print(X[0], Y[0])