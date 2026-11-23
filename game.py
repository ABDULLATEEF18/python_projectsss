
import random


def main():
  
    # Generate a random number between 1 and 20
    random_number = random.randint(1, 20)
     
    print(random_number)
    
    # Keep track of the number of attempts
    
    attempts = 0
   
    
   
    print("===================================")
    print("       NUMBER GUESSING GAME")
    print("===================================")

    print("I have selected a number between 1 and 20.")
    print("Try to guess the number!")
    print()

    # Continue asking until the player guesses correctly
    while True:
        # try and except block
        try:

            # Collect the player's guess and use it to explain casting
            player_guess = int(input("Guess a number: "))
            
            # Check whether the guess is within the valid range using a conditional if statement.
            if player_guess < 1 or player_guess > 20:
                print("This guess is not a valid one! ")
                continue
            
            # Increase the attempt counter
            attempts += 1
            
            # Compare the guess with the secret number using if, elif and else statements.
            
            if player_guess < random_number:
                print("Guess is lesser than number! ")
                
            elif player_guess > random_number:
                print("Guess is larger than number! ")
                
            else:
                print("\n Congratulations you guessed correctly! ")
           
                #print the number of attempts
                print(f"you guessed in {attempts} attempts congratulations")
                 
                # the break statement to eventually break out of the loop.
                break
              

              
        except ValueError:
              print("Invalid input! Please enter a whole number.")


# Run the game
if __name__ == "__main__":
    main()
