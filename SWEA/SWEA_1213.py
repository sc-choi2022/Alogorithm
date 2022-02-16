import sys
sys.stdin = open("test_input.txt", 'rt', encoding='UTF8')

# 10번의 테스트케이스
for _ in range(10):
    # 테스트케이스 번호
    case = int(input())
    # 비교할 패턴
    pattern = list(input())
    # 검색하는 문자열
    fulltext = list(input())
    # 개수를 세는 cnt값 초기화
    cnt = 0

    # 패턴이 문자열을 모두 확인하는 for문
    for i in range(len(fulltext)-len(pattern)+1):
        # 각 시도에 다른 문자가 있는지 확인하는 변수 check
        check = True
        for j in range(len(pattern)):
            # 각 위치의 문자가 다르다면
            if fulltext[i+j] != pattern[j]:
                # check에 False 할당
                check = False
                break
        # 각 시도 후 다른 문자가 없었다면
        if check == True:
            # cnt 1 증가
            cnt += 1
    # 테스트 케이스의 번호와 개수 출력
    print(f'#{case} {cnt}')