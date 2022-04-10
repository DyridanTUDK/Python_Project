# Dont change the code below 👇
# Password Generator Projects
import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','(',')','*','+']
print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your passwords?\n"))
nr_symbols = int(input("How many symbols would you like in your passwords?\n"))
nr_numbers = int(input("How many number would you like in your passwords?\n"))
# Dont change the code below 👆
# Hard Mode
random_pass = []
for i in range(1,nr_letters+1):
    random_pass.append(random.choice(letters))
for i in range(1,nr_numbers+1):
    random_pass.append(random.choice(numbers))
for i in range(1,nr_symbols+1):
    random_pass.append(random.choice(symbols))

random_prnt_pass = ''
for i in range(1,len(random_pass)+1):
    random_prnt_pass+= random.choice(random_pass)

print(random_prnt_pass)