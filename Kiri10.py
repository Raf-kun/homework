num = int(input("Введите четырехзначное число: "))
desyatki = num // 10
edinitsi = num % 10
summa = desyatki + edinitsi
proisvedenie = desyatki * edinitsi
print(f"В числе {num}, сумма - {summa}, произведение - {proisvedenie}")
