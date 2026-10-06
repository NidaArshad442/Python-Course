"""city = ["Lahore", "karachi", "kamalia"]
print(city[2])"""
"""fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])"""
#Ab List ka next important concept: append()
#Agar list mein new item add karna ho, append() use karte hain:
"""city = ["Lahore", "sialkot", "karachi"]
city.append("muree")
print(city)"""
#3
"""students = ["Ali", "Sara", "Ahmed"]

print(students)

students.append("Nida")

print(students)"""
#list me remove krna ho kese ko remove use krty hn remove()
"""students = ["Ali", "Sara", "Ahmed", "Nida"]
students.remove("Sara")
print(students)"""
#list me kitny items hn y count krny ky liy len() use hota hn
"""students = ["Ali", "Sara", "Ahmed", "Nida"]

print(len(students))"""
"""fruits = ["apple", "banana", "mango", "orange", "grapes"]
print(len(fruits))"""
# list ka 5 concept hn insert() krna
"""cities = ["Lahore", "Karachi", "Islamabad"]
cities.insert(1, "Faisalabad") 

print(cities) """
#append()  → end mein add
#insert()  → specific index par add
#remove()  → value se remove
#pop()     → index se remove
#len()     → total items count
##task7 pop()
"""students = ["Ali", "Sara", "Ahmed", "Nida"]
students.pop(2)
print(students)"""
##task using for loop print values
"""students = ["Ali", "Sara", "Ahmed", "Nida"]
for student in students:
    print(student)"""
#Next Task — List + for + if
#Ab hum list + loop + condition combine karenge
"""marks = [45, 70, 30, 80, 55]
for mark in marks:
    if mark >= 50:
        print(mark, "pass")
    else:
         print(mark, "fail")"""
#task8
"""cities = ["Lahore", "Karachi", "Islamabad"]
cities.pop(1)
cities.insert(1, "faisalabad")
print(cities) """  
#task
"""students = ["Ali", "Sara", "Ahmed", "Nida"]
students[2] = "hamza" 
print(students)  """
#task
"""products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
products[1] = "Wireless mouse" 
products.append("Headphones") 
print(products)"""
#task
"""cart = ["Shirt", "Shoes", "Watch", "Bag"]
cart.pop(2)
cart[1] = "Sneakers"
cart.append("cap")
print(cart)"""
#task
"""colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors[2] = "Pink"
print(colors)"""
#task
"""students = ["Ali", "Sara", "Ahmed", "Nida"]
marks = [45, 70, 30, 80]

for i in range(len(students)):
    if marks[i] >= 50:
        print(students[i], marks[i], "Pass")
    else:
        print(students[i], marks[i], "Fail")"""
#task 15
"""products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [80000, 2000, 5000, 30000]
for i in range(len(products)): 
    print(products[i], prices[i]) """ 
#task16
"""products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [80000, 2000, 5000, 30000]
for i in range(len(products)): 
    print(products[i], prices[i])
    if prices[i] >= 5000:
        print("Expensive")
    else:
        print("Affordable") """ 
#task17 
"""students = ["Ali", "Sara", "Ahmed", "Nida"]
marks = [45, 70, 30, 80]
for i in range(len(students)):
    if marks[i] >= 50:
        print(students[i], marks[i],"pass")
    else:
        print(students[i], marks[i], "fail")  """ 
#task18
"""products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [80000, 2000, 5000, 30000]
for i in range(len(products)):
    if prices[i] >= 5000:
        print(products[i], prices[i])"""
#task19
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [80000, 2000, 5000, 30000]
for i in range(len(products)):
    if prices[i] < 5000:
        print(products[i], prices[i])        


            