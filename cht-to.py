import time

print("Подойти к раковине")
time.sleep(2)
print("Включаем воду")
time.sleep(3)
print("Складываем посуду в раковину")
time.sleep(4)
print("Процесс мытья посуды")
time.sleep(5)
posuda = int(input("Сколько там посуды?: "))
i = 0
while i <= posuda:
    print("Намыливаем губку...")
    time.sleep(5)
    print("Моем поусуду.... моем...")
    time.sleep(7)
    i += 1
print("Протираем помытую посуду...")
time.sleep(5)
print("Убираем посуду! Юху! Мы все сделали, можем идти спать!")
time.sleep(5)

