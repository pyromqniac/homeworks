low = 10
high = 500
attempts = 0
secret = 342

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    print(f"Шаг {attempts}: проверяем число {guess}")
    if guess == secret:
        print(f"Успех! Число {secret} найдено за {attempts} шагов.")
        break
    elif guess < secret:
        low = guess + 1
    else:
        high = guess - 1