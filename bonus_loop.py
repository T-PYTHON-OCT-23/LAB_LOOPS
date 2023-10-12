number:int = int(input("Enter a positive integer: "))
total=0

if number.is_integer() :
 for n in range(1,number+1):
    if n % 2 ==0 :
        total+=n
        
    else:
       continue

else:
   print("Try again with an integer")
   

print(f"The sum of even numbers between 1 and {number} is {total}.")