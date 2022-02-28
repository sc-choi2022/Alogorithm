# 도화지의 한 변의 길이 N
N = 100
# 색종이의 한 변의 길이 K
K = 10

# 색종이 수 numb
numb = int(input())

# 도화지에 색종이가 겹치치 않은 상태를 나타낸 리스트 arr
arr = [[0]*100 for _ in range(100)]
# 색종이가 겹쳐진 곳의 수를 새는 cnt 초기화
cnt = 0

# 색종이 수만큼 for문 진행
for _ in range(numb):
    # 왼쪽의 사이 거리 L, 아래의 사이 거리 B
    L, B = map(int, input().split())
    # 아래의 사이 거리를 이용하여 행을 설정
    for i in range(N-B-1, N-B-K-1, -1):
        # 왼쪽의 사이 거리를 이용하여 열을 설정
        for j in range(L, L+K):
            # 색종이 부분을 arr에 표시
            arr[i][j] = 1
# 도화지 영역에 색종이가 겹쳐진 부분을 cnt 1 증가
for ii in range(100):
    for jj in range(100):
        if arr[ii][jj] == 1:
            cnt += 1
# cnt를 출력
print(cnt)