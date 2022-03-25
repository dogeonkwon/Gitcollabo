num = 10
binary = ''
while num != 0:
    binary = str(num % 2) + binary
    num = num // 2
print(binary)

result = 0
for i in range(len(binary)):
    result = result * 2 + int(binary[i])
print(result)