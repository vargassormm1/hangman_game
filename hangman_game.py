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

while(wrong_guesses < chances):
    user_guess = input("Enter a letter to guess: ")


    if user_guess in word_to_guess:
        right_guesses += user_guess

        for letter in word_to_guess:
            if letter in right_guesses:
                print(letter, end=" ")
            else:
                print('_', end=" ")
        print()
    
    if(len(right_guesses) == len(letters_to_guess)):
        print('Congrats!!')
        break
