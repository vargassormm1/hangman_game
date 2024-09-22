import random

fruits = ['apple', 'banana', 'mango', 'strawberry',
'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 
'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

word_to_guess = random.choice(fruits)

print("Guess the word! HINT: word is a name of a fruit")
for letter in word_to_guess:
    print('_', end=' ')
print()

chances = len(word_to_guess) + 2
wrong_guesses = 0
right_guesses = ''
letters_to_guess = "".join(list(set(word_to_guess)))
wrong_letters = []

while(wrong_guesses < chances):
    user_guess = input("\nEnter a letter to guess: ").lower()

    if user_guess in right_guesses or user_guess in wrong_letters:
        print('You already guessed that letter. Try another one!')
        continue

    if user_guess in word_to_guess:
        right_guesses += user_guess

        for letter in word_to_guess:
            if letter in right_guesses:
                print(letter, end=" ")
            else:
                print('_', end=" ")
        print()
    
        if(len(right_guesses) == len(letters_to_guess)):
            print('Congratulations, You won!!!')
            break
    else:
        wrong_guesses += 1
        wrong_letters.append(user_guess)

        for letter in word_to_guess:
            if letter in right_guesses:
                print(letter, end=" ")
            else:
                print('_', end=" ")
        print()
        
        print('\n--------------------------------------------------------------------')
        print(f"Wrong guess! You have {chances - wrong_guesses} chances left.")
        print(f"Wrong guesses so far: {', '.join(wrong_letters)}")
        print('--------------------------------------------------------------------\n')

