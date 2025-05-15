# Gives varaible for numbers 
numbers_and_special_characters = "1234567890!@#$%^&*()_+[]\:;,.?/"
# Asks for password and 
print("Lets assess your pasword strength, we reccomend a password over 8 characters, and with at least one number or special character {}".format(numbers_and_special_characters))
password = input("What is your password")
# Strips password of any spaces 
password.strip()
# Sees if the pasword length is under 8 characters 
if len(password) <8:
    print("Oh no your password is too short! Please use a password with over 8 characters")
# Sees if the password does not contain any numbers 
elif len(password) >8 and any(i in numbers_and_special_characters for i in password) == False:
 print("Oh no it looks like you do not have any numbers or special characters in your password Please add some to make it more secure")
# Says the person has a good password
else: 
   print("Your password is strong")