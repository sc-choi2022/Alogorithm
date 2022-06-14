def dfs(n, team1, team2):
    global ans

    # n번째 선수가 N번째 선수일때
    if n == N:
        # team1과 team2의 사람 수가 동일하면
        if len(team1) == len(team2):
            # team1와 team2의 능력치의 합 sum1와 sum2을 0으로 초기화하고
            sum1 = sum2 = 0
            # 모든 능력치를 sum1, sum2에 더해준다.
            for i in range(N//2):
                for j in range(N//2):
                    sum1 += S[team1[i]][team1[j]]
                    sum2 += S[team2[i]][team2[j]]
            # ans의 값은 ans와 sum1, sum2의 차이 중 작은 값으로 할당한다.
            ans = min(ans, abs(sum1 - sum2))
        return
    # n을 1증가 시키고, 두가지 경우로 dfs 재귀를 한다.
    # team1에 n을 추가했을 때
    dfs(n + 1, team1 + [n], team2)
    # team2에 n을 추가했을 때
    dfs(n + 1, team1, team2 + [n])

# 축구를 하는 N명
N = int(input())
# 능력치를 담은 리스트 S
S = [list(map(int, input().split())) for _ in range(N)]
ans = 1000

# 아직 선수가 배정되지 않은 상태 0, [], []으로 dfs 실행
dfs(0, [], [])
# 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력
print(ans)