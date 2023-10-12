number = int(input("please enter the positive integer: "))
sum = 0
for n in range(1,number+1):
    if n % 2 == 0:
        sum = sum+n
print(f"The sum of even numbers between 1 and {number} is: {sum}")
