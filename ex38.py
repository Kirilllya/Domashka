sides = int(input("Введите количество сторон (от 3 до 10): "))

if sides < 3 or sides > 10:
    print("Ошибка: количество сторон должно быть от 3 до 10.")
else:
    if sides == 3:
        figure = "треугольник"
    elif sides == 4:
        figure = "квадрат"
    elif sides == 5:
        figure = "пятиугольник"
    elif sides == 6:
        figure = "шестиугольник"
    elif sides == 7:
        figure = "семиугольник"
    elif sides == 8:
        figure = "восьмиугольник"
    elif sides == 9:
        figure = "девятиугольник"
    elif sides == 10:
        figure = "десятиугольник"

    print(f"Фигура с {sides} сторонами - это {figure}.")

# решено, но зачем такая конструкция? -)
# if
# else:
#     if 
#     elif
#     elif

# да и можно было обойтись без такого количества elif
