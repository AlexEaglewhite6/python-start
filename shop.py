products = [
    {"name" : "Гортензия", "price" : 850, "qty" : 12},
    {"name" : "Хризантема", "price" : 450, "qty" : 25},
    {"name" : "Роза", "price" : 375, "qty" : 20},
    {"name" : "Пионы", "price" : 1000, "qty" : 10},
    {"name" : "Альстрамерия", "price" : 230, "qty" : 23},
]

print("Католог товаров:\n")

for product in products:
    print(f"{product.get("name")} - {product.get("price")} руб. ")

print("\nОбщая стоимость товаров:\n")

for product in products:
    print(f"{product.get("name")} - {product.get("price") * product.get("qty")} руб.")

max_price = 0
expensive_product = {}

for product in products:
    if product.get("price") > max_price:
        max_price = product.get("price")
        expensive_product = product

print(f"\nСамый дорогой товар - {expensive_product.get("name")} по цене {expensive_product.get("price")} руб.")

print("\nТовары, которых больше 20 штук:\n")

for product in products:
    if product.get("qty") > 20:
        print(f"{product.get("name")} - {product.get("qty")} шт.")

print("\nТовары при 10% скидки")

discount = 10

#Цена * процент = цена с процентом. 10/100 = 0.1
for product in products:
    print(f"{product.get("name")} - {int(product.get("price") * (1-(discount/100)))}")