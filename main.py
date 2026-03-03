import random

print("🎮 Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Введи число: "))
        attempts += 1

        if guess < secret_number:
            print("🔼 Больше!")
        elif guess > secret_number:
            print("🔽 Меньше!")
        else:
            print(f"🎉 Ты угадал за {attempts} попыток!")
            break
    except ValueError:
        print("❌ Введи число!")
