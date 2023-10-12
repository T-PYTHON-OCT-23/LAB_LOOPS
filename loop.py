# 1
for n in range(45,210):
    if n == 100 :
        continue
    if n == 205 :
        break
    print(n)
tries = 5
user_input = "what is the product of 7 * 24 ?"
corecct_answer = "168"
print("You have 5 tries for this buzzle")
while input(user_input) != corecct_answer:
    print("Your Answer is wrong try again..")
    tries -= 1
    print(f"You have {tries} left")
    if tries == 0 :
        break
else:
    print("You answered this Question correctly")