import sys

# 기차 안의 현재 인원 수 train
train = 0
# 출력할 최댓값 ans
ans = 0

for i in range(4):
    # 내린 사람의 수 leave, 탄 사람의 수 take
    leave, take = map(int, sys.stdin.readline().split())

    train -= leave
    ans = max(ans, train)
    train += take
    ans = max(ans, train)
# 최대 사람 수를 출력
print(ans)