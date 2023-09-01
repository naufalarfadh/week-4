def sales_prices(items_and_prices):
    item = ""
    price = ""
    item_or_prices = items_and_prices.split()
    
    for x in item_or_prices:
        if x.isalpha():
            item += x + " "
        else:
            price = x
    
    item = item.strip()
    
    return "{} are on sale for ${}".format(item,price)

print(sales_prices("Winter fleece jackets 49.99"))