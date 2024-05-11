import sys

# R행 C열의 위성 사진정보
R, C = map(int, sys.stdin.readline().split())
# 실시간 위성 사진을 저장하는 배열 race
race = [''] + [(sys.stdin.readline().rstrip()) for _ in range(R)]
# 카약의 번호와 거리를 저장하는 배열 result
result = []
for i in range(1, R+1):
    for j in range(1, C):
        if race[i][-j].isnumeric():
            result.append([int(race[i][-j]), j])
            break
result.sort(key=lambda x:(x[1]))
# 순위를 저장하는 변수 rank
rank = 0
# 같은 순위를 확인하기 위한 변수 tmp
tmp = 0
# 팀의 등수를 저장하는 배열 answer
answer = [[] for _ in range(10)]
for r in result:
    if r[1] != tmp:
        rank += 1
    answer[r[0]] = rank
    tmp = r[1]

# i번째 줄에는 i번 팀의 등수를 출력
for k in range(1, 10):
    print(answer[k])