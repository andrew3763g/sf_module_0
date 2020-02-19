<<<<<<< HEAD
print(" Think of an integer number ")
print(" Think of a range of numbers containing your number ")
limit_min = int(input("Say the lower range limit "))
limit_max = int(input("Say the higher range limit "))
print(" Guess the number within the limits, I will try to determine it ")
is_equal = "N"
new_guess = limit_min
guess_number = 0
while is_equal == "N" :
    guess_number = guess_number + 1
    new_guess_proposal = int((limit_max + limit_min) / 2)
    if new_guess_proposal == new_guess :
        new_guess = new_guess_proposal + 1
    else: new_guess = new_guess_proposal
    print(" I think the right number is " + str(new_guess))
    is_equal = input(" I got it?, Y/N ")
    if is_equal == "Y" :
        break
    is_bigger = input(" Your number is bigger then guessed? Y/N ")
    if is_bigger == "Y" :
        limit_min = new_guess
    else: limit_max = new_guess
print(" Your number is " + str(new_guess))
print(" I guessed " + str(guess_number) + " times")
input(" Press Enter to escape ")
=======
print(" Think of an integer number ")
print(" Think of a range of numbers containing your number ")
limit_min = int(input("Say the lower range limit "))
limit_max = int(input("Say the higher range limit "))
print(" Guess the number within the limits, I will try to determine it ")
is_equal = "N"
new_guess = limit_min
guess_number = 0
while is_equal == "N" :
    guess_number = guess_number + 1
    new_guess_proposal = int((limit_max + limit_min) / 2)
    if new_guess_proposal == new_guess :
        new_guess = new_guess_proposal + 1
    else: new_guess = new_guess_proposal
    print(" I think the right number is " + str(new_guess))
    is_equal = input(" I got it?, Y/N ")
    if is_equal == "Y" :
        break
    is_bigger = input(" Your number is bigger then guessed? Y/N ")
    if is_bigger == "Y" :
        limit_min = new_guess
    else: limit_max = new_guess
print(" Your number is " + str(new_guess))
print(" I guessed " + str(guess_number) + " times")
input(" Press Enter to escape ")
>>>>>>> 367b79e2540b51b54265c10749a11e14dd6aeb3f
