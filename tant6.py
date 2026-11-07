import random
import string
print("welcome to the password generator!")
tall_password=int(input("How many characters would you like your password to be? "))
letter_password=int(input("How many letters would you like in your password? "))
number_password=int(input("How many numbers would you like in your password? "))
symbol_password=int(input("How many symbols would you like in your password? "))
sum_of_characters=letter_password+number_password+symbol_password
if sum_of_characters==tall_password:
    password=[]
    t_p=random.choices(string.ascii_letters,k=letter_password)
    n_p=random.choices(string.digits,k=number_password)
    s_p=random.choices(string.punctuation,k=symbol_password)
    password.extend(t_p)
    password.extend(n_p)
    password.extend(s_p)
    random.shuffle(password)
    print(f"Your password is: {''.join(password)}")
    
else:
    print("The sum of letters, numbers, and symbols does not equal the total password length. Please try again.")    