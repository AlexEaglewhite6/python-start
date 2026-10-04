import csv, random, datetime

random.seed(42)

date_today = datetime.date.today()
date_period = 60
date_from = date_today-datetime.timedelta(days=date_period)

date_random_from = date_from.toordinal()
date_random_to = date_today.toordinal()


opening_hour = 9
opening_minute = 0
closing_hour = 21
closing_minute = 0

opening_time_sec = opening_hour * 3600 + opening_minute * 60
closing_time_sec = closing_hour * 3600 + closing_minute * 60

assortment = []
discounts = [0, 5, 10, 15]
with open("assortment.csv", "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        assortment.append(line.strip().split(","))

with open("orders.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=
                            ["order_id",
                             "date",
                             "product",
                             "category",
                             "price",
                             "qty",
                             "discount"])
    writer.writeheader()
    i = 1
    while i <= 200:
        random_date = datetime.date.fromordinal(random.randint(date_random_from, date_random_to)).strftime("%d.%m.%Y")
        random_time_sec = random.randint(opening_time_sec, closing_time_sec)
        random_hour,remain_sec = divmod(random_time_sec, 3600)
        random_minute, random_sec = divmod(remain_sec, 60)
        random_time = datetime.time(hour=random_hour, minute=random_minute, second=random_sec)
        random_datetime = f"{random_date} {random_time}"
        random_product = random.choice(assortment)        
        writer.writerow({"order_id" : i,
                         "date" : random_datetime,
                         "product" : random_product[0],
                         "category" : random_product[1],
                         "price" : random_product[2],
                         "qty" : random.randint(1,50),
                         "discount" : random.choice(discounts)})
        i += 1