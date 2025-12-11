def build_sales_log(sales_list):
    sales_dict = {}
    for line in sales_list:
        line = line.split('|')
        e_id, item_name, price= line
        price = float(price)
        if e_id not in sales_dict:
            sales_dict[e_id] = 0
        sales_dict[e_id] += price
    return sales_dict

def find_top_performer(sales_dict):
    top_employee = ''
    top_amount = 0
    for e_id, amount in sales_dict.items():
        if amount > top_amount:
            top_amount = amount
            top_employee = e_id
    return f'Top Performer is {top_employee} with ${top_amount}'

sales_list = [
    "E101|Laptop|1200.00",
    "E102|Mouse|25.50",
    "E101|Monitor|300.00",
    "E103|Headphones|150.00",
    "E102|Keyboard|50.00",
    "E103|Laptop|1000.00",
    "E101|Mousepad|15.00"
]
sales_dict = build_sales_log(sales_list)
print('Sales Report:')
for e_id , amount in sales_dict.items():
    print(f'{e_id}: ${amount:.2f}')
print('--------------------')
print(find_top_performer(sales_dict))

