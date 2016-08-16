import random

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    die = int(input("How many die?\n"))
    print ("Rolling the die...")
    print ("The values are....")
    for num in range(0, die):
        print (random.randint(1, 6))

    roll_again = input("Roll the dices again?\n")
    
