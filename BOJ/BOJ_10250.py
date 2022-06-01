# 테스트케이스 개수
T = int(input())

for _ in range(T):
    # 층수 H, 각층의 방 개수 W, N번째 도착한 손님
    H, W, N = map(int,input().split())
    # 방번호의 층수 부분 floor
    floor = N % H
    # 방 번호의 엘리베이터 기준으로 센 번호
    number = N//H + 1
    # 층수는 N % H가 0일때에 예외적인 규칙이 생긴다.
    if N % H == 0:
        # floor는 H, number는 N//H를 그대로 사용한다.
        floor = H
        number = N//H
    # floor와 number를 가지고 규칙에 맞게 출력한다.
    print(floor*100 + number)