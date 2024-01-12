import sys

# 채팅방의 기록 수 N
N = int(sys.stdin.readline())
# 채팅 기록 중 곰곰티콘이 사용된 횟수 answer
answer = 0
# ENTER를 기점으로 곰곰티콘을 사용하는 사람을 저장하는 셋 cnt
cnt = set()

for _ in range(N):
    recode = sys.stdin.readline().rstrip()

    # 새로운 유저가 입장한 경우, 즉 곰곰티콘이 사용되는 조건
    if recode == 'ENTER':
        answer += len(cnt)
        cnt = set()
        continue
    # 곰곰티콘을 사용한 유저를 저장
    cnt.add(recode)
# 채팅 기록 중 곰곰티콘이 사용된 횟수를 출력
print(answer+len(cnt) if cnt else answer)