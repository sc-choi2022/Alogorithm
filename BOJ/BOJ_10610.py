import sys
# 양수 N의 각 자리수를 담은 리스트 N
N = list(map(int, list(sys.stdin.readline().strip())))

# 30의 배수를 만들 수 없는 경우 -1 출력
if sum(N)%3 or 0 not in N:
    print(-1)
# 만들 수 있다면
else:
    # 정렬 후 출력
    N.sort(reverse=True)
    for n in N:
        print(n, end='')