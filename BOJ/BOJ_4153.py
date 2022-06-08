# 테스트 케이스가 주어지지 않았으므로 while문 사용
while True:
    # 3개의 길이를 담은 리스트 triangle를 정렬
    triangle = list(map(int, input().split()))
    triangle.sort()
    # 만약 0 0 0이 들어오면 break
    if sum(triangle) == 0:
        break
    # 직각삼각형이면 right 출력
    if (triangle[2])**2 == (triangle[0])**2 + (triangle[1])**2:
        print('right')
    # 아니라면 wrong
    else:
        print('wrong')