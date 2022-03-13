for _ in range(4):
    arr = list(map(int, input().split()))
    ans = 'a'
    # d인 경우
    if arr[2] < arr[4] or arr[6] < arr[0] or arr[3] < arr[5] or arr[7] < arr[1]:
        ans = 'd'
    else:
        # c인 경우
        if [arr[0], arr[1]] == [arr[6], arr[7]] or [arr[2], arr[3]] == [arr[4], arr[5]] or [arr[0], arr[3]] == [arr[6], arr[5]] or [arr[4], arr[7]] == [arr[2], arr[1]]:
            ans = 'c'
        # b인 경우
        elif arr[1] == arr[7] or arr[3] == arr[5] or arr[0] == arr[6] or arr[2] == arr[4]:
            ans = 'b'
    # 출력
    print(ans)

