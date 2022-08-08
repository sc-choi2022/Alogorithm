# 테스트케이스 개수 T
T = int(input())

for _ in range(T):
    # A,B로 주어지는 A와 B를 int로 변환하여 lst에 저장
    lst = list(map(int, input().split(',')))
    # A+B을 출력
    print(sum(lst))