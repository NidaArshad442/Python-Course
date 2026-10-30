#q1 write a progarm to print poem on screen
"""print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!
''')"""
#q2 use the repl and print 5 table using it ....repl mean cmd open krky terminal open kr ky python likh ky enter kry or code apna likhy screen py print hona shuru ho jye ga
# main ny terminal open krky likha :
print(5*1)
print(5*2)
print(5*3)
print(5*4)
print(5*5)
print(5*6)
print(5*7)
print(5*8)
print(5*9)
print(5*10)
# terminal pr humy print() nhi ikhna pra humny just 5*1 likh 5 print hogya 
#q3 module install krna or use krna 2 trha ky mof=dule hoty hn built in and external
#pip install use krky module install kry gy
## module1 
"""import pyjokes
# print("printing jokes....")
print("most funniest jokes ..)")
joke = pyjokes.get_joke()
print(joke)"""
#module2
"""import pyttsx3
engine = pyttsx3.init()
engine.say("hey i am good")
engine.runAndWait()"""
#q4 sode chatgpt sy likhwana with commit wala or without commit wala
# Import os module
import os

# Specify the directory you want to list
directory_path = '/New folder'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)