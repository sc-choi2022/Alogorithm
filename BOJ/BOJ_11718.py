# 주어지는 값을 출력
while True:
    try:
        print(input())
    # EOF: End Of File, 입력이 끝나면 break
    except EOFError:
        break