grades = int(input("Введите набранные баллы (0-100): "))

if grades > 100:
    print("Ошибка: балл не может быть больше 100")
elif grades >= 85:
    print("Отлично (A)")
elif grades >= 65:
    print("Хорошо (B)")
elif grades >= 50:
    print("Удовлетворительно (C)")
else:
    print("Не зачтено (F)")