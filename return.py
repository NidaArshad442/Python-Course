"""def add(a, b):
    return a + b

result = add(10, 20)

print(result)
"""
#task2
"""def check_result(name, marks):

    if marks >= 50:
        return "Pass"
    else:
        return "Fail"
result = check_result("Noor", 75) 
print(result) """ 
#task3 
"""def discount(price):
    if price >= 5000:
        return "Discount Availible"
    else:
        return "Not Availible"
result = discount(6000)
print(result) """
#task4
"""def total(price, quantity):
    total = price * quantity
    return total
result = total(500, 3)
print(result)    """ 
#task5
"""product = input("Enter your product: ")
price = int(input("Enter your price: "))
quantity = int(input("Enter product quantity: "))
def calculate_total(price, quantity):
    total = price * quantity
    return total
result = calculate_total(price, quantity) 
print(product, result) """
#task6
def calculate_discount(price):
    if price >= 5000:
        discount = price * 10 / 100
        final_price = price - discount
        return final_price
    else:
        return "orignal price" 
result = calculate_discount(7000) 
print(result)                          