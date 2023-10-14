number = int(input("Enter a positive integer: "))
sumEvenNumber = 0

for numbers in range(1, number + 1):
    if numbers % 2 == 0:
        sumEvenNumber = sumEvenNumber + numbers
print(f"The sum of even numbers between 1 and {number} is {sumEvenNumber}")



