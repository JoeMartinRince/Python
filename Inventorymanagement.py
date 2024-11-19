"""
AUTHOR : Joe Martin Rince
DATE : 19-11-2024
"""
Inventory=[("Laptop",20,50000),("Monitor",5,10000),("smartphone",15,10000)]
highest_stock_value=0
item_with_highest_stock_value=None
for item in Inventory:
    item_name,quantity,stock_value=item
    print(item_name,quantity,stock_value)
for item in Inventory:
    item_name, quantity, stock_value = item
    total_value=quantity*stock_value
    print(f"item name:{item_name},stock value:{stock_value}")
if stock_value>highest_stock_value:
    highest_stock_value=stock_value
    item_with_highest_stock_value=item_name
print("Highest stock is:",highest_stock_value)
print(f"Item with highest stock value is: {item_with_highest_stock_value}")
