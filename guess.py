import random

num = random.randomint(1,100)

print("Welcome to number guessing game!")
print("Choose a number between 1 and 100")
print("If your choice is 10 numbers away from my number, I'll tell you 'FAR'.")
print("If your choice is within 10 of my number, I'll tell you you 'CLOSE'.")
print("If your choice is farther than your most recent guess, I'll say you 'FURTHER'.")
print("If your choice is closer than your most recent guess, I'll say you'CLOSER'.")
print("LET'S PLAY!")

guesses = [0]
   
while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('CLOSER!')
        else:
            print('TOO FAR!')
   
    else:
        if abs(num-guess) <= 10:
            print('CLOSE!')
        else:
            print('FAR!')
