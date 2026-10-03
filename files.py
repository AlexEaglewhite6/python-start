with open("notes.txt", "w", encoding="utf") as f:
    f.write("Каждый новый день дарит нам шанс начать всё с чистого листа.\n")
    f.write("Важно не забывать ценить моменты, которые кажутся обычными.\n")
    f.write("Именно из таких мелочей в итоге складывается наше счастье.\n")
    f.write("Главное — сохранять искренность и верить в свои силы всегда.\n")
    f.write("Пусть этот текст станет для вас небольшим напоминанием о важном.\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    count_of_lines = 0
    for line in f:
        count_of_lines += 1
        print(f"{count_of_lines}. {line}")
        
    print(f"\nКоличество строк в файле: {count_of_lines}\n")

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Ведь даже самый долгий путь начинается с одного маленького шага.\n")
    f.write("Идите к своей мечте смело, ведь вы способны на большее, чем кажется.\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("А я все стер!")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())