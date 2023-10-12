user_input=input("Enter a positive integer: ")
counter = 1
total = 0

while not user_input.isnumeric():
    user_input=input("Error! please enter a positive integer not a string: ")
else:
    while int(user_input) <= 0:
        user_input=input("Negative numbers and zero are not allowed, please enter a positive integer: ")
    else:
        while counter != int(user_input)+1:
            if counter%2 == 0 :
                total = total + counter
                counter+=1
            else:
                counter+=1
        else:
            print(f"The sum of even numbers between 1 and ",user_input,"is: ",total)