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
answer = 28

while input(Question) != "answer":
        print("That's wrong Try again..")
else:
    print("Great! You answered this Question correctly")
