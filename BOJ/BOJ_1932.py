# 삼각형의 크기 n
n = int(input())

# 삼각형의 숫자들을 담을 리스트 triangle
triangle = []

# 리스트 triangle에 값 추가하기
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 삼각형의 가장 아래층부터 시작하여 합이 최대가 되는 경로에 있는 수의 합울 구하려 한다.
for i in range(n-1, 0, -1):
    for j in range(len(triangle[i]) - 1):
        # triangle[i-1][j]층은 현재 위치에서
        # 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중 큰 값을 더해 준다.
        triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

# 가장 꼭대기 층의 값을 출력한다.
print(triangle[0][0])