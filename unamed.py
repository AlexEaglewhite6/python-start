with open("new file.txt", "w", encoding="utf-8") as f:
    f.write("Это новый файл, который создался автоматически.\n")
    f.write("Здесь должен быть какой-то важный текст, но я его еще не придумал.\n")

with open("new file.txt", "a", encoding="utf-8") as f:
    f.write("А вот еще одна строка!")
    
with open("new file.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(f"new file.txt\n{content}\n")

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(f"data.txt\n{content}\n")

with open("data.txt", "w", encoding="utf") as f:
    f.write("Теперь я чист!")

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(f"data.txt\n{content}")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Какие данные, которые здесь должны быть, но их нет.\nЭто грустно :(")