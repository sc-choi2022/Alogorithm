# dfs를 활용하기 위해 함수 dfs 정의
# idx번째 직원, 확률을 value로 설정하여 dfs
def dfs(idx, value):
    # 변수 ans의 값을 변경하기 위해 global 선언
    global ans

    # N번째 직원까지 일 배정이 완료되었다면 ans와 비교하여 max값이 ans가 된다.
    if idx == N:
        ans = max(ans, value)
        return

    # 확률은 언제나 1보다 작으므로 도중에 ans의 값보다 같거나 작다면
    # 더 커질 수 없다.
    if ans >= value:
        return

    # N명의 직원에게 i번째 일을 할당하기 위한 for문
    for i in range(N):
        # i번째 일이 할당되지 않았다면
        if visited[i] == 0:
            # i번째 일이 할당되었다는 표시를 하고
            visited[i] = 1
            # idx+1번째 직원, 새로 만들어진 value를 넣어 dfs를 돌린다.
            dfs(idx + 1, value*lst[idx][i] * 0.01)
            # i번재 일의 할당 여부를 초기화
            visited[i] = 0

# 테스트 케이스 개수
T = int(input())

for case in range(1, T + 1):
    # 일의 수, 직원의 인원 N
    N = int(input())
    # 각 직원의 일에 따른 성공확률을 담을 리스트 lst
    lst = [list(map(int, input().split())) for _ in range(N)]
    # idx번째 일이 할당 되었는지 확인하기 위한 리스트 visited
    visited = [0 for _ in range(N)]
    # 출력할 최대 확률 값 ans
    ans = 0
    # 0번째 직원부터 일을 배정받고 확률을 구할 기본 값을 1로 설정하여 dfs
    dfs(0, 1)

    # 출력 조건에 맞게 최대 성공확률을 출력
    print('#{} {}'.format(case, format(ans * 100, '.6f')))