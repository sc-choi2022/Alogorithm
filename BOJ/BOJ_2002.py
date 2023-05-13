import sys

# 차의 대수 N
N = int(sys.stdin.readline())
# 입구의 차량 순서를 저장하는 딕셔너리
enter = dict()
# 출구의 차량 순서
leave = [''] * N
# 추월 차의 대수 cnt
cnt = 0

for i in range(N):
    enter[sys.stdin.readline().rstrip()] = i
for j in range(N):
    leave[j] = sys.stdin.readline().rstrip()

for k in range(N-1):
    for l in range(k+1, N):
        if enter[leave[k]] > enter[leave[l]]:
            cnt += 1
            break
# 터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차가 몇 대인지 출력
print(cnt)