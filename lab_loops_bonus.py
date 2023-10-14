print("This program calculate the sum of even numbers.")
value = input("Enter a positive integer: ")
result =0 
for num in range(2, int(value)+2, 2):
    print(num) #Only display the even numbers.
    result = result + num #Calculate the sum and store the value in result.

print(f"The sum of even numbers between 1 and {value} is: {result}") 

    


    
    


        


