name = input("Как тебя зовут? ")
points = 0

print(f"{name}, тебе нужно пройти викторину из 3-х вопросов.")

if input("1. Столица России? ") == "Москва":
    points = points + 1
    print("Правильной!")
else:
    print("Неправильной! Правильный ответ: Москва")

if int(input("2. Сколько планет в солнечной системе? ")) == 8:
    points = points + 1
    print("Правильно!")
else:
    print("Неправильно! Правильный ответ: 8")

if int(input("3. Сколько официальных языков в Швейцарии? ")) == 4:
    points = points + 1
    print("Правильно!")
else:
    print("Неправильно! Правильный ответ: 4")

if points == 0:
    print("Ты вообще что-то знаешь?")
elif points == 1:
    print(f"Глюпий {name} набрал {points} балл!")
elif points == 2:
    print(f"Неплохо, {name}, но можно было и лучше. Всего {points} балла.")
elif points == 3:
    print(f"{name}, да ты гений! Все {points} балла!")