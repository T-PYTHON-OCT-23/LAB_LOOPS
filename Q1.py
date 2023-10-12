numbers = range(45,211)
for n in numbers:
    if n==100:
        print("\nskipped\n")
        continue
    elif n==205:
        print("\nthe number is ",n,",thus will break the loop\n")
        break
    print(n)
else:
    print("counting is done succesfully")