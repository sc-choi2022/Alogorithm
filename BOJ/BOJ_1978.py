# 수의 개수 N
N = int(input())
# N개의 수를 담을 리스트 numbers
numbers = list(map(int, input().split()))
# 소수의 개수를 출력할 변수 ans
ans = 0

# numbers의 모든 number에 대해
for number in numbers:
    # 1은 소수도 약수로 가지고 있으므로 cnt 2부터 시작
    cnt = 2
    # cnt가 number가 될때 까지
    while cnt < number:
        # 약수인 cnt를 만나면 while문을 탈출
        if number % cnt == 0:
            break
        # if문을 만나지 않았다면 cnt 1증가
        cnt += 1
    # 만약 cnt가 number의 수까지 도달했다면 소수이므로 ans 1증가
    if cnt == number:
        ans += 1

# ans를 출력
print(ans)