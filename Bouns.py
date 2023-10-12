num=int(input("Enter the positive number: "))
sum=0

for i in range(1,num+1):
    if i%2==0:
        sum+=i    
print("The sum of even numbers between 1 and ",num,"is",sum)