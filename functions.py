def calculate_discount(price, discount_percent):
    if discount_percent>=(20/100):
        return price - price * discount_percent
    return price

def calculate_discount():
    price = input('Enter the original price of an item: ')
    discount_percent = input('Enter the discount percentage: ')
    return calculate_discount(price, discount_percent)
