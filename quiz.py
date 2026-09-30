import random

questions= [
    {"text" : "Столица России? ", "answer" : "Москва"},
    {"text" : "Сколько планет в солнечной системе? ", "answer" : "8"},
    {"text" : "Сколько официальных языков в Швейцарии? ", "answer" : "4"}
]

name = input("Как тебя зовут? ")
points = 0

print(f"{name}, тебе нужно пройти викторину из 3-х вопросов.")

random.shuffle(questions)
for question in questions:
    user_answer = input(f"{question.get("text")}").strip().lower()

    if (user_answer == question.get("answer").strip().lower()):
        points += 1
        print("Правильно!")
    else:
        print(f"Неправильной! Правильный ответ: {question.get("answer")}")

if points == 0:
    print("Ты вообще что-то знаешь?")
elif points == 1:
    print(f"Глюпий {name} набрал {points} балл!")
elif points == 2:
    print(f"Неплохо, {name}, но можно было и лучше. Всего {points} балла.")
elif points == 3:
    print(f"{name}, да ты гений! Все {points} балла!")