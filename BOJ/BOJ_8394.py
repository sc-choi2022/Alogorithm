import sys

# 회의에 참석한 사람의 수
N = int(sys.stdin.readline())
# 초기 점화식 값 d1, d2, d3을 0, 1, 2로 초기화
d1, d2, d3 = 0, 1, 2

for i in range(3, N + 1):
    # 점화식을 만족하면서 마지막 자리수만을 d1, d2, d3에 저장
    d1, d2, d3 = d2, d3, (d2 + d3)%10
# d3 출력
print(d3)