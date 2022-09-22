pic = [[0]*100 for _ in range(100)]

# 종이의 개수 N, 가려지는 기준 M
N, M = map(int, input().split())

# 보이지 않는 그림의 개수를 세는 cnt
cnt = 0

for _ in range(N):
    # 왼쪽 아래 모서리 좌표(x1, y1)와 오른쪽 위 모서리 좌표(x2, y2)
    x1, y1, x2, y2 = map(int, input().split())
    
    # 범위 안의 좌표에 종이의 개수를 저장
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            pic[i][j] += 1
            # 만약 M+1개가 되면 cnt 1증가
            if pic[i][j] == M+1:
                cnt +=1
# cnt 출력
print(cnt)