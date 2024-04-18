import sys

# 운동기구의 개수 N
N = int(sys.stdin.readline())
# 근손실 정도를 나타내는 정수를 저장하는 loss
loss = sorted(list(map(int, sys.stdin.readline().split())))

# 홀수인 경우 활용하는 변수 tmp
tmp = -1
if len(loss)%2:
    tmp = loss.pop()

maximum = -1
for i in range(N//2):
    maximum = max(maximum, loss[i] + loss[-(i+1)])

# 근손실 정도의 합의 최솟값을 출력
print(max(tmp, maximum))