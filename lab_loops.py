rangr_numbers= range(45,210)

for n in rangr_numbers:
    if n == 205 :
        break
    if n == 100:
        continue
    print("the number is : ", n)
    
print("-"*20)

count = 0
answer = (7*24)
while int(input("what is the product of 7 * 24 ? \n the answer: ")) != answer:
    count += 1
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly , number of attempts", count)    
     
