num =int(input("enter number positive integer: "))
for n in range(num %2==0):
    num+=num
    print(f"The sum of even numbers is {num}")
    