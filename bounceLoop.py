'''
Write a Python program that prompts the user for a positive integer n,
 and then calculates the sum of all even numbers between 1 and n, inclusive.

Your program should use a loop (either a for loop or a while loop) to iterate over
 the numbers between 1 and n, and only add the even numbers to the sum.

'''




num = int(input('Enter a number: '))
sum = 0
i = 0
while i <= num:
    if i % 2 == 0:
        print(i)
        sum+=i
    i+=1
print(f"Sum of all the even numbers is {sum}")


'''py programmer Alya'''