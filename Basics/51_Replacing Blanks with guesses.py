#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


guess = input("Guess a letter: ").lower()
chosen_word_length=len(chosen_word)
display=[]
for i in range(chosen_word_length):
    display.append("_")
#Alternative: display=[]
              # for letter in chosen_word:
              #     display+="_" PTR:This Short hand can be used to lists aswell


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


for position in range(chosen_word_length):  #Note:The position takes the values 0,1,2,to the lenght of the chosen word
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter


#Error:This would be a wrong way as the index function keeps returning the same index 0 for all b letters in the word baboon.

# for letter in chosen_word:
#     if letter==guess:
#         index_of_guess=chosen_word.index(guess)  PTR:FUCK YOU INDEX FUNCTION
#         display[index_of_guess]=guess





#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)