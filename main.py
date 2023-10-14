print("Q1")
print()

numbers  = range(45, 210)

for num in numbers:
    if num ==100:
        continue
    if num ==205:
        break
    print(num)
num+=1

#Q2

print()
print("Q2")

answer = "what is the product of 7 * 24 ? "
result = "168"

while input(answer) != result:
        print("Your Answer is wrong try again..")
        continue
else:   
        print("You answered this Question correctly")     
 
