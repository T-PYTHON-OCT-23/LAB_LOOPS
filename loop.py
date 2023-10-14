#(1)using range loop
iterate = range(45, 210)

for r in iterate:
    if r == 100:
        continue
    if r == 205:
        break
    print(r)

#(2)using while loop
Question = "Find the result of multiplying 7 by 4"
trials = 10 

while input(Question) != 28: 
    trials -= 1
    if trials <= 0: 
        print("You used all your tries! the answer is 28.")
        break
    print(f"That's wrong Try again.. {trials} left ")
else:
    print("Great! You answered this Question correctly")