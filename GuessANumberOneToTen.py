# One of the guided scripts generated during Codecademy's ....
# ... Python 2 web tutorial
# modifified slightly by me


from random import randint


random_number = randint(1, 10)

guesses_left = 3

print("Are you a winner or a loser?")
print("To win, correctly guess a number between one and ten.")
print("You have three tries.")

attempt = int(0)

while guesses_left > 0:
    odds = round((float((1/(10-attempt)))*100))
    print("The odds of a corect guess are",odds,"%")
    guess = int(input("Guess a number between 1 and 10: "))
    guesses_left -= 1
    if guess == random_number:
        print("You win, winner!")
        break
    else:
        if guesses_left > 0:
            print("Try again.")
    
    attempt += 1
else:
    print("You lose, loser!")
