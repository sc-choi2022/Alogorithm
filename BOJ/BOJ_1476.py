# 지구 E, 태양 S, 달 M
E, S, M = map(int, input().split())

# year 값을 1로 초기화
year = 1
while True:
    # E, S, M의 값을 빼고 각 값의 최대값을 나눈 나머지가 0인 경우 year 출력
    if (year - E)%15 == 0 and (year - S)%28 == 0 and (year - M)%19 == 0:
        print(year)
        break
    # 아닌 경우 year 1 증가
    else:
        year += 1