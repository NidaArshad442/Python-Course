#Practice Task 1 — Input → If/Else → Variable
"""name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if marks >= 50:
    print(name, "pass")
else:
    print(name, "fail")"""
#Task 2 — elif Revision
"""name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Grade A")  
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade c") 
else:
    print("fail")  """
#Task 3 — for + List + if/else 
"""marks = [45, 70, 30, 80, 55]
for i in range(len(marks)):
    if marks[i] >= 50:
        print(marks[i], "pass")
    else:
        print(marks[i], "fail")                  """
#Task 4 — for + List + if/else + %
"""numbers = [10, 15, 22, 31, 40, 47]

for number in numbers:
    if number %2 == 0:
        print(number, "Even")
    else:
        print(number, "Odd") """ 

#🟢 Task 5 — while + input + if/else + break
"""correct_password = "python123"
attempt = 1

while attempt <= 3:

    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        print("Wrong password")

    attempt +=  1              """
# Task 6 — while + % + if/else
"""i = 1

while i <= 10:

    if i %2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

    i += 1 """
#   Task 7 — Function + Parameter + return 
"""def function_name(price, quantity):
    total = price * quantity
    return total

result = function_name(500, 4)
print(result)  """ 
# Task 8 — Function + Parameter + if/else + return
"""def check_result(name, marks):
    if marks >= 50:
        return "pass"
    else:
        return "fail"

result = check_result("Abeer", 98)
print("Abeer", result)"""
#Task 9 — Function + List + for + if/else
"""def check_marks(marks):
    for mark in marks:
        if mark >= 50:
            print(mark, "Pass")
        else:
            print(mark, "Fail")


marks = [45, 70, 30, 80, 55]

check_marks(marks)"""
#task10 — Function + Parameters + if/else + return
"""def calculate_discount(price):
    if price >= 5000:
        discount = price * 10 / 100
        final_price = price - discount
        return final_price
    else:
        return "no discount"

result = calculate_discount(7000)
print(result)"""
#Task 11 — Function + Parameters + return + Calculation
def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(1200, 3) 
print(result)  
