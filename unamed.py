import csv

orders = []

with open("orders.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        orders.append({
            "order_id" : int(row["order_id"]),
            "product" : row["product"],
            "price" : int(row["price"]),
            "qty" : int(row["qty"]),
        })

print(orders[0])

with open("report.csv", "w", encoding="utf", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["product", "revenue"])
    writer.writeheader()
    writer.writerows([{"product" : "test", "revenue" : "1"}])