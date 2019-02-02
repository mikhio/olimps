I = input()
S = I.split(' ')

a = int(S[0])
b = int(S[1])

s = int((a - 1) / 4) + 1
g = int((b - 1) / 4) + 1
r = a % 2
j = b % 2

if s == g:
    print ('YES')
else:
    print('NO')

if r == 0:
    print('HIGH')
else:
    print('LOW')

if j == 0:
    print('HIGH')
else:
    print('LOW')