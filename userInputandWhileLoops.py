message = input("Tell me something you want me to repeat: ")
print(message)

age =  input("how old are you? ")
age= int(age)
if age >= 18 :
    print("true")
else:
    print("You are lying lie")

number = input("enter a number, and i will tell you if its even or not")
number = int(number)

if number % 2 == 0:
    print(str(number) + " is even")
else:
    print(str(number) + " is odd")

current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1


# letting the user quit a prompt
prompt = ("\nwhat is your name")
prompt += ("\nenter 'quit' to end the program")

active = True
while active:
    message =  input(prompt)

    if message =='quit':
        active = False
    else:
        print(message)
