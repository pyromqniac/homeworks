for i in range(10, 61):
    if i % 4 == 0 and i % 7 == 0:
        print("SuperCombo")
    elif i % 4 == 0:
        print("Four")
    elif i % 7 == 0:
        print("Seven")
else:
    print("Цикл завершен на числе:", i)