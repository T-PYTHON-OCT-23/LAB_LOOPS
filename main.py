for n in range(45,210):
    if n==100:
        continue
    if n==205:
        break
    print(n)

ans=False
while not ans:
    res=int(input("what is the product of 7 * 24 ?"))
    if res==168:
        ans=True
    else:
        print("Wrong answer, try again")
else:
    print("Good job")

while True:
    try:
        number=int(input("Enter a number: "))
        if number>=1:
            break
    except ValueError:
        print("You didn't enter a valid number")

sum=0
for n in range(2,number+1,2):
    sum+=n

print("The sum of even numbers is: ",sum)
