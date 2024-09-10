import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 비밀번호의 길이 N
    N = int(sys.stdin.readline())
    # 해당 idx로 끝나는 비밀번호의 개수를 저장하는 배열 prev
    prev = [1] * 10
    for _ in range(N-1):
        tmp = [0] * 10
        tmp[0] = prev[7]
        tmp[1] = prev[2] + prev[4]
        tmp[2] = prev[1] + prev[3] + prev[5]
        tmp[3] = prev[2] + prev[6]
        tmp[4] = prev[1] + prev[5] + prev[7]
        tmp[5] = prev[2] + prev[4] + prev[6] + prev[8]
        tmp[6] = prev[3] + prev[5] + prev[9]
        tmp[7] = prev[4] + prev[8] + prev[0]
        tmp[8] = prev[5] + prev[7] + prev[9]
        tmp[9] = prev[6] + prev[8]
        prev = tmp

    # 조건을 만족하는 비밀번호의 개수를 출력
    print(sum(prev)%1234567)