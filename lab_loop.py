numbers = range(45, 210)


for n in numbers:
    if n == 100:
        continue
    print(n)
    if n ==205:
        break


result = "what is the product of 7 * 24 ? "
while input(result) != "168" :
    print("Your Answer is wrong try again.. ")
    
else:
    print("You answered this Question correctly")

