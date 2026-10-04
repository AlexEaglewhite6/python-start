import csv

revenue = 0
min_order = 0
max_order = 0
orders = []
with open("orders.csv", "r", encoding="utf-8") as f:
    next(f)
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

count_of_orders = len(orders) - 1
min_order_revenue = orders[0]["price"] * orders[0]["qty"]
max_order_revenue = min_order_revenue
for order in orders:
    order_revenue = order["price"] * order["qty"]
    revenue += order_revenue


    print(min_order_revenue)

    if order_revenue < min_order_revenue:
        min_order_revenue = order_revenue
        min_order = order
    elif order_revenue > max_order_revenue:
        max_order_revenue = order_revenue
        max_order = order
    

average_check = revenue / count_of_orders

print(f"Всего заказов: {count_of_orders}")
print(f"Общая выручка: {revenue:,}")
print(f"Средний чек: {average_check:,}")
print("\nМинимальный заказ:")
print(f"Дата: {min_order["date"]}\nПродукт: {min_order["product"]}\nЦена: {min_order["price"]}\nКоличество: {min_order["qty"]}\nСумма заказа: {min_order_revenue}")
print("\nМаксимальный заказ: ")
print(f"Дата: {max_order["date"]}\nПродукт: {max_order["product"]}\nЦена: {max_order["price"]}\nКоличество: {max_order["qty"]}\nСумма заказа: {max_order_revenue}")