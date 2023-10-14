number ="Please Enter a positive number: "
total = 0


while int(input(number)) %2 ==0:
        
        if int(number) % 2 ==0:
              total +=number

        print(f"The sum of even numbers between  1 and {number}  is {total}.")  
else:
    print("Please Enter a positive number Only") 

'''
for even in int(number):
    if even % 2 == 0:
        total += even
        even -= 1
    print(f"The sum of even numbers between  1 and {number}  is {total}.")  
  
    if even % 2 == 1:
        print("Please Enter a positive number Only") 
        
'''
