import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# queen이 들어갈 수 있는 자리인지 확인하는 함수 check
def check(x):
    for i in range(x):
        # x 위치에 queen을 놓았을 때 같은 줄에 존재하거나 대각선에 존재한다면
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            # queen을 놓을 수 없다.
            return False
        # queen을 x위치에 놓을 수 있다.
    return True

def dfs(x):
    global cnt
    # N-1까지 queen이 자리를 잡았다면
    if x == N:
        # 퀸을 놓는 방법 수 ans 1 증가
        cnt += 1
    else:
        # x번째 행에서 i의 열에 queen을 놓는다고 가정
        for i in range(N):
            row[x] = i
            # check 함수로 queen의 위치가 가능한 곳이었다면
            if check(x):
                # 다음 행의 queen의 위치를 찾으러 간다.
                dfs(x + 1)

for case in range(1, T+1):
    # NxN 행렬의 N
    N = int(input())
    # 각 행에서 queen의 열 위치를 담을 리스트 row
    row = [0]*N
    # 방법의 수 cnt 초기화
    cnt = 0
    # row의 0번 행렬부터 dfs 함수 실행
    dfs(0)
    # 테스트 케이스 수와 cnt 출력
    print(f'#{case} {cnt}')
