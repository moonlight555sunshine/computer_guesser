# Prompt the user to think of a number
print("Think of a number between 0 and 1000, and I'll guess it in no more than 10 tries")
# Initialize the search range
max_number = 1000
min_number = 0
# Start the guessing loop
while True:
    # Calculate the middle of the current range
    guess_number = int((max_number - min_number) / 2) + min_number
    print(f"I think it's {guess_number}")
    # Ask the user for feedback
    answer = input("Is it correct? (Too small/Too big/correct) ")
    # Handle user response
    if answer.lower().strip() == "correct":
        print("I'm win!")
        break
    elif answer.lower().strip() == "too big":
        # If guess is too big, adjust upper bound
        max_number = guess_number
        continue
    elif answer.lower().strip() == "too small":
        # If guess is too small, adjust lower bound
        min_number = guess_number
        continue
    else:
        # Handle unexpected input
        print("Don't lie!")
        continue