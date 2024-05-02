import sys

def sound_check(start):
    global answer
    checklist = 'quack'
    checklist_visit = [-1] * 5
    idx = 0
    # 확인하는 오리의 모든 울음소리 확인
    for d in range(start, L):
        if sound[d] == checklist[idx] and not visited[d]:
            visited[d] = 1
            checklist_visit[idx] = d
            if sound[d] == 'k':
                idx = 0
                checklist_visit = [-1] * 5
                continue
            idx += 1
    if not idx:
        answer += 1
        return
    if checklist_visit[-1] == -1:
        for c_v in checklist_visit:
            visited[c_v] = 0

# 녹음한 소리 sound
sound = sys.stdin.readline().rstrip()
# 녹음한 소리의 길이 L
L = len(sound)
# 울음소리의 확인여부를 저장하는 배열 visited
visited = [0] * L
# 오리의 마리 수 answer
answer = 0

for i in range(L):
    if sound[i] == 'q' and not visited[i]:
        sound_check(i)
if sum(visited) != L or not answer:
    print(-1)
else:
    print(answer)