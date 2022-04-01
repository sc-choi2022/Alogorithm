def dfs(idx, cnt):
    global answer
    # cnt 값이 answer보다 크다면 return
    if cnt >= answer:
        return
    # idx가 목적지 N-1이상일 때
    if idx >= N-1:
        # cnt와 answer를 비교하여 작은 값을 answer에 저장
        if cnt <= answer:
            answer = cnt
        return
    # idx위치의 연료로 갈 수 있는 모든 위치를 방문
    for i in range(Bat[idx]):
        dfs(idx+i+1, cnt+1)

T = int(input())
for case in range(1, T+1):
    # N개의 버스, Bus의 배터리 정보 N-1개를 받을 리스트 Bat
    N, *Bat = map(int, input().split())
    # answer값 최대값으로 초기화
    answer = 10000
    # 인덱스 0, cnt -1에서 시작
    dfs(0,-1)

    # 테스트케이스 번호와 answer 출력
    print(f'#{case} {answer}')