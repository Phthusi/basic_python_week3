def calculate_discount(price, discount_percent):
    if discount_percent>=(20/100):
        return price - price * discount_percent
    return price

def run_discount():
    price = float(input('Enter the original price of an item: '))
    discount_percent = float(input('Enter the discount percentage: '))
    return calculate_discount(price, discount_percent)

print(run_discount())