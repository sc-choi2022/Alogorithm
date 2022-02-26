lights = input()
lights = list('N' + lights)
n = len(lights)
cnt = 0
for i in range(1, n):
    # 전구가 켜져 있다면
    if lights[i] == 'Y':
        # 스위치를 누른다.
        cnt += 1
        # 스위치를 눌렀을 때 일어날 일
        # i의 배수 위치의 값들의 상태를 변경
        for s in range(i, n, i):
            if lights[s] == 'Y':
                lights[s] = 'N'
            elif lights[s] == 'N':
                lights[s] = 'Y'
    # 더 이상 켜진 전구가 없다면 탈출
    if 'Y' not in lights:
        break
if 'Y' in lights:
    cnt = -1
# 모든 전구를 끄기 위해서 스위치를 누른 횟수 출력
print(cnt)