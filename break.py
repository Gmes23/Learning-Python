prompt = ("\nwhat is your name: ")
prompt += ("\nenter 'quit' to end the program")

while True:
    message =  input(prompt)

    if message == 'quit':
        break
    else:
        print(message)
