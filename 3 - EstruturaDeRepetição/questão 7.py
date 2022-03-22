comp = 0

for i in range(1, 6):
    num1 = float(input())
    if num1 > comp:
        comp = num1
    if i == 1:
        comp = num1

print(comp)