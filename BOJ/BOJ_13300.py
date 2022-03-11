# 학생수 N, 최대 인원 수 K
N, K = map(int, input().split())

# 여자와 남자의 학년별 인원수를 index와 학년의 매칭할 리스트 xx, xy
xx = [0] * 7
xy = [0] * 7
# 필요한 방의 수 초기화
room = 0
# N개의 정보를 받아 성별에 맞게 학년에 추가
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        xx[Y] += 1
    elif S == 1:
        xy[Y] += 1

# K를 기준으로 room의 수를 확인
for i in range(1, 7):
    room += xx[i] // K
    room += xy[i] // K
    if xx[i]%K != 0:
        room += 1
    if xy[i]%K != 0:
        room += 1

# 최소한의 방의 수 출력
print(room)