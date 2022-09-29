# 그룹번호값을 초기화
group = 1

while True:
    # 아이들의 수 혹은 종료 0을 N에 저장
    N = int(input())
    # 아이들의 이름과 메세지의 종류를 담을 리스트 name, word
    name = [0]*N
    word = [0]*N

    # N이 종료 0이라면 break
    if N == 0:
        break
    # N이 아이들의 명수라면 Group번호를 출력
    print('Group', group)
    # N명의 정보를 name고 word에 저장
    for i in range(N):
        lst = list(input().split())
        name[i] = lst[0]
        word[i] = lst[1:]

    # 나쁜 메세지를 보낸 사람이 존재하는 지 확인하기 위한 flag
    flag = True
    # j번째 아이의 메세지 정보를 확인한다.
    for j in range(len(name)):
        for k in range(len(word[0])):
            # 나쁜 메세지가 있는 경우
            if word[j][k] == 'N':
                # 누가(A) 누구(B)에게 나쁜 말을 했는지 "A was nasty about B"로 출력
                print(name[j-k-1], 'was nasty about', name[j])
                # 나쁜 메세지가 존재하는 Group이므로 False 저장
                flag = False
    # 아무도 나쁜 메세지를 받지 않은 경우
    if flag:
        print('Nobody was nasty')
    print()
    # group 1 증가
    group += 1