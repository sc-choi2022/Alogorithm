# 임한수의 영어 이름 name
name = input()
# 이름의 알파벳의 개수를 담을 딕셔너리 name_dic
name_dic = {}

for i in range(len(name)):
    # 알파벳 name[i]이 name_dic에 있는 경우 value 1 증가
    if name[i] in name_dic:
        name_dic[name[i]] += 1
    # 알파벳 name[i]이 name_dic에 없는 경우 value 1로 저장
    else:
        name_dic[name[i]] = 1
# 사전순으로 재정렬
name_dic = sorted(name_dic.items())
# 짝수개의 알파벳을 저장하는 even, 홀수개의 알파벳을 저장하는 odd
even = ''
odd = ''
# odd의 개수를 담을 리스트 break_cnt
break_cnt = 0

for key, value in name_dic:
    # 알파벳이 홀수개 있는 경우
    if value%2:
        break_cnt += 1
        odd += key
    even += key*(value//2)
    # 팰린드롬이 불가능하면 I'm Sorry Hansoo 출력
    if break_cnt > 1:
        print("I'm Sorry Hansoo")
        exit()

# 영어 이름을 팰린드롬 출력
print(even+odd+even[::-1])