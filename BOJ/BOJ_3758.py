import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 팀의 개수 N, 문제의 개수 K, ID을 의히마는 ID, 엔트리의 개수 M
    N, K, ID, M = map(int, sys.stdin.readline().split())
    # 테스트에 결과를 저장하는 result
    result = {}

    for i in range(M):
        # 팀의 번호 num, 문제 번호 no, 획득한 점수 s
        num, no, s = map(int, sys.stdin.readline().split())
        if num not in result:
            result[num] = [0]*(K+3)
            result[num][no] = s
            result[num][K+1], result[num][K+2] = i, 1
        else:
            result[num][no] = max(result[num][no], s)
            result[num][K+1] = i
            result[num][K+2] += 1
    # 순위의 기준이 되는 정보를 저장하는 배열 ranking
    ranking = list(result.items())
    ranking.sort(key=lambda x: (-sum(x[1][:K+1]), x[1][K+2], x[1][K+1]))

    for j in range(N):
        # 팀의 순위를 찾은 경우 출력
        if ranking[j][0] == ID:
            print(j+1)
            break