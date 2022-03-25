def Bitprint(i):
    for j in range(7, -1, -1):
        print('1' if (i& (1<<j)) else '0', end = "")
        # print("%d"% ((i>>j) &1), end = "")

a = 0x10
x = 0x01020304

print('{} = '.format(a), end = "")
Bitprint(a)

print()

# %08x는 숫자 x를 8 hex digits로 표현
print("%08x = " % x, end = "")

for i in range(0, 25, 8):

    Bitprint(x >> i)
    print(end = " ")