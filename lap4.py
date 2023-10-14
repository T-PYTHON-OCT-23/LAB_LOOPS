
for number in range(45,210):
    print(number)
    if number == 100 :
        continue
    elif number== 205 :
        break


Mathimatical_Qustion = "what is the product of 7 * 24 ?"
trials = 3
while int(input (Mathimatical_Qustion)) != 168:
    print("Your Answer is wrong try again..")

    trials -=1
    if trials ==0 :
        print("You used all your tries")
        break
    print(f"Try again.")
else:
    print ("You answered this Question correctly")
