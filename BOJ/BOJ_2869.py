# 낮에 올라가는 거리, 밤에 미끄러지는 거리, 나무 막대의 거리
A, B, V = map(int,input().split())

# 두가지 경우 존재
# 낮 시간이 지나고 딱 맞게 정상도착: (V-B)/(A-B)만큼 일 걸린다.
# 그렇지 않은 경우: (V-B)/(A-B)의 정수부분에 +1 만큼 일 걸린다.
cnt = (V-B)/(A-B)
if cnt == int(cnt):
    print(int(cnt))
else:
    print(int(cnt) + 1)