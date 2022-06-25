from collections import deque
import sys

def bfs(N):
    # deque를 활용하여 queue 생성
    queue = deque()
    # queue에 첫 위치 추가
    queue.append(N)
    # queue에 값이 없어질 때까지 whil문 진행
    while queue:
        # 변수 temp에 queue.popleft() 값을 할당
        temp = queue.popleft()
        # N == K라면 checked[temp] return
        if temp == K:
            return checked[temp]
        # temp에서 움직일 수 있는 모든 결과 result에 대해 for문 진행
        for result in (temp - 1, temp + 1, 2 * temp):
            # result가 범위 안에 있고 이미 방문한 위치가 아니라면
            if 0 <= result <= 100000 and checked[result] == 0:
                # check에 방문시간을 할당 후 result를 queue에 추가
                checked[result] = checked[temp] + 1
                queue.append(result)

# 수빈이의 위치 N, 동생의 위치 K
N, K = map(int, sys.stdin.readline().split())

# 이미 확인한 숫자인지 여부와 도착 시간을 담을 리스트 checked
checked = [0] * 100001
# 수빈이의 위치를 넣어 bfs 실행 후 return 값 시간을 출력
print(bfs(N))