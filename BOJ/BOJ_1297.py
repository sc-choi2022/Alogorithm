import sys

# TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W
D, H, W = map(int, sys.stdin.readline().split())

# 배수 number
number = (D**2/(H**2+W**2))**0.5
# TV의 높이와 TV의 너비 출력
print(int(H*number), int(W*number))