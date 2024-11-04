human_age = float(input("Введите возраст вашей собаки в человеческих годах: "))

if human_age < 0:
    print("Ошибка: возраст не может быть отрицательным.")
else:

    if human_age <= 2:
        dog_age = human_age * 10.5
    else:
        dog_age = 21 + (human_age - 2) * 4

    print(f"Возраст вашей собаки в собачьих годах: {dog_age} лет.")
