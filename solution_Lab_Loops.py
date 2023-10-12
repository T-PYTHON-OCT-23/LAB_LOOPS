#for loop
numbers = range(45,210)
for n in numbers:

    if n == 100 :
        continue
    if n == 205:
        break
    print(f"number: {n}")   
user = "what is the product of 7 * 24 ?"
trials = 5
#while loop
while input(user) != "168":
    print("Your Answer is wrong try again..")   
    trials -= 1
    if trials <= 0:
        print("You used all your tries")
        break
else:
    print("You answered this Question correctly")
        
       
        
