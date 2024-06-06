import random as r


def guess(ans):

    user = int(input("Enter your guess "))
    if ans == user:
        print("You won you guessed correctly ")
    else:
        if ans > user:
            print("Your guess is smaller guess larger ")
            guess(ans)
        else:
            print("your guess is larger guess smaller ")
            guess(ans)


lower_limit = int(input(" enter the lower limit of the range "))
upper_limit = int(input(" Enter the upper limit of the range "))
number = r.randint(lower_limit, upper_limit)

guess(number)
