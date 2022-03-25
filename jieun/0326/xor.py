def Bitprint(i):
    for j in range(7, -1, -1):
        print('1' if (i& (1<<j)) else '0', end = "")
        # print("%d"% ((i>>j) &1), end = "")

a = 0x86
key = 0xAA
print("a   =>", end = "")
Bitprint(a)
print()
print("a^=key ==>", end = "")
a ^= key
Bitprint(a)
print()
print("a^=key ==>", end = "")
a ^= key
Bitprint(a)
print()
