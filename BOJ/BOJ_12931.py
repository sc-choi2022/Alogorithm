import sys

# 배열의 크기 N
N = int(sys.stdin.readline())
# 배열 B
B = list(map(int, sys.stdin.readline().split()))

# 연산1(값 하나를 1 증가), 연산2(배열의 모든 값을 두 배)의 개수
cnt1, cnt2 = 0, 0

for b in B:
    # b를 만들기 위해 필요한 연산2의 개수
    tmp = 0
    while b:
        # b가 2의 배수인 경우
        if not b%2:
            tmp += 1
            b //= 2
        # b가 2의 배수가 아니기때문에 연산 1이 필요한 경우
        else:
            cnt1 += 1
            b -= 1
    # 연산2의 최대 개수 cnt2에 저장
    cnt2 = max(cnt2, tmp)

# 배열 A를 B로 바꾸기 위한 최소 연산 횟수를 출력
print(cnt1+cnt2)