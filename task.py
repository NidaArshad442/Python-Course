#task no 1
"""name = input("Enter student name: ")
marks = int(input("Enter marks: "))
if marks >= 50:
    print(name, "You passed")
else:
    print(name, "You failed")"""  
#task2
"""product = input("Enter your product: ")

price = int(input("Enter price: "))

quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 5000:
    print("You got a discount")
else:
    print("No discount")

print(product, "Total:", total)"""
# task3
"""correct_password = "python123" 
attempt = 1
while attempt <= 3:
    password = input("Enter your password: ")

    if password == correct_password:
        print("you login successfully")
        break
    else:
        print("Wrong password")

    attempt += 1"""
#task 4
"""def student(name, marks):
    print("Name", name)
    print("Marks", marks)

    if marks >= 50:
        print("Pass")
    else:
        print("Fail")

student("Hazib", 75)
               """
#task5
def check_age(name, age):
    print("Name", name)
    print("Age", age)
    if age >= 18:
        print("You are eligible") 
    else:
        print("you are not eligible") 
check_age("Hazib", 19)                         