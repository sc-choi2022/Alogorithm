# dfs를 활용한 방법
def dfs(permu):
    # cnt가 M개에 도달하면 permu를 출력 후 return
    if len(permu) == M:
        print(*permu)
        return
    # 1부터 N까지의 숫자에서
    for i in range(1, N+1):
        # permu안에 i가 없다면
        if i not in permu:
            # permu가 빈 배열이 아닐 때
            if permu:
                # 사전 순으로 증가하는 순서로 출력하기 위한 if문
                if max(permu) < i:
                    # i를 추가하고
                    permu.append(i)
                    # permu와 1 증가 시킨 cnt를 넣어 dfs로 보낸다
                    dfs(permu)
                    # permu에서 i를 제거
                    permu.pop()
            # permu가 빈 배열이라면 추가한다.
            else:
                # i를 추가하고
                permu.append(i)
                # permu와 1 증가 시킨 cnt를 넣어 dfs로 보낸다
                dfs(permu)
                # permu에서 i를 제거
                permu.pop()

# 1부터 N까지 M개를 고르기 위해 N, M이 주어진다.
N, M = map(int,input().split())

# 빈배열과 0개의 수로 dfs 실행
dfs([])