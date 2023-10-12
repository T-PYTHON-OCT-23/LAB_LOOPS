

number=input("Enter a positive integer:")



while not number.isnumeric():
    print("The Entry wrong")
    number=input("Enter a positive integer:")
    
    
    
    
r = int(number)
num_even=[]

for n in range(0,r + 1,2):
    num_even.append(n)
    
    

sum_even=sum(num_even)

print(f"The sum of even numbers between 1 and {number} is {sum_even}.")


