import sys
sys.stdin = open("GNS_test_input.txt")

test_case = int(input())
number_rule = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for _ in range(test_case):
    case, number_len = input().split()
    un_lst = list(input().split())
    or_lst = []

    for number in number_rule:
        for i in un_lst:
            if i == number:
                or_lst.append(i)
    print(case)
    print(*or_lst)