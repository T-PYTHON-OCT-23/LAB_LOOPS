numbers= range(45,210)
for n in numbers:
    if n==100:
      continue
    if n==205:
     break
    print(n)
i="what is the product of 7 * 24?"
trials = 3
while input(i) != "168":
    trials -= 1
    if trials <= 0:
       print("You used all your tries")
       break
    print(f"Try again. {trials} left ")
else:
    print( "You answered this Question correctly")
   
155
'''
Ask the the user : "what is the product of 7 * 24 ?"
check if the answer is right then exit the loop and print "You answered this Question correctly"
if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
'''
'''
by programmer alya..

'''