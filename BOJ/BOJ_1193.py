# X번째 분수를 찾는 값 X
X = int(input())
# X를 찾기위해 값의 위치를 확인할 변수 check
check = 1
# 대각선 갯수를 세는 변수 cnt
cnt = 1
# 마지막의 더해지는 cnt의 몇번째 숫자인지를 확인하기 위한 변수 a
a = 0

while True:
    # check + cnt값이 X보다 커지면 분수의 위치를 지나치는 것이므로 break
    if check + cnt > X:
        # 마지막에 더해지는 cnt의 몇번째 숫자인지를 확인
        a = X - check
        break
    # check에 cnt를 더해주고 cnt 1 증가
    check += cnt
    cnt += 1
# cnt가 홀수이면 대각선이 오른쪽을 향한다.
if cnt % 2:
    # 분자의 값이 점점 작아지고 분모의 값이 점점 커진다. 이는 a와 cnt로 표현가능하다.
    print(str(cnt - a) + '/' + str(a + 1))
# cnt가 짝수이면 대각선이 왼쪽을 향한다.
else:
    print(str(a + 1) + '/' + str(cnt - a))