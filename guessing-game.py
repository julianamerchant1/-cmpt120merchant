# guessing-game.py Finish Tues Oct 2018
def main():
    print("I'm thinking of an animal that lives in the jungle...")
    animal = input("Guess what it is! ")
    animal.lower
    if animal == "monkey":
        print("You guessed it! ")
    else:
        print ("Wrong animal! Quit? (if you wish to continue, guess again!): ")
    continue
#tried to use continue function above to repeat the program if the user retries,
#but it gives me an error: "'continue' not properly in loop", no matter where i move it
#if not that error due to moving the function, it alternatively tells me there is incorrect indentation
#without 'continue', the program does not loop
#i get an error message when the new second animal is guessed
#even if the guess is correct and they type monkey
main()
