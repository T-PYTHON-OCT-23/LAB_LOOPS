
num:int =input("Enter a positive integer:")
sum=0
i=1

while i <= num :
    if i % 2 == 0:
         sum +=i
i+=1
print("the sum of even numbers is :",sum)