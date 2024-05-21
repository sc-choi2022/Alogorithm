import sys

# 옵션의 개수 N
N = int(sys.stdin.readline())
# 옵션을 저장하는 셋 options
options = set()

for _ in range(N):
    # 옵션을 나타내는 문자열을 저장하는 배열 words
    words = sys.stdin.readline().rstrip().split()
    # words의 길이 N
    N = len(words)
    # 단축키의 적용 가능 여부를 저장하는 변수 flag
    flag = False

    for i in range(N):
        # 1번으로 단축키 지정이 가능한 경우
        if words[i][0].upper() not in options:
            # 옵션에 단축키를 저장
            options.add(words[i][0].upper())
            # flag에 True를 저장 후 단축키에 괄호를 저장 후 출력
            flag = True
            words[i] = '['+words[i][0]+']'+words[i][1:]
            print(' '.join(words))
            break
    # 2번으로 단축키 지정이 가능한 지 확인
    if not flag:
        for j in range(N):
            # 2번으로 단축키의 적용 가능 여부를 저장하는 변수 check
            check = False
            for k in range(len(words[j])):
                # 단축키 지정이 가능한 경우
                if words[j][k].upper() not in options:
                    # 옵션에 단축키를 저장
                    options.add(words[j][k].upper())
                    # flag와 check에 True를 저장 후 단축키에 괄호를 저장 후 출력
                    flag, check = True, True
                    words[j] = words[j][:k]+'['+words[j][k]+']'+words[j][k+1:]
                    print(' '.join(words))
                    break
            # 2번으로 단축키 적용 완료 시 break
            if check:
                break
    # 어떠한 것도 단축키로 지정할 수 없는 경우 출력
    if not flag:
        print(' '.join(words))