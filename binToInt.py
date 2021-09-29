head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
binary = ""

for i in range(0, len(head)):
    binary = binary + str(head[i])

print(binary)
print(int(binary, 2))
