import sys

def sol(x, y, N):
    global cnt0, cnt1
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 현재 종이의 색이 다른 경우
            if color != paper[i][j]:
                sol(x, y, N//2)
                sol(x, y + N//2, N//2)
                sol(x + N//2, y, N//2)
                sol(x + N//2, y + N//2, N//2)
                return

    # 해당 색종이의 개수를 저장
    if color == 0:
        cnt0 += 1
    else:
        cnt1 += 1

# 종이의 한 변의 길이 N
N = int(sys.stdin.readline())
# 색종이의 색의 저장하는 배열 paper
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
# 하얀색의 개수 cnt0, 파란색의 개수 cnt1
cnt0, cnt1 = 0, 0

sol(0, 0, N)

# 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력
print(cnt0)
print(cnt1)