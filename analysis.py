#---------------------------------------------------
# БИБЛИОТЕКИ
#---------------------------------------------------
import csv
from datetime import datetime
#---------------------------------------------------

#---------------------------------------------------
# ПЕРЕМЕННЫЕ
#---------------------------------------------------
orders = [] # Список из словарей заказов
WEEKDAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
MONTH = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
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
    print(f"Цена: {order["price"]:,} руб.")
    print(f"Количество: {order["qty"]:,} шт.\n")
    print(f"Cумма заказа (без скидки): {revenue(order["price"], order["qty"]):,} руб.")
    print(f"Скидка: {order["discount"]}%")
    print(f"Сумма заказа (со скидкой): {revenue(order["price"], order["qty"], order["discount"]):,} руб.")

def percent(a, b):
    return a * 100 / b
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
total_discount_costs = total_gross_revenue - total_net_revenue
avg_check = total_net_revenue / count_of_orders
min_order = min(orders, key = lambda o : revenue(o["price"], o["qty"], o["discount"]))
max_order = max(orders, key = lambda o : revenue(o["price"], o["qty"], o["discount"]))
#---------------------------------------------------
# ВЫВОД АНАЛИЗА
#---------------------------------------------------
print("ОБЩАЯ СВОДКА\n")
print(f"Общее количество заказов: {count_of_orders}")
print(f"Валовая выручка: {total_gross_revenue:,.2f} руб.")
print(f"Реальная выручка: {total_net_revenue:,.2f} руб.")
print(f"Издержки на скидки: {total_discount_costs:,.2f} руб.")
print(f"Доля издержек в выручке: {percent(total_discount_costs, total_gross_revenue):.2f}%")
print(f"Средний чек: {avg_check:,.2f} руб.")
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
    gross_revenue = stat["gross_revenue"]
    net_revenue = stat["net_revenue"]
    discount_cost = gross_revenue - net_revenue
    print(f"Категория: {cat}\n")
    print(f"Количество заказов: {stat["orders"]}")
    print(f"Валовая выручка: {gross_revenue:,.2f} руб.")
    print(f"Чистая выручка: {net_revenue:,.2f} руб.")
    print(f"Издержки на скидках: {discount_cost:,.2f} руб.")
    print(f"Доля издержек в категории: {percent(discount_cost, net_revenue):,.2f}%")
    print(f"Средний чек: {stat["net_revenue"]/stat["orders"]:,.2f} руб.")
    print(f"Доля от общей выручки: {percent(stat["net_revenue"], total_net_revenue):,.2f}%\n\n")

print("ТОП 5 ТОВАРОВ\n")

revenue_by_products = {}
qty_by_products = {}
for o in orders:
    if o["product"] not in qty_by_products:
        qty_by_products[o["product"]] = o["qty"]
    else:
        qty_by_products[o["product"]] += o["qty"]

    if o["product"] not in revenue_by_products:
        revenue_by_products[o["product"]] = revenue(o["price"], o["qty"], o["discount"])
    else:
        revenue_by_products[o["product"]] += revenue(o["price"], o["qty"], o["discount"])

top_by_qty = sorted(qty_by_products, key= lambda product : qty_by_products[product], reverse=True)[:5]
top_by_revenue = sorted(revenue_by_products, key = lambda product: revenue_by_products[product], reverse=True)[:5]

print("Топ 5 товаров по выручке:\n")
for i, product in enumerate(top_by_revenue, start=1):
    print(f"{i}. {product} - {revenue_by_products[product]:,.2f} руб.")
print("\nТоп 5 товаров по количеству:\n")
for i, product in enumerate(top_by_qty, start=1):
    print(f"{i}. {product} - {qty_by_products[product]} шт.")


revenue_by_weekdays = {}
revenue_by_month = {}

for o in orders:
    dt = datetime.strptime(o["date"], "%d.%m.%Y %H:%M:%S")
    weekday = WEEKDAYS[dt.weekday()]
    month = MONTH[dt.month]
    if weekday not in revenue_by_weekdays:
        revenue_by_weekdays[weekday] = 0
    else:
        revenue_by_weekdays[weekday] += revenue(o["price"], o["qty"], o["discount"])

    if month not in revenue_by_month:
        revenue_by_month[month] = 0
    else:
        revenue_by_month[month] += revenue(o["price"], o["qty"], o["discount"])

print("\nВЫРУЧКА ПО ДНЯМ НЕДЕЛИ:\n")

for week_name in WEEKDAYS:
    if week_name in revenue_by_weekdays:
        print(f"{week_name} - {revenue_by_weekdays[week_name]:,.2f} руб.")

print("\nВЫРУЧКА ПО МЕСЯЦАМ\n")
for month_name in MONTH:
    if month_name in revenue_by_month:
        print(f"{month_name} - {revenue_by_month[month_name]:,.2f} руб.")

best_cat = max(by_category, key=lambda c: by_category[c]["net_revenue"]) 
best_cat_rev = by_category[best_cat]["net_revenue"]
worst_cat = min(by_category, key=lambda c: by_category[c]["net_revenue"])
worst_cat_rev = by_category[worst_cat]["net_revenue"]
print("\n\nКатегория лидер по продажам:\n")
print(f"{best_cat} - {best_cat_rev:,.2f} руб. ({percent(best_cat_rev, total_net_revenue):.2f})%")
print("\nКатегория аутсайдер по продажам:\n")
print(f"{worst_cat} - {worst_cat_rev:,.2f} руб. ({percent(worst_cat_rev, total_net_revenue):.2f}%)")