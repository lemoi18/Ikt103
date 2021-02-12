import csv

# for every customer

with open('customers.csv', mode='r', ) as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        id = row[0]
        name = row[1]
        address = row[2]
        print('Customer:', end='')
        print(f' {row[1]}, {row[2]} ')


with open('customers.csv', mode='r', ) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    name_customer_id_ = {}
    for row in csv_reader:
        id = row['id']
        fornavn = row['name']
        address = row['address']
        if id in name_customer_id_:
            name_customer_id_[id] += fornavn

        if id not in name_customer_id_:
            name_customer_id_[id] = fornavn
# for every product <product>, <cost>
with open('products.csv', mode='r', ) as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        id = row[0]
        name = row[1]
        price = row[2]
        print('Product:', end='')
        print(f' {row[1]}, {row[2]} ')
# 3  <product name> amount: <amount>
with open('orders.csv', mode='r', ) as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    total = {}

    for row in csv_reader:

        product_id = row['productid']
        amount = int(row['amount'])
        if product_id in total:
            total[product_id] += amount

        if product_id not in total:
            total[product_id] = amount

with open('products.csv', mode='r', ) as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        name = row[1]
        id = row[0]
        price = row[2]
        if id in total:
            total[name] = total.pop(id)

    for pair in total.items():
        print(f'{pair[0]} amount: {pair[1]}')

# 4 <product name> gross income: <amount>
with open('products.csv', mode='r') as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    next(reader)
    for row in reader:
        price = int(row[2])
        name = row[1]
        amut = int(total.get(row[1]))
        if name in total:
            total[name] = amut * price

    for pair in total.items():
        print(f"{pair[0]} gross income: {pair[1]}")

# 5

with open('products.csv', mode='r', ) as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    productid_and_price = {}
    for row in csv_reader:
        name = row['name']
        id = row['id']
        price = row['price']
        if id in productid_and_price:
            productid_and_price[id] += int(price)

        if id not in productid_and_price:
            productid_and_price[id] = int(price)

with open('orders.csv', mode='r', ) as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    order = {}
    custormer_product = {}

    for row in csv_reader:

        customer_id = row['customerid']
        product_id = row['productid']
        amount = int(row['amount'])
        if customer_id in order:
            order[customer_id] += amount

        if customer_id not in order:
            order[customer_id] = amount


with open('orders.csv', mode='r', ) as csv_file:
    csv_reader = csv.reader(csv_file, skipinitialspace=True)

    for id in name_customer_id_:
        money_spent = 0

        for line in csv_reader:
            if line[1] == id:
                for eyedi, price in productid_and_price.items():
                    if eyedi == line[2]:
                        money_spent += int(price) * int(line[3])

                    else:
                        continue

        for fornavn, aydie in name_customer_id_.items():
            if id == fornavn:
                print(f'{aydie} money spent: {money_spent}')


        csv_file.seek(0)