numbers = [123, 24, 67, 666, 114, 322, 10, 56, 9, 34]

print(f"Список чисел: {numbers}")

min = numbers[0]
max = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < min:
        min = numbers[i]

    if numbers[i] > max:
        max = numbers[i]

print(f"Минимальное число в списке: {min}.")
print(f"Максимальное число в списке: {max}")

even_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

print(f"Список четных чисел: {even_numbers}")

reversed_numbers = []
for i in range(len(numbers)):
    reversed_numbers.insert(-i, numbers[i])

print(f"Список чисел в обратном порядке: {reversed_numbers}")

total = 0
for i in range(len(numbers)):
    total += numbers[i]

print(f"Сумма чисел в списке: {total}")