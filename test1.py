##Q1 — For Loop
##1 se 10 tak numbers print karo.
##for i in range(1, 11):
 ##   print(i)
 ##   Q2 👇1 se 20 tak sirf even numbers print karo.
"""for i in range(2, 21, 2):
    print(i)"""
##Q3 🐍While loop:10 se 1 tak reverse counting print karo 

"""i = 10
while i >= 1: 
    print(i)
    i -= 1"""
##Q4 🐍While loop se 2 se 20 tak EVEN numbers print karo. 
"""i = 2
while i <= 20:
    print(i)
    i = i + 2 """
## q5 User se number lo aur 1 se us number tak counting print karo.
"""num = int(input("give me a one number: "))
i = 1
while i <= num:
    print(i)
    i += 1"""
## 🧪 Q6: Input + While + If
##User se ek number lo aur 1 se us number tak sirf odd numbers: 
"""num = int(input("Give me a number: "))

i = 1

while i <= num:

    if i % 2 != 0:
        print(i)

    i += 1  """
 ## find even number
"""num = int(input("Enter a number: ")) 
if num % 2 == 0:
    print("Even") 
else:
    print("odd")"""
## User se ek number lo.
##Program ko:1 se us number tak jaana hai.
##Har number ko check karna hai:even hn ya odd
num = int(input("Enter a number: "))

i = 1

while i <= num:

    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

    i += 1
