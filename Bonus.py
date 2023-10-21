number= 1
total= 10

while number < 5 :
    intro = input('give a number')
    num=int (intro)
    total += num
    number += 1

    print('Total is:' , total)