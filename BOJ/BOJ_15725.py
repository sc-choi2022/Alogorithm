import sys

E = sys.stdin.readline().rstrip()

if E[:2] == '-x':
    E = E.replace('-x', '-1x')

