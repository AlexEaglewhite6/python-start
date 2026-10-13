#---------------------------------------------------
# БИБЛИОТЕКИ
#---------------------------------------------------
import csv
#---------------------------------------------------

#---------------------------------------------------
# ПЕРЕМЕННЫЕ
#---------------------------------------------------
orders = [] # Список из словарей заказов

#---------------------------------------------------
# ФУНКЦИИ
#---------------------------------------------------

#---------------------------------------------------
# Считае выручку с учетом и без учета скидки
def revenue(price, qty, discount = 0):
    return price * qty * ( 1 - discount / 100 )
#---------------------------------------------------
# Считает общую выручку за несколько заказов (по умолчанию без учета скидок)
def total_revenue(orders, discounts = False):
    total = 0
    if discounts == True:
        for o in orders:
            total += revenue(o["price"], o["qty"], o["discount"])
        return total
    else:
        for o in orders:
            total += revenue(o["price"], o["qty"])
        return total
#---------------------------------------------------
# Выводит форматированное представление заказа
def format_order(order):
    print(f"Дата: {order["date"]}\n")
    print(f"Продукт: {order["product"]}")
    print(f"Цена: {order["price"]:,}")
    print(f"Количество: {order["qty"]:,}\n")
    print(f"Cумма заказа (без скидки): {revenue(order["price"], order["qty"]):,}")
    print(f"Скидка: {order["discount"]}")
    print(f"Сумма заказа (со скидкой): {revenue(order["price"], order["qty"], order["discount"]):,}")

#---------------------------------------------------
# ЧТЕНИЕ CSV ФАЙЛА
#---------------------------------------------------
with open("orders.csv", "r", encoding="utf-8") as f:
    next(f) #Пропуск заголовка
    for line in f:
        order = line.strip().split(",")
        orders.append(
            {
                "order_id" : int(order[0]),
                "date" : order[1],
                "product" : order[2],
                "category" : order[3],
                "price" : int(order[4]),
                "qty" : int(order[5]),
                "discount" : int(order[6])
            }
        )
#---------------------------------------------------

count_of_orders = len(orders) # количество заказов

total_gross_revenue = total_revenue(orders)
total_net_revenue = total_revenue(orders, True)
avg_check = total_net_revenue / count_of_orders
min_order = min(orders, key = lambda o : revenue(o["price"], o["qty"], o["discount"]))
max_order = max(orders, key = lambda o : revenue(o["price"], o["qty"], o["discount"]))
#---------------------------------------------------
# ВЫВОД АНАЛИЗА
#---------------------------------------------------
print("ОБЩАЯ СВОДКА\n")
print(f"Общее количество заказов: {count_of_orders}")
print(f"Валовая выручка: {total_gross_revenue:,}")
print(f"Реальная выручка: {total_net_revenue:,}")
print(f"Издержки на скидки: {(total_gross_revenue - total_net_revenue):,}")
print(f"Средний чек: {avg_check:,}")

print("\nМинимальный заказ:\n")
format_order(min_order)

print("\nМаксимальный заказ:\n")
format_order(max_order)

print("\nВЫРУЧКА ПО КАТЕГОРИЯМ\n")

by_category = {}
for o in orders:
    if o["category"] not in by_category:
        by_category[o["category"]] = {
            "orders" : 1,
            "gross_revenue" : revenue(o["price"], o["qty"]),
            "net_revenue" : revenue(o["price"], o["qty"], o["discount"]),
        }
    else:
        by_category[o["category"]]["orders"] += 1
        by_category[o["category"]]["gross_revenue"] += revenue(o["price"], o["qty"])
        by_category[o["category"]]["net_revenue"] += revenue(o["price"], o["qty"], o["discount"])

for cat, stat in by_category.items():
    print(f"Категория: {cat}\n")
    print(f"Количество заказов: {stat["orders"]}")
    print(f"Валовая выручка: {stat["gross_revenue"]:,.2f}")
    print(f"Чистая выручка: {stat["net_revenue"]:,.2f}")
    print(f"Средний чек: {stat["net_revenue"]/stat["orders"]:,.2f}\n\n")