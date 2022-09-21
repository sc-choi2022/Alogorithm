# 3의 배수를 확인할 숫자를 만드는 함수 three
def three(X):
    Y = list(map(int, X))
    return sum(Y)

cnt = 0
X = input()
while True:
    # 한자리 자연수 X가 완성된 경우 cnt 출력
    if int(X) < 10:
        print(cnt)
        # X가 3의 배수라면 YES 출력
        if X in ['3', '6', '9']:
            print('YES')
        # NO 출력
        else:
            print('NO')
        break
    # X에 three(X)의 return 값을 str형태로 저장
    X = str(three(X))
    # cnt 1 증가
    cnt += 1