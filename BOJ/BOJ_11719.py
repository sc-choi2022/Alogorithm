while True:
    # input()을 출력
    try:
        print(input())
    # EOFError 런타임에러가 발생한다면 break
    except EOFError:
        break