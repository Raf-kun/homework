n = int(input("Введите сторону: "))
square = []

#диагонналь

for i in range(n):
    for j in range(n):
        if j <= i:
            print(" * ", end='')
        else:
            print("   ", end='')
    print()

print()

for i in range(n):
    for j in range(n):
        if j <= n - 1 - i:
            print("  ", end='')
        else:
            print(" * ", end='')
    print()
